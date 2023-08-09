pub mod requests;
pub mod ticket_s;


// Class for Freshservice API
pub struct FreshAPI{
    pub api_key: String,
    pub domain: String,
}

// Implementation of FreshAPI
impl FreshAPI{
    pub fn new() -> FreshAPI{
        let mut new_api_obj = FreshAPI{
            api_key: String::new(),
            domain: String::new(),
        };

        new_api_obj.get_credentials();
        return new_api_obj;
    }

    pub fn get_credentials(&mut self) {
        println!("Getting credentials...");
        println!("Please enter your Freshservice API key:");
        let mut temp_key : String = String::new();
        let _b1 = std::io::stdin().read_line(&mut temp_key).unwrap();
        println!("Please enter your Freshservice domain (Example: cuihelpdesk):");
        let mut temp_domain : String = String::new();
        let _b2 = std::io::stdin().read_line(&mut temp_domain).unwrap();
        temp_domain = "https://".to_string() + &temp_domain.trim_end().to_string() + ".freshservice.com";
        println!("API Key: {0}\nDomain: {1}", temp_key, temp_domain);
        self.api_key = temp_key.trim_end().to_string();
        self.domain = temp_domain.trim_end().to_string();
    }

    pub fn get_ticket(&mut self, id: i32) {
        println!("Getting ticket...");
        let ticket_url_addition = "/api/v2/tickets/".to_string() + &id.to_string();
        let url = self.domain.to_string() + &ticket_url_addition;
        let req = requests::ticket_get_request(self.api_key.to_string(), url);
        println!("{:#?}", req);
    }
}