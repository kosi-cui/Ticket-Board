pub use super::ticket_s;
use serde_json::Value;

#[tokio::main]
pub async fn ticket_get_request(key: String, url: String) -> Value {
    let client: reqwest::Client = reqwest::Client::new();
    let response = client
    .get(&url)
    .basic_auth(key, Some("X"))
    .send()
    .await;

    let response_json : Value  = serde_json::from_str(&response.unwrap().text().await.unwrap()).unwrap();

    return response_json;
}


// Things needed to update a task:
/*
    status: (3 to close)
    notify_before: set to 0
    title: keep the title of the task
    description: keep the description of the task
*/

#[tokio::main]
pub async fn ticket_put_request(key: String, url: String, data: Value) {
    let client = reqwest::Client::new();
    let _ = client
    .put(url)
    .basic_auth(key, Some("X"))
    .json(&data)
    .send()
    .await;
}

#[tokio::main]
pub async fn ticket_post_request(key: String, url: String, data: Value) {
    let client = reqwest::Client::new();
    let _ = client
    .post(url)
    .basic_auth(key, Some("X"))
    .json(&data)
    .send()
    .await;
}