-- -- users에서 age 30 이상
SELECT * FROM users
WHERE age >= 30;

-- -- users에서 age 30 이상인 사람의 이름만
SELECT first_name FROM users
WHERE age >= 30;

-- users > 성 = 김, 나이 >= 30인 사람의 성과 나이만
SELECT age, last_name FROM users
WHERE last_name = '김'AND age >= 30;

