# Business Standard News Scraper 📰

## 📌 Overview
    This project Extracts the latest business and finance headlines from Business Standard. website using Python.  
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
       cd web-scraping-portfolio/BusinessStandard
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python bs_scraper.py
    
    4. Output:
        Scraped data → finance_data.csv
          Logs → log.txt

---

## 📊 Sample Output

                                                    TITLE                                               LINK                                     TIME
    1   SpiceJet shares jump 7% on aircraft additions;...  https://www.business-standard.com/markets/news...  Updated On : 10 Oct 2025 | 11:13 AM IST
    2   Why did Sona BLW shares rise over 4% in trade ...  https://www.business-standard.com/markets/news...  Updated On : 10 Oct 2025 | 11:12 AM IST
    3   Natco Pharma up 6% as Delhi HC clears SMA drug...  https://www.business-standard.com/markets/news...  Updated On : 10 Oct 2025 | 11:08 AM IST
    4   Stock Market LIVE: HDFC Bank, ICICI Bank lift ...  https://www.business-standard.com/markets/news...  Updated On : 10 Oct 2025 | 11:07 AM IST
    5   Commodities booming; other MFs may also halt s...  https://www.business-standard.com/markets/news...  Updated On : 10 Oct 2025 | 11:01 AM IST
    

---
## 📸 Sample Screenshot

<img width="813" height="566" alt="Screenshot 2025-10-07 at 5 13 27 PM" src="https://github.com/user-attachments/assets/57736467-2f2e-4b9c-b3d8-a21d5ac4cf20" />


---
## 📂 Project Structure
      
    BusinessStandard/
      │── bs_scraper.py        # Main scraper script
      │── finance_data.csv     # Sample scraped data
      │── log.txt              # Log file for scraping activity
      │── requirements.txt     # Python dependencies
      │── README.md            # Project documentation
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
