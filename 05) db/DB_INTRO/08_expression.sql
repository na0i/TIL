-- users 레코드의 개수
SELECT COUNT(*) FROM users;

-- 30살 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users
WHERE age >= 30;

-- 계좌 잔액이 가장 높은 사람의 액수와 이름
SELECT country, first_name, MAX(balance) FROM users;

-- -- 이렇게 하면 제일 부자의 전체데이터랑 금액 둘다 나옴
-- SELECT *, MAX(balance) FROM users;

-- -- 이렇게 써버리면 합계, 1번째 사람의 first name 등장
-- SELECT SUM(balance), first_name FROM users;

-- 평균, 개수, 총합
SELECT AVG(balance), COUNT(*), SUM(balance) FROM users;