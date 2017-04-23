BEGIN TRANSACTION;
DROP TABLE `User`;
CREATE TABLE `User` (
	`IDX`	INTEGER,
	`Login`	TEXT,
	`Password`	TEXT,
	`Points`	INTEGER,
	`Level`	INTEGER,
	PRIMARY KEY(IDX)
);
DROP TABLE `Moderator`;
CREATE TABLE `Moderator` (
	`IDX`	INTEGER,
	`Login`	INTEGER,
	`Password` INTEGER,
	PRIMARY KEY(IDX)
);
DROP TABLE `Question`;
CREATE TABLE `Question` (
	`IDX`	INTEGER,
	`LocationIDX`	INTEGER,
	`Question`	TEXT,
	`Answer1`	TEXT,
	`Answer2`	TEXT,
	`Answer3`	TEXT,
	`CorrectAnswer`	TEXT,
	PRIMARY KEY(IDX)
);
DROP TABLE `Location`;
CREATE TABLE `Location` (
	`IDX`	INTEGER,
	`Name`	TEXT,
	`BeaconMajor`	INTEGER,
	`ModeratorIDX`	INTEGER,
	`Latitude`	INTEGER,
	`Longitude`	INTEGER,

	PRIMARY KEY(IDX)
);
DROP TABLE `VisitedLocations`;
CREATE TABLE `VisitedLocations` (
	`IDX`	        INTEGER,
	`UserIDX`       INTEGER,
	`LocationIDX`	INTEGER,
    `Visited`	    TEXT,
	PRIMARY KEY(IDX)
);


INSERT INTO `User` (Login, Password, Level) VALUES ('Marcin', 'xxx', 0);
INSERT INTO `Moderator` (IDX, Login, Password) VALUES (1, 'Marcin', 'xxx');
INSERT INTO `Question` (LocationIDX, Question, Answer1, Answer2, Answer3, CorrectAnswer) VALUES (1, 'where are you now', 'spaceship', 'zoo', 'london', 'codecool');
INSERT INTO `Location` (Name, BeaconMajor, ModeratorIDX, Latitude, Longitude) VALUES ('codecool', 1, 1, 66, 66);
INSERT INTO `VisitedLocations` (UserIDX, LocationIDX, Visited) VALUES (1, 1, 'False');
COMMIT;