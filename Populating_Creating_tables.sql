CREATE TABLE [User] (
	[User_ID] int IDENTITY(1,1) NOT NULL UNIQUE,
	[User_Name] nvarchar(max) NOT NULL,
	[USer_Email] nvarchar(max) NOT NULL,
	[Password] nvarchar(max) NOT NULL,
	[Date_Of_Creation] datetime NOT NULL,
	PRIMARY KEY ([User_ID])
);

CREATE TABLE [Admin] (
	[Admin_ID] int IDENTITY(1,1) NOT NULL UNIQUE,
	[Admin_Name] nvarchar(max) NOT NULL,
	[Admin_Email] nvarchar(max) NOT NULL,
	[Password] nvarchar(max) NOT NULL,
	[Date_Of_Creation] datetime NOT NULL,
	PRIMARY KEY ([Admin_ID])
);

CREATE TABLE [Movie] (
	[Movie_ID] int IDENTITY(1,1) NOT NULL UNIQUE,
	[Movie_Name] nvarchar(max) NOT NULL,
	[Summary] nvarchar(max) NOT NULL,
	[Year] int NOT NULL,
	[Admin_ID] int NOT NULL,
	PRIMARY KEY ([Movie_ID])
);

CREATE TABLE [Review] (
	[Review_ID] int IDENTITY(1,1) NOT NULL UNIQUE,
	[Rating] int NOT NULL,
	[Review_Description] nvarchar(max) NOT NULL,
	[Num_Of_Likes] int NOT NULL,
	[Date] datetime NOT NULL,
	[User_ID] int NOT NULL,
	[Movie_ID] int NOT NULL,
	PRIMARY KEY ([Review_ID])
);

CREATE TABLE [User_Movie] (
	[User_ID] int IDENTITY(1,1) NOT NULL UNIQUE,
	[Movie_ID] int NOT NULL,
	[Watchlist] bit NOT NULL,
	[Favourite] bit NOT NULL,
	[Status] bit NOT NULL,
	PRIMARY KEY ([User_ID], [Movie_ID])
);

CREATE TABLE [Crew] (
    [Movie_ID] int IDENTITY(1,1) NOT NULL,
    [Cast] nvarchar(255) NOT NULL,
    PRIMARY KEY ([Movie_ID], [Cast])
);

CREATE TABLE [Genre] (
    [Movie_ID] int IDENTITY(1,1) NOT NULL,
    [Genre] nvarchar(255) NOT NULL,
    PRIMARY KEY ([Movie_ID], [Genre])
);


ALTER TABLE Movie
ADD Duration nvarchar(255) NOT NULL DEFAULT 0;

ALTER TABLE [Movie] ADD CONSTRAINT [Movie_fk4] FOREIGN KEY ([Admin_ID]) REFERENCES [Admin]([Admin_ID]);
ALTER TABLE [Review] ADD CONSTRAINT [Review_fk5] FOREIGN KEY ([User_ID]) REFERENCES [User]([User_ID]);

ALTER TABLE [Review] ADD CONSTRAINT [Review_fk6] FOREIGN KEY ([Movie_ID]) REFERENCES [Movie]([Movie_ID]);
ALTER TABLE [User_Movie] ADD CONSTRAINT [User_Movie_fk0] FOREIGN KEY ([User_ID]) REFERENCES [User]([User_ID]);

ALTER TABLE [User_Movie] ADD CONSTRAINT [User_Movie_fk1] FOREIGN KEY ([Movie_ID]) REFERENCES [Movie]([Movie_ID]);
ALTER TABLE [Crew] ADD CONSTRAINT [Crew_fk0] FOREIGN KEY ([Movie_ID]) REFERENCES [Movie]([Movie_ID]);
ALTER TABLE [Genre] ADD CONSTRAINT [Genre_fk0] FOREIGN KEY ([Movie_ID]) REFERENCES [Movie]([Movie_ID]);


begin transaction

-- Populate the Admin table with specific IDs if they don't already exist
SET IDENTITY_INSERT [Admin] ON;
INSERT INTO [Admin] ([Admin_ID], [Admin_Name], [Admin_Email], [Password], [Date_Of_Creation]) VALUES
(1, 'Admin1', 'admin1@example.com', 'adminpass1', DATEADD(DAY, -ABS(CHECKSUM(NEWID()) % 1825), GETDATE())),
(2, 'Admin2', 'admin2@example.com', 'adminpass2', DATEADD(DAY, -ABS(CHECKSUM(NEWID()) % 1825), GETDATE()));
SET IDENTITY_INSERT [Admin] OFF;

SET IDENTITY_INSERT [User] ON;
INSERT INTO [User] ([User_ID], [User_Name], [User_Email], [Password], [Date_Of_Creation]) VALUES
(1, 'Sadiqah', 'Sadiqah@example.com', 'password7', DATEADD(DAY, -ABS(CHECKSUM(NEWID()) % 1825), GETDATE())),
(2, 'Lyeba', 'Lyeba@example.com', 'password8', DATEADD(DAY, -ABS(CHECKSUM(NEWID()) % 1825), GETDATE())),
(3, 'Asghar', 'Asghar@example.com', 'password9', DATEADD(DAY, -ABS(CHECKSUM(NEWID()) % 1825), GETDATE()));
SET IDENTITY_INSERT [User] OFF;


-- Populating the Movie table with existing Admin_IDs
SET IDENTITY_INSERT [Movie] ON;
INSERT INTO [Movie] ([Movie_ID], [Movie_Name], [Summary], [Year], [Admin_ID]) VALUES
(1, 'Inception', 'A mind-bending thriller about dreams within dreams.', 2010, 1),
(2, 'The Matrix', 'A computer hacker learns about the true nature of his reality.', 1999, 1),
(3, 'Interstellar', 'A team of explorers travel through a wormhole in space.', 2014, 2);
SET IDENTITY_INSERT [Movie] OFF;

-- Populating the Review table with existing User_IDs and Movie_IDs
INSERT INTO [Review] ([Rating], [Review_Description], [Num_Of_Likes], [Date], [User_ID], [Movie_ID]) VALUES
(5, 'Incredible movie with stunning visuals!', 15, GETDATE(), 1, 2),
(4, 'A classic with groundbreaking concepts.', 20, GETDATE(), 2, 3),
(5, 'A beautiful story about space exploration.', 10, GETDATE(), 3, 1);



--begin transaction 
SET IDENTITY_INSERT [User_Movie] ON;
-- Populating the User_Movie table with existing User_IDs and Movie_IDs
INSERT INTO [User_Movie] ([User_ID], [Movie_ID], [Watchlist], [Favourite], [Status]) VALUES
(1, 2, 1, 1, 1),
(2, 3, 1, 0, 1),
(3, 1, 1, 1, 0);
SET IDENTITY_INSERT [User_Movie] OFF;


--begin transaction
SET IDENTITY_INSERT [Crew] ON;
-- Populating the Crew table with existing Movie_IDs
INSERT INTO [Crew] ([Movie_ID], [Cast]) VALUES
(2, 'Leonardo DiCaprio'),
(2, 'Joseph Gordon-Levitt'),
(3, 'Keanu Reeves'),
(3, 'Laurence Fishburne'),
(1, 'Matthew McConaughey'),
(1, 'Anne Hathaway');
SET IDENTITY_INSERT [Crew] OFF;

-- Turn ON IDENTITY_INSERT for Genre table if necessary
SET IDENTITY_INSERT [Genre] ON;

SET IDENTITY_INSERT [Genre] ON;
INSERT INTO [Genre] ([Movie_ID], [Genre]) VALUES
(2, 'Action'),
(2, 'Sci-Fi'),
(3, 'Action'),
(3, 'Sci-Fi'),
(1, 'Adventure'),
(1, 'Sci-Fi');
SET IDENTITY_INSERT [Genre] OFF;


--ALTER TABLE [Crew]
--DROP CONSTRAINT Crew_fk0;  -- adjust constraint name as needed

--ALTER TABLE [Crew]
--ADD PRIMARY KEY ([Movie_ID], [Cast]);

UPDATE Movie
SET Duration = '2 hours 28 minutes'
WHERE Movie_Name = 'Inception';

UPDATE Movie
SET Duration = '2 hours 16 minutes'
WHERE Movie_Name = 'The Matrix';

UPDATE Movie
SET Duration = '2 hours 49 minutes'
WHERE Movie_Name = 'Interstellar';


Commit;



select * from Admin
select * from [User]
select * from Review
select * from Movie
select * from User_Movie
select * from Crew
select * from Genre