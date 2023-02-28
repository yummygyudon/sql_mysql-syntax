/*
 * 5월 1일 기준 -> 주문ID, 제품ID, 출고일자, 출고여부
    - 출고 여부 : 5월 1일까지 출고 완료
        - 이후 날짜 : 출고 대기
        - 없으면 : 출고 미정
*/
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, "%Y-%m-%d"), 
    (CASE 
        WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
        WHEN OUT_DATE > '2022-05-01' THEN '출고대기'
        WHEN ISNULL(OUT_DATE) THEN '출고미정'
        END) as '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID ASC