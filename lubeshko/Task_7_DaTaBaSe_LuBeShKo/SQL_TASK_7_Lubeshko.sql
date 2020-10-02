BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Product" (
	"product_id"	INTEGER,
	"product_name"	VARCHAR(50) NOT NULL,
	"product_dtl"	TEXT NOT NULL,
	PRIMARY KEY("product_id")
);
CREATE TABLE IF NOT EXISTS "Customer" (
	"customer_id"	INTEGER,
	"name"	TEXT NOT NULL,
	"address"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	PRIMARY KEY("customer_id")
);
CREATE TABLE IF NOT EXISTS "Sales" (
	"sales_id"	INTEGER,
	"customer_id"	INTEGER,
	"date_of_sale"	date,
	"product_id"	INTEGER,
	FOREIGN KEY("customer_id") REFERENCES "Customer",
	FOREIGN KEY("product_id") REFERENCES "Product",
	PRIMARY KEY("sales_id" AUTOINCREMENT)
);
INSERT INTO "Product" ("product_id","product_name","product_dtl") VALUES (1,'Samsung note 20','phones'),
 (2,'Apple macbook pro','сomputers'),
 (3,'Bmw x7','cars'),
 (4,'Audi Q8','cars'),
 (5,'Apple iphone 12','phones'),
 (6,'Sony vaio','сomputers');
INSERT INTO "Customer" ("customer_id","name","address","email") VALUES (1,'Markov Averky','463 Marcelle Crescent','musellerress-2412@yopmail.com'),
 (2,'Grishin Willie','55 Lang Highway','kiddefypparro-0295@yopmail.com'),
 (3,'Konovalov Yulian','37 Justus Rise','asillucuna-8247@yopmail.com'),
 (4,'Aksyonov May','26 Arely Close','zoteronnob-6515@yopmail.com'),
 (5,'Kostin Kim','62 Hansen Road','memysoppe-2863@yopmail.com');
INSERT INTO "Sales" ("sales_id","customer_id","date_of_sale","product_id") VALUES (2,1,'12-12-2020',1),
 (3,2,'13-01-2020',3),
 (4,3,'14-02-2020',2),
 (5,4,'15-03-2020',6),
 (6,5,'16-04-2020',5);
COMMIT;
