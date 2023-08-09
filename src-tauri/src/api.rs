#[tokio::main]

pub async fn request() -> Result<(), reqwest::Error> {
    let res = reqwest::get("https://www.rust-lang.org").await?;
    println!("Status: {}", res.status());
    Ok(())
}