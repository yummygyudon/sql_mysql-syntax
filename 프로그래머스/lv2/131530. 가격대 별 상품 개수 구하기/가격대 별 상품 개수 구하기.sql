-- 코드를 입력하세요
/*
SET @UNIT := -10000;
SELECT (@UNIT := @UNIT+10000) AS PRICE_GROUP,
        (SELECT COUNT(*)
         FROM PRODUCT
         WHERE PRICE >= @UNIT AND PRICE < (@UNIT+10000)) AS PRODUCTS
FROM PRODUCT
WHERE @UNIT < FLOOR((SELECT MAX(PRICE)
                FROM PRODUCT)/10000)*10000
ORDER BY PRICE_GROUP ASC

# SELECT FLOOR(75000/10000)*10000

SELECT PRODUCT_ID, PRICE
                FROM PRODUCT
                ORDER BY PRICE
*/
SELECT cal.PRICE_RANGE AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM (SELECT IF(PRICE<10000, 0, FLOOR(PRICE/10000)*10000) AS PRICE_RANGE
      FROM PRODUCT) AS cal
GROUP BY cal.PRICE_RANGE
ORDER BY PRICE_RANGE