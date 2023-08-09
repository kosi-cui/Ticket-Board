pub use super::ticket_s;
use serde_json::Value;

#[tokio::main]
pub async fn ticket_get_request(key: String, url: String) -> serde_json::Value {
    println!("{:#?}", url);
    let client: reqwest::Client = reqwest::Client::new();
    let response = client
    .get(&url)
    .basic_auth(key, Some("X"))
    .send()
    .await;

    println!("{:#?}", response);
    let response_json : Value  = serde_json::from_str(&response.unwrap().text().await.unwrap()).unwrap();

    println!("{:#?}", response_json);
    return response_json;
}