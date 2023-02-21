/*
 * 조회 = 환자이름, 환자번호, 성별코드, 나이, 전화번호
 - 12세 이하
 - 여자환자
 - 전화번호가 없는 경우, 'NONE'
 - 내림차순 = 나이 & 오름차 = 이름
*/
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE')
FROM PATIENT
WHERE GEND_CD = 'W' AND AGE <= 12
ORDER BY AGE DESC , PT_NAME ASC