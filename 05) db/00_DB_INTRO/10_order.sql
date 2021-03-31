-- 나이순으로 오름차순 정렬
SELECT * FROM users
ORDER BY age ASC LIMIT 10;

-- 나이 + 성으로 오름차순 정렬 상위 10개
SELECT * FROM users
ORDER BY age, last_name ASC LIMIT 10;

-- 두개의 결과값이 다름
SELECT * FROM users
ORDER BY last_name, age ASC LIMIT 10;

-- 계좌잔액 내림차순, > 성과 이름 10개(제일 부자 상위 10명의 이름)
SELECT last_name, first_name FROM users
ORDER BY balance DESC LIMIT 10;
