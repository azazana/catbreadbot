CREATE SCHEMA IF NOT EXISTS telegrambot;

# CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS telegrambot.history (
    id uuid PRIMARY KEY,
    id_user INT NOT NULL,
    message TEXT,
    created timestamp with time zone
);

CREATE TABLE IF NOT EXISTS telegrambot.level (
    id uuid PRIMARY KEY,
    id_user INT NOT NULL,
    level int,
    created timestamp with time zone
);
