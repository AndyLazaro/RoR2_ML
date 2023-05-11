CREATE TABLE RunData(
	runID INTEGER PRIMARY KEY AUTOINCREMENT,
	GameMode VARCHAR NOT NULL,
	GameEnding VARCHAR NOT NULL,
	TimeAlive FLOAT NOT NULL,
	Difficulty VARCHAR NOT NULL,
	Survivor VARCHAR NOT NULL,
	TotalKills INT NOT NULL,
	TotalDamageDealt INT NOT NULL,
	TotalDamageTaken INT NOT NULL,
	HighestDamageDealt INT NOT NULL,
	TotalGoldCollected INT NOT NULL,
	TotalItemsCollected INT NOT NULL,
	TotalPurchases INT NOT NULL,
	Equipment VARCHAR
);

CREATE TABLE ItemData(
	runID INT,
	
	FOREIGN KEY (runID) REFERENCES RunData(runID)
);

INSERT INTO RunData(GameMode, GameEnding, TimeAlive, Difficulty, Survivor, TotalKills, TotalDamageDealt, TotalDamageTaken, HighestDamageDealt, 
			TotalGoldCollected, TotalItemsCollected, TotalPurchases, Equipment) 
			VALUES ('ClassicRun', 'StandardLoss', '436.3875', 'Hard', 'MageBody', '104', '22884', '634', '384', '492', '7', '8', '');
			