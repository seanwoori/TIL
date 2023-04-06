CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK; -- 이 시점에 삭제된 데이터가 되돌려짐
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT; -- omnivore 인 데이터만 삭제가 적용됨

SELECT COUNT(*)
FROM zoo;