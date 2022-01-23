# SookTat-Project_team2-2022-1
- 숙탯의 2022-1학기 kaggle competition project 진행 과정을 기록한 저장소입니다. 

## Kaggle Project

- Competitions: [Store Sales - Time Series Forecasting](https://www.kaggle.com/c/store-sales-time-series-forecasting)
- Member : 고나경, 김윤진, 김은호, 정소영, 최윤서



### 20220122
  - []()
  - []()
  - []()
  - [김은호](https://github.com/YunSeo00/Sooktat-Project_team2-2022-1/blob/ed7deb60b8df997cbfe2fad2e0587c3e50872fcd/store-sales.ipynb)
  - [최윤서](https://github.com/YunSeo00/Sooktat-Project_team2-2022-1/blob/main/ProjectCode/20220122/CYS_220122.ipynb)

### 개요
제품 수요를 예측, Corporación Favorita에서 판매되는 제품군에 대한 매출을 예측

교육 데이터 : 날짜, 상점 및 제품 정보, 해당 품목의 프로모션 여부, 판매 번호
-	목적 : 제품 수요 예측을 통해 소매업체의 제품 공급 도움
-	예상 효과 : 재고 과잉 관련 음식물 쓰레기 감소,고객 만족도 상승, 지역 상점의 필요성 확인


### 데이터 확인 
train.csv ; 학습 데이터 .
-	id
-	date 판매된 날짜
- store_nbr 제품이 판매되는 상점
-	Family 판매되는 제품 유형
-	sales 지정된 날짜에 특정 상점에서 제품군에 대한 총 판매
-	onpromotion 은 특정 날짜에 매장에서 판촉된 제품군의 총 항목 수

test.csv ; 검증 데이터 
-	id, date, store_nbr, Family, onpromotion
- sales (X) 예측

stores.csv ; 상점 정보 , city , state , type , cluster 를 포함한 메타데이터를 저장
-	store_nbr
-	city
-	state
-	type  ;A,B,C,D,AND
-	cluster 유사한 상점의 그룹 ;One-17

oil.csv ; 유가 정보 , 에콰도르는 석유 의존도가 높은 국가로 경제적인 건전성이 유가 충격에 매우 취약
-	date 날짜
-	dcoilwtico 유가

holidays_events.csv ; 휴일 정보
메타데이터가 포함된 휴일 및 이벤트
-	Date
-	Type ;Holiday,Event,Additional(휴일),Transfer(휴일),Bridge(휴일)
-	Local ;National,Local,Regional
-	Locale_name ;지역명
-	Description ;휴일/이벤트명
-	Transferred ;True(평일),False

transaction.csv ; 거래량 정보
-	Date 날짜
-	Store_nbr 상점
-	Transaction 일별 거래량

sample_submission.csv ; 올바른 형식의 샘플 제출 파일.
-	Id
-	Sales

additional Notes

public부문의 임금은 2주마다 15일과 매월 말일에 지급된다. 슈퍼마켓 판매는 이에 영향을 받을 수 있습니다.
2016년 4월 16일에 규모 7.8의 지진이 에콰도르를 강타했습니다. 지진 발생 후 몇 주 동안 슈퍼마켓 판매에 큰 영향을 미친 물과 기타 생필품을 기부하는 구호 활동에 사람들이 모였습니다. – 물, 생필품 거래량 급증

  
