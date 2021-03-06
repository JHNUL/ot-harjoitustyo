CREATE TABLE IF NOT EXISTS Players (
  id INTEGER PRIMARY KEY,
  name VARCHAR(30) NOT NULL UNIQUE,
  last_login REAL
);

CREATE TABLE IF NOT EXISTS Scores (
  id INTEGER PRIMARY KEY,
  player_id INTEGER NOT NULL,
  timestamp REAL NOT NULL,
  value INTEGER NOT NULL,
  FOREIGN KEY (player_id) REFERENCES Players (id)
);
