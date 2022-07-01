CREATE TABLE IF NOT EXISTS companies (
    id VARCHAR(100) NOT NULL,
    company_name VARCHAR(300) NOT NULL,
    web_site VARCHAR(100),
    source VARCHAR(300),
    PRIMARY KEY (id)
);