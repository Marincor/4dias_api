CREATE TABLE IF NOT EXISTS companies (
    id SERIAL,
    company_name VARCHAR(300) NOT NULL,
    web_site VARCHAR(100),
    source VARCHAR(300),
    approved BOOLEAN, 
    PRIMARY KEY (id)
);