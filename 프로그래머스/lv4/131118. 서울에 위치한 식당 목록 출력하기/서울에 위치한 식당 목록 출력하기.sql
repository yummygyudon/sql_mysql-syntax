/*
 * 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수
 1. 리뷰 평균점수 : 소수점 세 번째 자리에서 반올림
    -  평균점수를 기준으로 내림차순 정렬, 즐겨찾기 수 내림차순
*/
SELECT r.REST_ID, r.REST_NAME, r.FOOD_TYPE, r.FAVORITES, r.ADDRESS, ROUND(AVG(v.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO as r INNER JOIN REST_REVIEW as v ON r.REST_ID = v.REST_ID
WHERE r.ADDRESS LIKE '%서울%시%'
GROUP BY r.REST_ID
ORDER BY SCORE DESC, r.FAVORITES DESC