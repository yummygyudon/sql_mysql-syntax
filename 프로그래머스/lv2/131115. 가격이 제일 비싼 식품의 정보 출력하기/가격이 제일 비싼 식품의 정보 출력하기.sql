/*
 * 가격이 제일 비싼 식품의
 * 식품 ID, 식품 이름, 식품 코드, 식품 분류, 식품 가격
*/
SELECT *
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE)
      FROM FOOD_PRODUCT
     )