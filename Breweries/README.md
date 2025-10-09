# Breweries Data Scraper 🍺

## 📌 Overview
    This project Collects brewery information such as name, location, and beer types. website using Python.  
    It collects real-time market data, processes it, and stores it in a CSV file for further analysis.

---

## ⚙️ Features
    - Fetches and parses API or web data automatically.  
    - Converts raw JSON to clean, readable CSV files.  
    - Integrates with schedulers for automated runs.  
    - Logs all activities for transparency.  
    - Simple, reusable, and well-documented codebase.

---

## 🚀 How to Run

    1. **Clone this repository (or open this folder):**
       ```bash
       git clone https://github.com/abhishekkumar269/web-scraping-portfolio.git
       cd web-scraping-portfolio/Breweries
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python read_all_data.py
    
    4. Output:
        Scraped data → 
          Logs → log.txt

---

## 📊 Sample Output

    | COMPANY   | LTP    | CHANGE |
    | --------- | ------ | ------ |
    | Reliance  | 2450.5 | +1.25% |
    | TCS       | 3321.0 | -0.85% |
    | HDFC Bank | 1567.3 | +0.45% |
    

---
## 📸 Sample Screenshot



---
## 📂 Project Structure
      
    Breweries/
      │── read_all_data.py      # Main scraper script
      │── xxx                   # Sample scraped data
      │── log.txt               # Log file for scraping activity
      │── requirements.txt      # Python dependencies
      │── README.md             # Project documentation
---

## 🛠️ Tech Stack

      Python 3
      Requests / BeautifulSoup (web scraping)
      CSV (data storage)
      Logging (activity tracking)

---
## ✨ Future Improvement

      Automate daily scraping using cron jobs.
      Add data visualization (graphs, charts).
      Store results in a database.

---
👨‍💻 Author: Abhishek Kumar

  🔗 Part of https://github.com/abhishekkumar269/web-scraping-portfolio
