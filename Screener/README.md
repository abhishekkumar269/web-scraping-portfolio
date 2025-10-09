# Screener company Scraper 📊

## 📌 Overview
    This project Extracted company name,company link. website using Python.  
    It collects relevant data, processes it, and saves the results in CSV or JSON format for further analysis.

---

## ⚙️ Features
    - Scrapes real-time data from the target website.  
    - Exports structured results in **CSV/JSON** format.  
    - Includes detailed logging for transparency and debugging.  
    - Lightweight and simple to configure.  
    - Ready to automate with cron jobs or schedulers.

---

## 🚀 How to Run

    1. **Clone this repository (or open this folder):**
       ```bash
       git clone https://github.com/abhishekkumar269/web-scraping-portfolio.git
       cd web-scraping-portfolio/Screener
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python screener_scraper.py
    
    4. Output:
        Scraped data → company_list.csv
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

<img width="505" height="475" alt="Screenshot 2025-10-09 at 12 31 53 AM" src="https://github.com/user-attachments/assets/10b2f226-a15f-4990-9847-e16e62dea858" />


---
## 📂 Project Structure
      
    Screener/
      │── screener_scraper.py           # Main scraper script
      │── company_list.csv              # Sample scraped data
      │── log.txt                       # Log file for scraping activity
      │── requirements.txt              # Python dependencies
      │── README.md                     # Project documentation
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
