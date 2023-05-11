# RoR2_ML
This project is using a machine learning algorithm to predict whether a Risk of Rain 2 run will win based on the current items, gold, time, and much more

Features used in model:
	GameMode - The current game moode the user is playing (Categorical)
    EX:  Simulacrum, Classic, Daily Run
    
	GameEnding - The ending the player has recieved (Categorical)
    Notes: there are multiple endings in the game code so I decided to wrap them together into the numericals 0 and 1 for win or loss (losing is counted as a type of ending)
    
	TimeAlive - The amount of time the game has played. We are able to take time alive as the total game time as if you die in the game you lose the run (Numerical)
  
	Difficulty - The difficulty the player is playing (Categorical)
    There are 4 difficulties included: Drizzle, Rainstorm, Monsoon, and Eclipse
	
  Survivor - The character the player chose to play (Categorical)
    There are 13 characters in game with no plans to add more
    
	TotalKills - Amount of enemies killed (Numerical)
	
  TotalDamageDealt - Total damage dealt in the run (Numerical)
  
	TotalDamageTaken - Total damage taken in the run (Numerical)
  
	HighestDamageDealt - The highest instance of damage dealt to a single enemy (Numerical)
  
	TotalGoldCollected - Total gold collected in the run (Numerical)
  
	TotalItemsCollected - Number of items collected in a run (Numerical)
  
	TotalPurchases - Number of total purchases made in a run (Numerical)
  
	Equipment - The active equipment item a player is carrying (Categorical)
  
  Items: A player can carry any number of items in the game, we decided to use over 100 items as features as well in a bag of words style matrix, each instance of an item a player carries adds to the total carried
  
Database used: RoR_Data.db
  This is the database used for the machine learning model which takes the above features listed and uses data crowdsoruced from various online chat rooms. The data is parsed from XML files using the file Data_Parsing.py.
  I was able to get around 450 entries for the model and it has worked well.
  
 SQLTableCode: File that has the SQL code that creates the database
 
 RoR2_ML_Model: 
  This is the machine learning code used which uses a K-Nearest Neighbors model to predict whether or not a player has won a run based off of all the features listed above. I was able to get around a 89% Accuracy for the model used and will be creating a model from scratch soon
  
Data_Parsing:
  Takes the xml files and parses them into the features needed and adds them to the database, there is an index.txt file which will track the number of files entered into the database and insert them accordingly in the correct location. 
