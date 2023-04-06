INSERT INTO articles
VALUES
    ('제목4', '내용4', 4),
    ('제목5', '내용5', 5),
    ('제목6', '내용6', 6),
    ('제목7', '내용7', 7),
    ('제목8', '내용8', 8),
    ('제목9', '내용9', 9),
    ('제목10', '내용10', 10);

INSERT INTO users
VALUES
    ('sophia', 2),
    ('beemo', 1),
    ('feel', 3),
    ('coco', 2);

DELETE FROM articles WHERE title IN (
    '제목4',
    '제목6',
    '제목7',
    '제목8'
);
