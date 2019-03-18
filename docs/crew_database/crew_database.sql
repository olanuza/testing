--
-- Create Database Structure
--
DROP TABLE IF EXISTS crew_members CASCADE;
CREATE TABLE crew_members (
       id char(5) NOT NULL,
       name varchar(50) NOT NULL,
       age int NOT NULL,
       
       PRIMARY KEY (id)
);


DROP TABLE IF EXISTS aircrafts CASCADE;
CREATE TABLE aircrafts (
       id char(5) NOT NULL,
       model varchar(50) NOT NULL,
       
       PRIMARY KEY (id)
);


DROP TABLE IF EXISTS history CASCADE;
CREATE TABLE IF NOT EXISTS history (
       aircraft_id char(5) NOT NULL,
       crew_member_id char(5) NOT NULL,
       experience int DEFAULT 0,
       
       FOREIGN KEY (crew_member_id) REFERENCES crew_members(id) ON DELETE NO ACTION,
       FOREIGN KEY (aircraft_id) REFERENCES aircrafts(id) ON DELETE NO ACTION,
       PRIMARY KEY (aircraft_id, crew_member_id)
);

--
-- Insert sample data
--
INSERT INTO crew_members (id, name, age) VALUES ('AAAAA', 'Guillem Serra', 40);
INSERT INTO crew_members (id, name, age) VALUES ('BBBBB', 'Josep Garcia', 20);
INSERT INTO crew_members (id, name, age) VALUES ('CCCCC', 'Marti Padró', 25);
INSERT INTO crew_members (id, name, age) VALUES ('DDDDD', 'Laia Corominas', 50);
INSERT INTO crew_members (id, name, age) VALUES ('EEEEE', 'Marta Capdevila', 55);


INSERT INTO aircrafts (id, model) VALUES ('11111', 'Model AAA');
INSERT INTO aircrafts (id, model) VALUES ('22222', 'Model AAB');
INSERT INTO aircrafts (id, model) VALUES ('33333', 'Model AAC');


INSERT INTO history (aircraft_id, crew_member_id, experience) VALUES ('11111', 'AAAAA', 3);
INSERT INTO history (aircraft_id, crew_member_id, experience) VALUES ('11111', 'DDDDD', 1);
INSERT INTO history (aircraft_id, crew_member_id, experience) VALUES ('22222', 'AAAAA', 1);
INSERT INTO history (aircraft_id, crew_member_id, experience) VALUES ('22222', 'DDDDD', 4);
INSERT INTO history (aircraft_id, crew_member_id, experience) VALUES ('22222', 'BBBBB', 2);
INSERT INTO history (aircraft_id, crew_member_id, experience) VALUES ('33333', 'AAAAA', 1);
INSERT INTO history (aircraft_id, crew_member_id, experience) VALUES ('33333', 'CCCCC', 1);
INSERT INTO history (aircraft_id, crew_member_id, experience) VALUES ('33333', 'DDDDD', 1);

--
-- Sample Queries
--

-- Find name of the oldest crew member
SELECT * FROM crew_members
WHERE age = (SELECT MAX(age) FROM crew_members);


-- Find name of the n-th crew member (second oldest, fifth oldest and so on)
SELECT * FROM crew_members
WHERE age = (SELECT DISTINCT(age) FROM crew_members
      	     ORDER BY age DESC OFFSET 1 LIMIT 1);


-- Find name of the most experienced crew member - that one who knows most aircrafts
SELECT * FROM crew_members
WHERE id = (SELECT crew_member_id FROM history
      	    GROUP BY crew_member_id ORDER BY COUNT(*) DESC LIMIT 1);


-- Find name of the least experienced crew member - that one who knows least aircrafts (counting from zero)
-- COMMENT: I know this query doesn't include the crew_members who doesn't have any experience (count = 0) but I couldn't find the way to do it
SELECT * FROM crew_members
WHERE id = (SELECT crew_member_id FROM history
      	    GROUP BY crew_member_id ORDER BY COUNT(*) ASC LIMIT 1);




