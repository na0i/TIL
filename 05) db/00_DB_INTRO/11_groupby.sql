-- 각 성씨가 몇명이 있을까?
SELECT last_name, COUNT(*)
FROM users
-- lastname이 같은 사람들만 따로 select 구문 진행
GROUP by last_name; 

-- SELECT DISTINCT last_name FROM users;


SELECT last_name, first_name
FROM users
GROUP by last_name, first_name;