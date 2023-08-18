// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use api::FreshAPI;
mod api;

use tauri::{ command, State, Window };
use serde::{Deserialize, Serialize};


#[command]
fn greet(name: &str) -> String {
  format!("Hello, {name}!")
}

#[command]
fn update_tickets() -> Vec<serde_json::Value>{
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


fn main() {
  let is_debug: bool = false;
  if is_debug{
    let mut api_obj : FreshAPI = api::FreshAPI::new();
    api_obj.get_reimage_tickets();
    return;
  }
  tauri::Builder::default()
  .invoke_handler(tauri::generate_handler![greet, update_tickets, close_ticket_task])
  .run(tauri::generate_context!())
  .expect("error while running tauri application");
}