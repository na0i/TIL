-- 전체 조회
SELECT * FROM classmates;

-- 컬럼 지정 조회하기
SELECT name, address FROM classmates;

-- 개수 제한(지정)
-- OFFSET 뒤부터 LIMIT 개
SELECT id, name FROM classmates LIMIT 2 OFFSET 2;