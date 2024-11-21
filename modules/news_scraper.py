import os
import csv
import re
from datetime import datetime
from bs4 import BeautifulSoup
from html import unescape
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_news(company_name, client_id, client_secret, num_articles=100):
    url = 'https://openapi.naver.com/v1/search/news.json'
    params = {
        'query': company_name,
        'display': num_articles,  # 요청할 뉴스 개수
        'sort': 'date'  # 최신순 정렬
    }
    headers = {
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        items = response.json()['items']
        return items
    else:
        print("Error:", response.status_code)
        return []

def clean_html(raw_html):
    """HTML 태그와 HTML 엔티티를 제거하고 텍스트만 반환하는 함수"""
    if isinstance(raw_html, str) and ('<' in raw_html and '>' in raw_html):  # HTML 형식 체크
        soup = BeautifulSoup(raw_html, 'html.parser')
        text = soup.get_text()  # HTML 태그 제거
        return unescape(text)  # HTML 엔티티 처리
    return unescape(raw_html)  # HTML이 아닌 경우에도 unescape로 처리

def clean_text(text):
    """특수문자 제거 및 정리하는 함수"""
    text = re.sub(r'[^\w\s]', '', text)  # 특수문자 제거
    return text.strip()  # 공백 제거


def save_news_to_csv(news_items):
    # ..news_data 디렉토리 생성
    os.makedirs('/home/ec2-user/stock_sentiment_predictor/news_data', exist_ok=True)
    file_path = '/home/ec2-user/stock_sentiment_predictor/news_data/news_data.csv'

    # 기존 데이터 읽기
    existing_news = set()
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                existing_news.add((row[0], row[1], row[2]))  # (날짜, 제목, 요약)

    # 새 데이터 추가
    with open(file_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for item in news_items:
            pub_date = item['pubDate'].split(', ')[1]  # 날짜 부분만 가져오기
            pub_date = datetime.strptime(pub_date, '%d %b %Y %H:%M:%S %z').strftime('%Y_%m_%d_%H:%S')  # 포맷 변경
            title = clean_text(clean_html(item['title']))  # HTML 및 특수 문자 제거
            description = clean_text(clean_html(item['description']))  # HTML 및 특수 문자 제거

            # 중복 체크
            if (pub_date, title, description) not in existing_news:
                writer.writerow([pub_date, title, description])

def main():
    client_id = 'CLIENT_ID'
    client_secret = 'CLIENT_SECRET'
    company_name = 'sk하이닉스'

    print("Fetching news...")
    news_data = fetch_news(company_name, client_id, client_secret)
    if news_data:
        save_news_to_csv(news_data)
        print(f"Saved {len(news_data)} news articles to CSV.")

if __name__ == "__main__":
    main()
