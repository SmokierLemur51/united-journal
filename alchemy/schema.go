package alchemy

import (
  "github.com/jmoiron/sqlx"
)

func CreateSchema(db *sqlx.DB) {
  schema := `
    CREATE TABLE IF NOT EXISTS checklists (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      deleted_at DATETIME,
      name VARCHAR(120) NOT NULL,
      information TEXT,
      completed BOOLEAN NOT NULL DEFAULT FALSE
    );

     CREATE TABLE IF NOT EXISTS checklist_items (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      deleted_at DATETIME,
      checklist_id INTEGER NOT NULL,
      information TEXT,
      completed BOOLEAN NOT NULL DEFAULT FALSE,
      FOREIGN KEY (checklist_id) REFERENCES checklists(id)
    );
  `
  db.MustExec(schema)
}
