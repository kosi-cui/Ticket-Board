// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use api::FreshAPI;
mod api;

use tauri::{ command, Manager };
use serde_json::{Value, json};


#[command]
fn greet(name: &str) -> String {
  format!("Hello, {name}!")
}

#[command]
fn update_tickets() -> Vec<Value>{
  let mut api_obj : FreshAPI = api::FreshAPI::new();
  if api_obj.valid_creds {
    let ticket_jsons = api_obj.get_reimage_tickets();
    ticket_jsons
  }
  else {
    let mut output = Vec::new();
    let invalid_cred_json = json!(
      {
        "title": "Invalid Credentials",
        "conf_folder": api_obj.xdg_dirs.config_dir.to_str().unwrap(),
      }
    );
    output.push(invalid_cred_json);
    output
  }
}

#[command]
fn get_credentials() -> Vec<String>{
  let api_obj : FreshAPI = api::FreshAPI::new();
  let mut creds: Vec<String> = Vec::new();
  creds.push(api_obj.api_key);
  creds.push(api_obj.domain);
  creds
}

#[command]
fn update_credentials(api_key: String, domain: String){
  
  // Error-checking for proper domain format
  let mut input_domain = domain.clone();
  let s = domain.chars();
  let sub : String = s.into_iter().take(8).collect();
  if sub != "https://" {
    input_domain = format!("https://{}", domain);
  }


  let mut api_obj : FreshAPI = api::FreshAPI::new();
  api_obj.update_credentials(api_key, input_domain);
}


#[command]
fn close_ticket_task(ticket_id: i32, task_id: i32){
  let mut api_obj : FreshAPI = api::FreshAPI::new();
  api_obj.close_ticket_task(ticket_id, task_id);
  update_tickets();
}

#[command]
fn clean_ticket_update() -> Vec<Value> {
  let mut api_obj : FreshAPI = api::FreshAPI::new();
  println!("Valid Creds: {}", api_obj.valid_creds);
  if api_obj.valid_creds {
    let output = api_obj.clean_get_tickets();
    output
  }
  else {
    let mut output = Vec::new();
    let invalid_cred_json = json!(
      {
        "title": "Invalid Credentials",
        "conf_folder": api_obj.xdg_dirs.config_dir.to_str().unwrap(),
      }
    );
    output.push(invalid_cred_json);
    output
  }
}

#[command]
fn resolve_ticket(ticket_id: i32, agent_id: i32) {
  println!("Resolving ticket: {}", ticket_id);
  let mut api_obj : FreshAPI = api::FreshAPI::new();
  api_obj.close_ticket(ticket_id, agent_id);
}

fn main() {
  tauri::Builder::default()
  .setup(|app| {
    let app_handle = app.app_handle();
    tauri::async_runtime::spawn(async move {
      loop {
        tokio::time::sleep(tokio::time::Duration::from_secs(60 * 60)).await;
        app_handle.emit_all("backend-update-tickets", "updatePing").unwrap();
      }
    });
    Ok(())
  })
  .invoke_handler(tauri::generate_handler![
    greet, 
    update_tickets, 
    close_ticket_task, 
    clean_ticket_update,
    get_credentials,
    update_credentials,
    resolve_ticket
    ]
  )
  .run(tauri::generate_context!())
  .expect("error while running tauri application");
}