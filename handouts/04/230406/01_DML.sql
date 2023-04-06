-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT COUNT(*) FROM users;
SELECT AVG(balance) FROM users;
SELECT country, AVG(balance) FROM users GROUP BY country;
SELECT country, AVG(balance) FROM users GROUP BY country ORDER BY AVG(balance);
SELECT AVG(age) FROM users WHERE age>=30;

SELECT country, COUNT(country) FROM users GROUP BY country;
--그룹화된 country를 기준으로 카운트하는 것이기 때문에 어떤 컬럼을 카운트해도 전체 개수는 동일.

SELECT last_name, COUNT(*) AS number_of_name FROM users 
GROUP BY last_name;
-- AS 키워드는 원본테이블이 변경되는 것이 아닌, 조회하는 테이블의 이름을 바꾸어줌.

CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates (name, age, address) 
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES 
('김철수',30,'경기'),
('이영미', 31, '강원'),
('박진성', 26, '전라'),
('최지수', 12, '충청'),
('정요한', 28, '경상');

UPDATE classmates
SET name='김철수한무두루미',
    address='제주도'
WHERE rowid=2;

DELETE FROM classmates WHERE name='최지수';
DELETE FROM classmates WHERE name LIKE '%영%';

DELETE FROM classmates;
