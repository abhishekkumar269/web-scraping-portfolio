# Quotes to Scrape Extractor 💬

## 📌 Overview
    This project Scrapes quotes, authors, and tags from the QuotesToScrape website. website using Python.  
    It collects real-time market data, processes it, and stores it in a CSV file for further analysis.

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
       cd web-scraping-portfolio/Quotes_to_Scrape
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python quotes_scraper.py 
    
    4. Output:
        Scraped data → quotes_data.csv
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

<img width="828" height="570" alt="Screenshot 2025-10-07 at 5 20 37 PM" src="https://github.com/user-attachments/assets/bea7a738-5b0f-4fec-a243-daa01d112272" />


---
## 📂 Project Structure
      
    Quotes_to_Scrape/
      │── quotes_scraper.py         # Main scraper script
      │── quotes_data.csv           # Sample scraped data
      │── log.txt                   # Log file for scraping activity
      │── requirements.txt          # Python dependencies
      │── screenshot.png            # Demo screenshot (sample output/website)
      │── README.md                 # Project documentation
---

## 🛠️ Tech Stack

      Python 3
      Selenium, BeautifulSoup, Requests  
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
