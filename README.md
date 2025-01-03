# 뉴스 감정 예측 및 주가와의 상관관계 분석

### Technology Stack 🔨
`#Python` `#Pandas` `#Sklearn` `#Tensorflow` `#KLUE/BURT` `#Matplotlib` `#Bs4` `#Naver API` `#K-TACC` `#FinanaceDataReader`


### Platform 🔧
`#Python` `#Anaconda` `#Jupyter Notebook`

___

### 프로젝트 개요
- 해당 프로젝트는 특정기업 관련된 뉴스 데이터를 수집하여 감정 점수를 예측하고, 이를 바탕으로 주가 변동성과의 상관관계를 분석하는 것을 목표로 합니다.
- 이를 통해 뉴스 데이터를 활용한 데이터 기반 투자 전략 설계 및 예측 모델의 가능성을 탐구합니다.

*해당 프로젝트에서는 SK하이닉스를 대상으로 진행되었습니다.*

___

### 프로젝트 구조
```
.
├── data/                      # 수집한 뉴스 및 주가 데이터
├── modules/
│   ├── news_crawler.py                             # 네이버 뉴스 데이터 수집
│   ├── sentiment_analysis.ipynb                    # 뉴스 감정 예측 모델 학습
│   ├── augmented_subject_focus_data.ipynb          # 데이터 증강
│   ├── subject_focus_finetuning.ipynb              # 다수의 주체 뉴스 Fine-Tuning
│   ├── day_sentiment_scores.ipynb                  # 감정 점수 계산 및 시각화
│   └── stock_and_sentiment_visualization.ipynb     # 감정 점수와 주가 상관관계 분석
│
├── README.md 
└── requirements.txt           # 프로젝트 의존성 목록
```

___

### 주요기능
#### 1. 뉴스 데이터 수집
`news_scraper.py`
- 네이버 뉴스 API를 활용하여 SK하이닉스 관련 뉴스를 수집합니다.
- 윤리적이고 합법적인 데이터 수집 방식을 준수하며, 자동화 스크립트를 통해 최신 데이터를 지속적으로 축적합니다.

#### 2. 뉴스 감정 예측 모델 학습
`sentiment_analysis.ipynb`
- 한글 문맥 분석에 최적화된 KLUE BERT 모델과 [금융 뉴스 문장 감성 분석 데이터셋](https://github.com/ukairia777/finance_sentiment_corpus)을 기반으로 모델을 학습시킵니다.
- 데이터 전처리, 탐색적 데이터 분석(EDA), Fine-Tuning을 통해 모델 성능을 최적화합니다.

#### 3. 다수의 주체가 포함된 데이터 증강 및 Fine-Tuning
`augmented_subject_focus_data.ipynb` `subject_focus_finetuning.ipynb`
- 다수의 주체가 포함된 문장에서 감정 예측 성능을 개선하기 위해 예측에 실패한 데이터를 직접 선별하고 [K-TACC](https://github.com/kyle-bong/K-TACC)를 사용하여 데이터 증강을 수행하여 데이터셋을 생성했습니다.
- 뉴스 문장의 기업명을 <SK하이닉스>으로 변환하고 <SK하이닉스>을 고유 토큰을 추가하여 모델이 문맥 내 주요 주체를 명확히 학습하도록 구성했습니다.

#### 4. 감정 점수와 주가의 상관관계 분석
`day_sentiment_scores`, `stock_and_sentiment_visualization.ipynb`
- 뉴스 감정 점수와 SK하이닉스의 주가 변동성을 비교 분석합니다.
- 시각화 및 상관관계 분석을 통해 감정 점수가 주가에 미치는 영향을 도출했습니다.

___

### 프로젝트 주요 결과
#### 1. 뉴스 감정 예측의 정확도
- KLUE BERT 모델을 사용하여 네이버 API로 추출한 뉴스 데이터를 감정 분석에 적용한 결과, 모델은 뉴스 문장의 맥락을 잘 반영하여 긍정적 또는 부정적 감정을 정확히 예측할 수 있었습니다. 특히 다수의 주체가 포함된 뉴스에서도 잘 작동하였으며, 예를 들어 2024년 11월 7일의 부정적인 뉴스는 다음 날 주가 하락과, 2024년 11월 21일의 긍정적인 뉴스는 주가 상승을 유도하는 경향을 보였습니다.

#### 2. 감정 점수와 주가의 상관관계
- 뉴스 감정 점수와 주가 간의 상관계수는 0.2로 다소 약한 상관관계를 보였으나, 두 변수 간의 관계는 비선형적일 가능성이 높습니다. 주가의 반응은 뉴스 감정 점수의 크기에 따라 다르게 나타날 수 있으며, 예를 들어 매우 긍정적인 뉴스는 큰 주가 상승을 이끌 수 있지만, 경미한 긍정적인 뉴스는 영향을 미치지 않을 수 있습니다. 또한, 뉴스 특성상 오늘날의 주가에 대한 뉴스도 다수 존재하기 때문에 감정 점수와 주가의 상관관계가 아니라 주가와 감정 점수의 관계가 나타날 수도 있습니다.

#### 3. 분석의 한계
- 수집된 뉴스 데이터의 양이 적고 분석 기간이 짧아 정확한 상관관계를 도출하는 데 어려움이 있었습니다. Prophet 라이브러리를 사용하여 주가 예측 결과와 뉴스 감정 데이터를 결합한 예측 결과를 비교한 결과, 감정 데이터가 적어서 의미 있는 예측을 도출하기 어려웠습니다. 데이터 양이 많고 상관관계가 명확해지면 투자자들에게 더 유용한 예측 모델을 제공할 수 있을 것으로 보입니다.

___
### Preview of the Project 🔍

**상관관계 시각화** (24.11.04~24.11.29)
![image](https://github.com/user-attachments/assets/38d9a526-b046-461e-afac-7ed3b434e436)

[프로젝트 발표 PPT](https://github.com/KION126/StockSentimentPredictor/blob/master/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EB%B0%9C%ED%91%9C%20PPT.pdf)

[프로젝트 결과 보고서](https://github.com/KION126/StockSentimentPredictor/blob/master/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EA%B2%B0%EA%B3%BC%20%EB%B3%B4%EA%B3%A0%EC%84%9C.pdf)

