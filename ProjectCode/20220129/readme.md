## 20220129 회의 기록 저장소입니다.


#### 다음 회의 날짜: 2022-02-06(일) 8시

#### 해야할 일
- 목표: 선형회귀모형, 랜덤포레스트회귀(randomforestregression)에서 돌아갈 수 있게, 'train_merge_data.pkl', 'test_merge_data.pkl' 전처리하기
- 지금까지 다른 사람 발표, 참고한 notebook들에서 얻은 정보들을 바탕으로 새로운 변수를 추가해도 좋고(lag, 푸리에변환, holiday, school_day 등등), 변수추가 안해도 되니까 자기가 부담없이 재밌는 만큼만 해요!
- transaction 예측이 이상할 수 있으니 믿지 마세요.
- 각 데이터 전처리를 왜 그렇게 했는지 이유만 있으면 됩니다. 정답은 없으니 각자 생각대로 해요!
- data split
  - train data : (맨 처음) ~ 2016/7/31 (train_merge_data.npy)
  - valid data : 2016/8/1 ~ 2017/8/15 (train_merge_data.npy)
  - test data : 2017/8/16 ~ 2017/8/30 (test_merge_data.npy)
- 주의점) test, valid data 전처리 할 때는 train data의 정보를 이용하여 전처리

- 보통의 전처리
  - 연속형 변수: 정규화(선형회귀모델의 경우, 변수의 정규성이 가정되어 있음)
  - 범주형 변수: labeling, onehotencoding 등 모델이 알아들을 수 있는 형태로 변환

- 오늘 회의하면서 좋다고 생각한 점
  - 은호님 발표에서 family 변수를 5개의 범주로 그룹화했는데 좋은 거 같음.
  - 비지도학습(클러스터링)을 이용하여 범주가 많은 변수를 몇 개의 범주로 그룹화하는 방식

- 회귀 문제에 쓰이는 모델 : 선형/다중 회귀 모형, 랜덤포레스트, 부스팅, SVM, XGB, ridge, lasso, 등등 (윤진님 파일에 더 있는 것 같아요) 
