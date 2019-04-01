# Bottle/SQLite/Paste server - testing bottle framework

# How to run
python test.py

# How to Test
http://localhost:8080/hello

http://localhost:8080/login

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


SELECT post_id, name, email, website_url, comment FROM comments;


SELECT * FROM comments;

.quit
