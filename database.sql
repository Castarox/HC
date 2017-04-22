BEGIN TRANSACTION;
DROP TABLE 'User';
CREATE TABLE `User` (
	`IDX`	INTEGER,
	`Login`	TEXT,
	`Password`	TEXT,
	`Status`	TEXT,
	`Level`	INTEGER,
	PRIMARY KEY(IDX)
);
DROP TABLE 'Moderator';
CREATE TABLE 'Moderator' (
	`IDX`	INTEGER,
	`UserIDX`	INTEGER,
	`LocalizationIDX` INTEGER,
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
	`BeaconIDX`	INTEGER,
	PRIMARY KEY(IDX)
);
DROP TABLE `Beacon`;
CREATE TABLE `Beacon` (
	`IDX`	        INTEGER,
	`BeaconIDX`	    INTEGER,
	PRIMARY KEY(IDX)
);
DROP TABLE `VisitedLocations`;
CREATE TABLE `VisitedLocations` (
	`IDX`	        INTEGER,
	`UserIDX`       INTEGER,
	`LocationIDX`	INTEGER,
    `Visited`	    BOOLEAN,
	PRIMARY KEY(IDX)
);


INSERT INTO `User` (Login, Password, Level) VALUES ('Marcin', 'xxx', 0);
INSERT INTO `Moderator` (UserIDX, LocalizationIDX) VALUES (1, 1);
INSERT INTO `Question` (LocationIDX, Question, Answer1, Answer2, Answer3, CorrectAnswer) VALUES (1, 'where are you now', 'spaceship', 'zoo', 'london', 'codecool');
INSERT INTO `Location` (Name, BeaconIDX) VALUES ('codecool', 1);
INSERT INTO 'Beacon' (BeaconIDX) VALUES (1);
COMMIT;