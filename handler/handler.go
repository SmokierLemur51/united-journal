package handler

import (
  "log"
  "net/http"
  "os"
  "github.com/jmoiron/sqlx"
  _ "github.com/mattn/go-sqlite3"
)

var (
  css = "/static/css/testing.css"
)

type Handler struct {
  Port string
  DB *sqlx.DB
}


func (h *Handler) ConfigureHandler(router *http.ServeMux) {
  var e error
  h.DB, e = sqlx.Connect("sqlite3", "instance/" + os.Getenv("DATABASE"))
  if e != nil {
    log.Fatal(e)
  }
  h.Port = ":5000"
  h.Routes(router)
}


func (h *Handler) Routes(router *http.ServeMux) {
  // Static
  fs := http.FileServer(http.Dir("./static"))
  router.Handle("/static/", http.StripPrefix("/static/", fs))

  router.HandleFunc("GET /", h.IndexHandler)
  router.HandleFunc("GET /checklists", h.ViewChecklists)
}


// entry point for the web application
func (h *Handler) IndexHandler(w http.ResponseWriter, r *http.Request) {
  html := HtmlTemplate{File: "index.html", Title: "Welcome"}
  html.RenderHtml(w)
}



func (h *Handler) ViewChecklists(w http.ResponseWriter, r *http.Request) {
  html := HtmlTemplate{
    Dir: "checklist", 
    File: "checklists.html", 
    CSS: css,
    Title: "Checklists",
  }
  html.RenderHtml(w)
}

