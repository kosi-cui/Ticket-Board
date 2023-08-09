pub mod requests;
pub mod ticket_s;
pub mod dirs;
use std::fs::File;
use std::io::{prelude::*, BufWriter};

use serde_json::Value;


// Class for Freshservice API
pub struct FreshAPI{
    pub api_key: String,
    pub domain: String,
    pub xdg_dirs: dirs::XdgDirs,
}

// Implementation of FreshAPI
impl FreshAPI{
    pub fn new() -> FreshAPI{
        let mut new_api_obj = FreshAPI{
            api_key: String::new(),
            domain: String::new(),
            xdg_dirs: dirs::XdgDirs::new(),
        };
        new_api_obj.get_credentials();
        return new_api_obj;
    }


    pub fn get_credentials(&mut self){
        println!("Getting credentials...");
        if !self.xdg_dirs.check_file_exists("conf"){
            println!("No conf file found, creating one...");

            // Get credentials from user
            println!("Please enter your Freshservice API key:");
            let mut temp_key : String = String::new();
            std::io::stdin().read_line(&mut temp_key).unwrap();
            println!("Please enter your Freshservice domain (Example: cuihelpdesk):");
            let mut temp_domain : String = String::new();
            std::io::stdin().read_line(&mut temp_domain).unwrap();
            temp_domain = "https://".to_string() + &temp_domain.trim_end().to_string() + ".freshservice.com";
            self.api_key = temp_key.trim_end().to_string();
            self.domain = temp_domain.trim_end().to_string();

            // Create conf file
            let _ = self.create_conf_file();
        }
        else {
            println!("Conf file found, reading...");
            self.read_conf_file().unwrap();
        }
        println!("Credentials: {:#?}, {:#?}", self.api_key, self.domain)
    }

    fn create_conf_file(&mut self) -> std::io::Result<()>{
        let file_path: String = dirs::XdgDirs::append_to_path(&self.xdg_dirs.config_dir, "conf").into_os_string().into_string().unwrap();
        let mut file = File::create(file_path)?;
        file.write_all(format!("{0}\n{1}", self.api_key, self.domain).as_bytes())?;
        Ok(())
    }

    fn read_conf_file(&mut self) -> std::io::Result<()>{
        let file_path: String = dirs::XdgDirs::append_to_path(&self.xdg_dirs.config_dir, "conf").into_os_string().into_string().unwrap();
        let mut file = File::open(file_path)?;
        let mut contents = String::new();
        file.read_to_string(&mut contents)?;
        let contents: Vec<&str> = contents.split("\n").collect();
        self.api_key = contents[0].to_string();
        self.domain = contents[1].to_string();
        Ok(())
    }


    pub fn get_ticket(&mut self, id: i32) {
        println!("Getting ticket...");
        let ticket_url_addition = "/api/v2/tickets/".to_string() + &id.to_string();
        let url = self.domain.to_string() + &ticket_url_addition;
        let req = requests::ticket_get_request(self.api_key.to_string(), url);
        let ticket_json: Value = serde_json::from_value(req).unwrap();
        let _ = self.write_ticket_file(ticket_json, id);
    }

    fn write_ticket_file(&mut self, ticket: Value, id: i32) -> std::io::Result<()>{
        let file_name = format!("{0}.json", id.to_string());
        let file_path: String = dirs::XdgDirs::append_to_path(&self.xdg_dirs.data_dir, &file_name).into_os_string().into_string().unwrap();
        println!("Writing ticket to {0}", file_path);
        let file = File::create(file_path)?;
        let mut writer = BufWriter::new(&file);
        serde_json::to_writer_pretty(&mut writer, &ticket)?;
        writer.flush()?;
        Ok(())
    }

    pub fn get_reimage_ticket_ids(&mut self, query: &str) -> Vec<i32>{
        let query_addition = format!("\"{}\"", query);
        let mut url = self.domain.to_string() + r#"/api/v2/search/tickets?query="# + query_addition.as_str();
        url = url.to_string();
        let req = requests::ticket_get_request(self.api_key.to_string(), url);
        let mut ticket_ids: Vec<i32> = Vec::new();
        for ticket in req["tickets"].as_object().unwrap(){
            //ticket_ids.push(ticket["id"].as_i64().unwrap() as i32);
        }

        return ticket_ids;
    }
}