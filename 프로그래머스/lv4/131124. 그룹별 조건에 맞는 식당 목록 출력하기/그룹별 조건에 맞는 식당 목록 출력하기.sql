/*
 * 회원 이름, 리뷰 텍스트, 리뷰 작성일
    - 리뷰 가장 많이 작성한 회원"의" 리뷰들
*/
# SELECT MEMBER_ID, MEMBER_NAME
# FROM MEMBER_PROFILE
# WHERE (MEMBER_ID) = ()

# SELECT *
# FROM
# (SELECT MEMBER_ID, MAX(COUNT(*)) AS CNT
# FROM REST_REVIEW
# GROUP BY MEMBER_ID
# ORDER BY CNT DESC) as r LEFT JOIN 
# (SELECT MEMBER_ID, MEMBER_NAME
# FROM MEMBER_PROFILE) as m ON r.MEMBER_ID = m.MEMBER_ID

# HAVING MAX(COUNT(MEMBER_ID))
SELECT p.MEMBER_NAME, v.REVIEW_TEXT, DATE_FORMAT(v.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM REST_REVIEW as v LEFT JOIN MEMBER_PROFILE as p ON v.MEMBER_ID = p.MEMBER_ID
WHERE v.MEMBER_ID IN (SELECT MEMBER_ID
                    FROM REST_REVIEW
                    GROUP BY MEMBER_ID
                    HAVING COUNT(MEMBER_ID) = (
                                SELECT MAX(c.CNT) as MAX_COUNT
                                FROM (
                                    SELECT COUNT(*) AS CNT
                                    FROM REST_REVIEW
                                    GROUP BY MEMBER_ID
                                ) as c
                            )
                    )
ORDER BY v.REVIEW_DATE, v.REVIEW_TEXT


# SELECT MEMBER_ID
# FROM REST_REVIEW