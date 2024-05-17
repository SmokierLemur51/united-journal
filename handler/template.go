package handler

import (
  "fmt"
  "html/template"
  "net/http"
)



// turn into interface
type HtmlTemplate struct {
  // Dir is needed if file not in root templates directory
  Dir   string
  File  string
  CSS   string
  // html title element
  Title string
  Content map[string]interface{}
}

func (t *HtmlTemplate) RenderHtml(w http.ResponseWriter) error {
  if t.Dir != "" {
    tmpl, err := template.ParseFiles(fmt.Sprintf("templates/%s/%s", t.Dir, t.File)) 
    if err != nil {
      return err
    }
    err = tmpl.Execute(w, t)
    if err != nil { 
      return err
    }
    w.Header().Set("Content-Type", "text/html; charset=utf-8")
    return nil
  }
  // Base dir
  tmpl, err := template.ParseFiles("templates/" + t.File) 
  if err != nil {
    return err
  }
  err = tmpl.Execute(w, t)
  if err != nil { 
    return err
  }
  w.Header().Set("Content-Type", "text/html; charset=utf-8")
  return nil
}
