// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

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
  api::request();

  tauri::Builder::default()
    .invoke_handler(tauri::generate_handler![greet])
    .invoke_handler(tauri::generate_handler![update_tickets])
    .run(tauri::generate_context!())
    .expect("error while running tauri application");
}
