/*
 - 대여 시작일 : 2022년 9월에 속하는
 - 대여 기간 30일 이상 : '장기 대여'
 - 대여 기간 30일 미만 : '단기 대여'
 - "RENT_TYPE"으로 추가
 - 대여 기록 ID 내림차
 
 IF(DATEDIFF(END_DATE,START_DATE) > 30, "장기 대여", "단기 대여") AS RENT_TYPE
 - 대여 시작일도 포함해야 하기 때문에 시작일을 제외하고 차이가 29일이 나면 30일 이상 대여로 포함된다
*/
SELECT HISTORY_ID, CAR_ID, SUBSTR(START_DATE,1,10) AS START_DATE, SUBSTR(END_DATE,1,10) AS END_DATE, IF(DATEDIFF(END_DATE,START_DATE) >= 29, "장기 대여", "단기 대여") AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE BETWEEN '2022-09-01' AND '2022-09-30'
ORDER BY HISTORY_ID DESC