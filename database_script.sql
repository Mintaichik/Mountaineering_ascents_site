CREATE TABLE climbing (
	id integer PRIMARY KEY autoincrement,
	mountain varchar(255) NOT NULL,
	difficulty_of_climbing integer NOT NULL,
	country varchar(255) NOT NULL,
	guide varchar(255) NOT NULL,
	guide_qualification integer NOT NULL,
)