/*
    - 생산일자가 2022년 5월
    - 총 매출 내림차 , 식품 ID 오름차
*/
SELECT po.PRODUCT_ID, 
        p.PRODUCT_NAME, 
        (po.TOTAL_AMOUNT * p.PRICE) AS TOTAL_SALES
        # po.TOTAL_AMOUNT,
        # p.PRICE
FROM 
(SELECT PRODUCT_ID, SUM(AMOUNT) AS TOTAL_AMOUNT
FROM FOOD_ORDER
WHERE PRODUCE_DATE BETWEEN '2022-05-01' AND '2022-05-31'
GROUP BY PRODUCT_ID) as po INNER JOIN 
(SELECT PRODUCT_ID, PRODUCT_NAME, PRICE
 FROM FOOD_PRODUCT 
 WHERE PRICE IS NOT NULL)as p ON po.PRODUCT_ID = p.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID

# SELECT PRODUCT_ID, PRODUCT_NAME, PRICE
#  FROM FOOD_PRODUCT 
#  WHERE PRICE IS NOT NULL