/*
 * 상품을 구매한 회원수, 상품을 구매한 회원의 
    - 2021년 가입 전체 회원 대상
    - 비율 : 2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수
        - 소수점 첫째자리까지 반올림
    - 년, 월별
    - 년 - 월 오름차
    
*/
# SELECT COUNT(*) as JOINED_USER_COUNT
# FROM USER_INFO
# WHERE YEAR(JOINED) = '2021' 

SELECT YEAR(SALES_DATE) AS YEAR, 
       MONTH(SALES_DATE) AS MONTH, 
       COUNT(DISTINCT USER_ID) AS PUCHASED_USERS,
       ROUND(
          COUNT(DISTINCT USER_ID) / 
          (SELECT COUNT(*) as JOINED_USER_COUNT
          FROM USER_INFO
          WHERE YEAR(JOINED) = '2021')
          , 1
       ) AS PUCHASED_RATIO
FROM ONLINE_SALE
WHERE USER_ID IN (SELECT USER_ID
                    FROM USER_INFO
                    WHERE YEAR(JOINED) = '2021' )
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE)
ORDER BY  YEAR, MONTH
