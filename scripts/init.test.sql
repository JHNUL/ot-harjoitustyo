DROP TABLE IF EXISTS Players;
DROP TABLE IF EXISTS Scores;

CREATE TABLE Players (
  id INTEGER PRIMARY KEY,
  playername VARCHAR(30) NOT NULL UNIQUE,
  last_login REAL
);

CREATE TABLE Scores (
  id INTEGER PRIMARY KEY,
  player_id INTEGER NOT NULL,
  score_timestamp REAL NOT NULL,
  score INTEGER NOT NULL,
  FOREIGN KEY (player_id) REFERENCES Players (id)
);
