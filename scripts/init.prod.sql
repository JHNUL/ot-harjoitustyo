CREATE TABLE IF NOT EXISTS Players (
  id INTEGER PRIMARY KEY,
  playername VARCHAR(30) NOT NULL,
  last_login REAL
);

CREATE TABLE IF NOT EXISTS Scores (
  id INTEGER PRIMARY KEY,
  player_id INTEGER NOT NULL,
  score_timestamp REAL NOT NULL,
  score INTEGER NOT NULL,
  FOREIGN KEY (player_id) REFERENCES Players (id)
);
