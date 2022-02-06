## 20220206 회의 기록 저장소입니다. 


### 다음 주 회의: 2월 12일 8시

### 할 일
1) 데이터 전처리 마무리
    - 다른 사람 코드 참고해서 보충할 것 더 보충하기
    - kaggle notebook 더 참고해도 좋을 것 같음.
2) 1에서 전처리된 데이터를 가지고 Regression, RandomForestRegression 모델 돌려서 검증데이터 성능 측정
    - `sklearn.metrics.mean_squared_log_error` 함수 이용. 함수 output에 root를 씌워야 kaggle의 성능 지표와 동일한 지표가 됨.
    - 검증데이터 성능 측정 시 모델 학습에 사용하는 데이터 : train_data
    - 테스트데이터 성능 측정 시 모델 학습에 사용하는 데이터 : 전체 train_data (train_data + valid_data)
    - 훈련, 검증, 테스트 데이터 분리 기준은 기존과 동일
    - 테스트데이터 성능은 kaggle에 summit 하면 확인할 수 있음.
