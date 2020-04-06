-- DATABASE CREATION QUERIES
-- Goal Table
CREATE TABLE Goal (
   ID INT PRIMARY KEY,
   [Subject] VARCHAR(50),
   [Description] VARCHAR(150)
);

-- Section Table
CREATE TABLE Section (
   ID INT PRIMARY KEY,
   [Description] VARCHAR(150),
   Goal_ID INT,
   FOREIGN KEY (Goal_ID) REFERENCES Goal(ID)
);

-- Step Table
CREATE TABLE Step (
   ID INT PRIMARY KEY,
   [Description] VARCHAR(150),
   [Day] DATE,
   Section_ID INT,
   Done BIT,
   FOREIGN KEY (Section_ID) REFERENCES Section(ID)
);