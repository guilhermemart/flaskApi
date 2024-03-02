USE FlaskApiDb;

CREATE TABLE products (
    id integer not null auto_increment,
    name varchar(100),
    description tinytext,
    price decimal(10, 2),
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO products (name,  description, price) VALUES ('paper', 'paper A4 for office and printers 100 units', 20.50);
INSERT INTO products (name, description, price) VALUES ('samsung galaxy s8', 'smartphone samsung top line', 2000.35);
INSERT INTO products (name, description, price) VALUES ('samsung j6', 'smartphone samsung entry line', 1000.99);
