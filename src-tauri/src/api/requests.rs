
pub use super::ticket_s;

#[tokio::main]
pub async fn ticket_get_request(key: String, url: String) -> Result<(), reqwest::Error> {
    let client: reqwest::Client = reqwest::Client::new();
    let response = client
    .get(&url)
    .basic_auth(key, Some("X"))
    .send()
    .await?
    .json::<ticket_s::Ticket>()
    .await;
    println!("{:#?}", response);
    Ok(())
}
