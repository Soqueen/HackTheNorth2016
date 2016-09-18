\echo 'DROPPING OLD TABLES...'
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS guests;
\echo

CREATE TABLE guests (
	id 			 BIGSERIAL		PRIMARY KEY,
	email        TEXT			NOT NULL,
	attending	 BOOLEAN		
);
\echo

CREATE TABLE events (
	id			 BIGSERIAL		PRIMARY KEY,
	guests_id    BIGSERIAL      REFERENCES guests(id),
	event_name	 TEXT           NOT NULL,
	location	 TEXT			NOT NULL,
	time		 TIMESTAMP		NOT NULL,
	description  TEXT			,
	host_name	 TEXT			NOT NULL,
	email		 TEXT			NOT NULL,
	url          TEXT			NOT NULL
);
\echo

