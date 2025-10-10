# NSE Stock Data Scraper 📊

## 📌 Overview
    This project scrapes stock market data from the **NSE (National Stock Exchange of India)** website using Python.  
    It collects real-time market data, processes it, and stores it in a CSV file for further analysis.

---

## ⚙️ Features
    - Scrapes live NSE stock data.
    - Stores data in **CSV/JSON** for easy analysis. 
    - Generates logs for tracking scraping activity.
    - Lightweight and easy to run.
    - Includes a **requirements.txt** for quick setup. 

---

## 🚀 How to Run

    1. **Clone this repository (or open this folder):**
       ```bash
       git clone https://github.com/abhishekkumar269/web-scraping-portfolio.git
       cd web-scraping-portfolio/NSE
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python nse_scraper.py
    
    4. Output:
        Scraped data → nse_data.csv
          Logs → log.txt

---

## 📊 Sample Output

        COMPANY        LTP CHANGE
    1        CIPLA   1,558.90   3.03
    2         SBIN     880.35   2.12
    3       MARUTI  16,269.00   1.78
    4        TRENT   4,727.90   1.44
    5   ADANIPORTS   1,415.00   1.39
    

---
## 📸 Sample Screenshot

<img width="378" height="445" alt="screenshot" src="https://github.com/user-attachments/assets/533ec6a7-86a4-450e-8ce7-04ba9e65a651" />

---
## 📂 Project Structure
      
      NSE/
      │── nse_scraper.py       # Main scraper script
      │── nse_data.csv         # Sample scraped data
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
