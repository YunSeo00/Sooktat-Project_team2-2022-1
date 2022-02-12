## 20220212 회의 기록 저장소입니다. 

#### 다음 주 회의: 2월 19일 8시

#### 할 일 
1. 모델 적합 및 훈련
    - sub_train data, valid data rmsle
    - full_train data(sub_train_data + vaild data), test_data rmsle(kaggle submit)

2. 역할 배분
    - 목표: 데이터 넣고 모델이 돌아가면 됨. 1의 결과를 얻어보기.
    - 간단한 모델 개념 설명, 주요 하이퍼파라미터
    - 더 해 볼 수 있는 것: 위에서 찾은 주요 하이퍼파라미터 값을 조정하면서 가장 좋은(valid에서의 성능이 가장 좋은) 하이퍼파라미터 조합 찾아보기

    - Lasso, Ridge, (Elastic Net) (교호작용항 X) - 정소영
    - Lasso, Ridge, (Elastic Net) (교호작용항 O) - 고나경
      - https://subinium.github.io/MLwithPython-4-3/
    - SVM(support vector machine) - 김은호
    - (Bagging) : RandomForest, (ExtraTree) - 전소연
    - (Adaboost), XGBoost(Extreme Gradient Boosting) - 김윤진
    - lightGBM - 윤서

3. data split (기존과 동일)
  - train data : (맨 처음) ~ 2016/7/31 (train_merge_data.npy)
  - valid data : 2016/8/1 ~ 2017/8/15 (train_merge_data.npy)
  - test data : 2017/8/16 ~ 2017/8/30 (test_merge_data.npy)

4. final_data_set_download
  - [final_train_data](https://drive.google.com/file/d/1u3xxnkpHDMU7OFqxbWpUufjWOXLDHrla/view?usp=sharing)
  - [final_test_data](https://drive.google.com/file/d/1aZpGLwqALWpQhngJxc9GmYkaGFELDFeT/view?usp=sharing)
