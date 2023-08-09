// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use api::FreshAPI;
mod api;


#[tauri::command]
fn greet(name: &str) -> String {
  return format!("Hello, {name}!");
}

#[tauri::command]
fn update_tickets(){
  println!("Updating tickets...");
}


fn main() {
  let is_debug: bool = true;
  if is_debug{
    let mut api_obj : FreshAPI = api::FreshAPI::new();
    //let ticket_json = api_obj.get_ticket(21816);
    api_obj.get_reimage_ticket_ids("status:2%20AND%20tag:\'Reimage\'");
    return;
  }
  
  tauri::Builder::default()
  .invoke_handler(tauri::generate_handler![greet])
  .invoke_handler(tauri::generate_handler![update_tickets])
  .run(tauri::generate_context!())
  .expect("error while running tauri application");
}