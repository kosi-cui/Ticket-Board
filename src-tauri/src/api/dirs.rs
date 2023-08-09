use std::path::{PathBuf, Path};

const PROJECT: &str = "freshservive-tauri";
const ORG: &str = "CUI ITS";
const APP: &str = "freshservice-tauri";

#[derive(Debug)]
pub struct XdgDirs {
    cache_dir: PathBuf,
    pub config_dir: PathBuf,
    pub data_dir: PathBuf,
    runtime_dir: PathBuf,
}

impl XdgDirs{
    pub fn new() -> XdgDirs{
        let x = directories_next::ProjectDirs::from(PROJECT, ORG, APP).unwrap();
        let output = XdgDirs {
            cache_dir: x.cache_dir().to_path_buf(),
            config_dir: x.config_dir().to_path_buf(),
            data_dir: x.data_dir().to_path_buf(),
            runtime_dir: x.cache_dir().to_path_buf(),
        };


        if !Path::new(x.config_dir()).is_dir() {
            println!("{:#?} does not exist, creating...", output.config_dir);
            let _ = std::fs::create_dir_all(&output.config_dir);
            let _ = std::fs::create_dir(&output.cache_dir);
            let _ = std::fs::create_dir(&output.data_dir);
            let _ = std::fs::create_dir(&output.runtime_dir);
        }

        return output;
    }

    pub fn check_file_exists(&self, file_name: &str) -> bool{
        let p = XdgDirs::append_to_path(&self.config_dir, file_name);  
        println!("Checking if file exists: {:#?}", p);
        p.exists()
    }

    pub fn append_to_path(p: &PathBuf, s: &str) -> PathBuf {
        let mut p = p.clone();
        p.push(s);
        p
    }
}