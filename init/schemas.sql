-- Cria o banco de dados se não existir
CREATE DATABASE IF NOT EXISTS clean_database;

-- Seleciona o banco de dados a ser usado (se necessário no seu contexto)
\c clean_database

-- Cria a tabela se não existir, com a coluna `id` auto-incrementável
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age BIGINT NOT NULL
);