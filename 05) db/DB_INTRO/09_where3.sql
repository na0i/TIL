-- 값의 비교가 아닌 패턴의 비교(LIKE)


-- 20대 찾기
SELECT * FROM users
-- WHERE age >= 20 and age < 30;
WHERE age LIKE '2_';

-- 지역번호 02 찾기
SELECT phone FROM users
WHERE phone LIKE '02-%';

-- 박씨이면서 준으로 끝나는 사람의 이름
SELECT last_name, first_name FROM users
WHERE first_name LIKE '%준' and last_name LIKE '박';

-- 번호 중간번호가 5114인 사람만
SELECT phone FROM users
WHERE phone LIKE '%-5114-%';