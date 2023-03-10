/*
 * 2022년 3월 판매 날짜, 상품ID, 유저ID, 판매량
    - OFFLINE_SALE 판매 데이터의 USER_ID : NULL
    - 판매일 , 상품ID, 유저 ID 오름차
*/
# SELECT *
# # FROM TABLE ONLINE_SALE UNION ALL TABLE OFFLINE_SALE
# FROM 
(
    SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
    FROM ONLINE_SALE
    WHERE SALES_DATE BETWEEN '2022-03-01' AND '2022-03-31'
)
UNION ALL
(
    SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, NULL as USER_ID, SALES_AMOUNT
    FROM OFFLINE_SALE
    WHERE SALES_DATE BETWEEN '2022-03-01' AND '2022-03-31'
) 
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID

# SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, SALES_AMOUNT
#     FROM OFFLINE_SALE
#     # WHERE SALES_DATE BETWEEN '2022-03-01' AND '2022-03-31'