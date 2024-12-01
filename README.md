## 뉴스 감정 예측 및 주가와의 상관관계 분석

### 프로젝트 개요
- 해당 프로젝트는 특정기업 관련된 뉴스 데이터를 수집하여 감정 점수를 예측하고, 이를 바탕으로 주가 변동성과의 상관관계를 분석하는 것을 목표로 합니다.
- 이를 통해 뉴스 데이터를 활용한 데이터 기반 투자 전략 설계 및 예측 모델의 가능성을 탐구합니다.
*해당 프로젝트에서는 SK하이닉스를 대상으로 진행되었습니다.*

---

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

---

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
`augmented_subject_focus_data.ipynb`, `subject_focus_finetuning.ipynb`
- 다수의 주체가 포함된 문장에서 감정 예측 성능을 개선하기 위해 예측에 실패한 데이터를 직접 선별하고 [K-TACC](https://github.com/kyle-bong/K-TACC)를 사용하여 데이터 증강을 수행하여 데이터셋을 생성했습니다.
- 뉴스 문장의 기업명을 <SK하이닉스>으로 변환하고 <SK하이닉스>을 고유 토큰을 추가하여 모델이 문맥 내 주요 주체를 명확히 학습하도록 구성했습니다.

#### 4. 감정 점수와 주가의 상관관계 분석
`day_sentiment_scores`, `stock_and_sentiment_visualization.ipynb`
- 뉴스 감정 점수와 SK하이닉스의 주가 변동성을 비교 분석합니다.
- 시각화 및 상관관계 분석을 통해 감정 점수가 주가에 미치는 영향을 도출했습니다.

---

### 프로젝트 주요 결과
#### 1. 뉴스 감정 예측 모델 성능
- 검증 정확도: 82.71%
- KLUE BERT 모델을 Fine-Tuning하여 뉴스에 적합한 감정 분석 결과를 확보했습니다.

#### 2. 감정 점수와 주가의 상관관계
- 감정 점수가 높은 날과 낮은 날의 주가 변동 패턴을 비교하여 의미 있는 상관성을 발견했습니다.
- 특정 날짜의 주요 뉴스 이벤트가 주가에 미치는 영향을 분석하여 투자 전략의 기초 자료를 제시했습니다.
