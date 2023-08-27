// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use api::FreshAPI;
mod api;

use tauri::{ command, Manager };
use serde_json::Value;


#[command]
fn greet(name: &str) -> String {
  format!("Hello, {name}!")
}

#[command]
fn update_tickets() -> Vec<Value>{
  let mut api_obj : FreshAPI = api::FreshAPI::new();
  let ticket_jsons = api_obj.get_reimage_tickets();
  //api_obj.close_ticket_task(22027, 1410);
  ticket_jsons
}


#[command]
fn close_ticket_task(ticket_id: i32, task_id: i32){
  println!("Closing ticket {} task {}", ticket_id, task_id);
  let mut api_obj : FreshAPI = api::FreshAPI::new();
  api_obj.close_ticket_task(ticket_id, task_id);
  update_tickets();
}

#[command]
fn clean_ticket_update() -> Vec<Value> {
  let mut api_obj : FreshAPI = api::FreshAPI::new();
  let output = api_obj.clean_get_tickets();
  println!("{:#?}", output);
  output
}


fn main() {
  let is_debug: bool = false;
  if is_debug{
    let mut api_obj : FreshAPI = api::FreshAPI::new();
    api_obj.get_reimage_tickets();
    return;
  }
  tauri::Builder::default()
  .setup(|app| {
    let app_handle = app.app_handle();
    tauri::async_runtime::spawn(async move {
      loop {
        tokio::time::sleep(tokio::time::Duration::from_secs(60 * 60)).await;
        app_handle.emit_all("backend-update-tickets", "updatePing").unwrap();
        println!("updatePing");
      }
    });
    Ok(())
  })
  .invoke_handler(tauri::generate_handler![greet, update_tickets, close_ticket_task, clean_ticket_update])
  .run(tauri::generate_context!())
  .expect("error while running tauri application");
}