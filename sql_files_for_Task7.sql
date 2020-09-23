CREATE TABLE Customer(
customer_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
name TEXT NOT NULL,
address TEXT NOT NULL,
email TEXT NOT NULL UNIQUE
);

CREATE TABLE Product(
product_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
product_name TEXT NOT NULL,
product_dtl TEXT NOT NULL
);

CREATE TABLE Sales(
sales_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
product_id INTEGER NOT NULL,
customer_id INTEGER NOT NULL,
date_of_sale TEXT NOT NULL,
FOREIGN KEY(customer_id)
REFERENCES Customer(customer_id)
FOREIGN KEY (product_id)
REFERENCES Product (product_id)
);

INSERT INTO Customer (name, address, email)
VALUES ("Allegra William", "5489 Las Virgenes Rd Calabasas, California(CA), 91302", "Allegra@gmail.com")
INSERT INTO Customer (name, address, email)
VALUES ("Bella-Rose Bob", "549 Daroca Ave San Gabriel, California(CA), 91775", "Bella@gmail.com")
INSERT INTO Customer (name, address, email)
VALUES ("Jordan-Lee Mcmillan", "5549 Derby Ln Paso Robles, California(CA), 93446", "Jordan@gmail.com")
INSERT INTO Customer (name, address, email)
VALUES ("Nina Plummer", "549 Prospect St San Carlos, California(CA), 94070", "Nina@gmail.com")
INSERT INTO Customer (name, address, email)
VALUES ("Kacper Hatfield", "549 Rancho Del Cerro Fallbrook, California(CA), 92028", "Kacper@gmail.com")
INSERT INTO Customer (name, address, email)
VALUES ("Muhammad Archer", "5491 Burlingame Ave Buena Park, California(CA), 90621", "Muhammad@gmail.com")
INSERT INTO Customer (name, address, email)
VALUES ("Avni Beaumont", "54999 Martinez Trl #56 Yucca Valley, California(CA), 92284", "Avni@gmail.com")


INSERT INTO Product (product_name, product_dtl)
VALUES ("Amstel 0.45L CAN","Beer")
INSERT INTO Product (product_name, product_dtl)
VALUES ("Staropramen 0.45L GB","Beer")
INSERT INTO Product (product_name, product_dtl)
VALUES ("Zlaty Bazant Cerne 0.9L PET","Beer")
INSERT INTO Product (product_name, product_dtl)
VALUES ("Villa Dini 1L Pinapple", "Juice")
INSERT INTO Product (product_name, product_dtl)
VALUES ("Hatni Sprauny 1.4L PET", "Kvass")
INSERT INTO Product (product_name, product_dtl)
VALUES ("Rechitskoe Svetloe 1.4L PET", "Beer")
INSERT INTO Product (product_name, product_dtl)
VALUES ("Bambolina 0.09L Apple", "Baby food")
INSERT INTO Product (product_name, product_dtl)
VALUES ("Heineken 0.47L GB", "Beer")

INSERT INTO Sales (product_id, customer_id, date_of_sale)
VALUES ("1","3","17.08.20")
INSERT INTO Sales (product_id, customer_id, date_of_sale)
VALUES ("1","7","01.08.20")
INSERT INTO Sales (product_id, customer_id, date_of_sale)
VALUES ("5","3","22.08.20")
INSERT INTO Sales (product_id, customer_id, date_of_sale)
VALUES ("2","6","09.08.20")
INSERT INTO Sales (product_id, customer_id, date_of_sale)
VALUES ("6","4","31.08.20")
INSERT INTO Sales (product_id, customer_id, date_of_sale)
VALUES ("3","3","15.08.20")
INSERT INTO Sales (product_id, customer_id, date_of_sale)
VALUES ("4","6","15.08.20")
INSERT INTO Sales (product_id, customer_id, date_of_sale)
VALUES ("1","2","18.08.20")




