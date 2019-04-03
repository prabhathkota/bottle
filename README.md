# Bottle/SQLite/Paste server - testing bottle framework

# How to run this ?
python test.py

# How to Test ?
http://localhost:8080/hello

http://localhost:8080/login

http://localhost:8080/show/1

http://localhost:8080/show/2

# setup SQLite
sqlite3
sqlite3 test.db

CREATE TABLE comments ( 
	post_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
	name TEXT NOT NULL, 
	email TEXT NOT NULL, 
	website_url TEXT NULL, 
	comment TEXT NOT NULL );


INSERT INTO comments ( name, email, website_url, comment )
VALUES ( 'Shivam Mamgain', 'xyz@gmail.com',
'shivammg.blogspot.com', 'Great tutorial for beginners.' );

INSERT INTO comments ( name, email, website_url, comment )
VALUES ( 'Prabhath Kota', 'prabhath@gmail.com',
'prabhath.blogspot.com', 'Great tutorial from Prabhath.' );

SELECT post_id, name, email, website_url, comment FROM comments;


SELECT * FROM comments;

.quit
