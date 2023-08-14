// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use api::FreshAPI;
mod api;

#[tauri::command]
fn greet(name: &str) -> String {
  format!("Hello, {name}!")
}

#[tauri::command]
fn update_tickets() -> Vec<serde_json::Value>{
  let mut api_obj : FreshAPI = api::FreshAPI::new();
  let ticket_jsons = api_obj.get_reimage_tickets();
  println!("{:#?}", ticket_jsons);
  ticket_jsons
}


fn main() {
  let is_debug: bool = false;
  let mut api_obj : FreshAPI = api::FreshAPI::new();
  if is_debug{
    //let ticket_json = api_obj.get_ticket(21816);
    //println!("{:#?}", ticket_json);
    api_obj.get_reimage_tickets();
    return;
  }
  
  tauri::Builder::default()
  .invoke_handler(tauri::generate_handler![greet])
  .invoke_handler(tauri::generate_handler![update_tickets])
  .run(tauri::generate_context!())
  .expect("error while running tauri application");
}