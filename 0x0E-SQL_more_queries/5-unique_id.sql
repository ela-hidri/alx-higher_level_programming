-- creates the table unique_id on your MySQ
CREATE TABLE IF NOT EXISTS unique_id(
id int UNIQUE DEFAULT 1,
name VARCHAR(256)
)
