package alchemy

import (
	"database/sql"
	"time"
  "github.com/jmoiron/sqlx"
)


type Checklist struct {
    ID int64 `db:"id"`
    CreatedAt time.Time `db:"created_at"`
    UpdatedAt time.Time `db:"updated_at"`
    DeletedAt sql.NullTime `db:"deleted_at"`
    Completed bool `db:"completed"`
    Name string `db:"name"`
    Information string `db:"information"`
    Items []ChecklistItem
}

type ChecklistItem struct {
    ID int64 `db:"id"`
    CreatedAt time.Time `db:"created_at"`
    UpdatedAt time.Time `db:"updated_at"`
    DeletedAt sql.NullTime `db:"deleted_at"`
    ChecklistID int `db:"checklist_id"`
    Checklist Checklist
    Completed bool `db:"completed"`
    Name string `db:"name"`
    Information string `db:"information"`
}

// Create
func CreateChecklist(db *sqlx.DB, name, info string) (Checklist, error) {
  result, err := db.Exec("INSERT INTO checklists (name, information) VALUES (?, ?)", name, info)
  if err != nil {
    return Checklist{}, err
  }
  id, err := result.LastInsertId()
  return Checklist{ID: id, Name: name, Information: info}, nil  
}

// For batch adding checklists 
func PopulateChecklists(db *sqlx.DB, checklists ...Checklist) {
  tx := db.MustBegin()
  for _, c := range checklists {
    tx.Exec("INSERT INTO checklists (name, information) VALUES (?, ?)", c.Name, c.Information)
  }
  tx.Commit()
}



