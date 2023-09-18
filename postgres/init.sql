CREATE TABLE IF NOT EXISTS movies (
    id BIGINT PRIMARY KEY,
    title TEXT NOT NULL,
    year INT NOT NULL,
    rating REAL NOT NULL,
    votes INT NOT NULL,
    runtime INT NOT NULL,
    genres TEXT NOT NULL
);
