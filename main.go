package main

import (
  "log"
  "net/http"
  "os"
  "github.com/SmokierLemur51/united-journal/handler"
  // "github.com/SmokierLemur51/united-journal/alchemy"
)

func init() {
  os.Setenv("DATABASE", "testing.db")
}

func main() {
  
  router := http.NewServeMux()

  handler := handler.Handler{}
  handler.ConfigureHandler(router)

  // alchemy.CreateSchema(handler.DB) 
  
  server := http.Server{
    Addr: handler.Port,
    Handler: router,
  }
  
  // Static files
  // fs := http.FileServer(http.Dir("./static"))
  // http.Handle("/static/", http.StripPrefix("/static/", fs))
 
  // alchemy.CreateSchema(handler.DB)

  log.Println("Listening on port " + handler.Port)
  log.Fatal(server.ListenAndServe())
}
