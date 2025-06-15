CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password TEXT NOT NULL
);

INSERT IGNORE INTO users (username, password)
VALUES ('user1', SHA2('password123', 256));
