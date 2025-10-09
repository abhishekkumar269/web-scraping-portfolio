# Flipkart Product Scraper 🛒

## 📌 Overview
    This project scrapes stock market data from the **NSE (National Stock Exchange of India)** website using Python.  
    It collects real-time market data, processes it, and stores it in a CSV file for further analysis.

---

## ⚙️ Features
    - Extracts product names, prices, and ratings efficiently.  
    - Saves output in **CSV or Excel** format for easy analysis.  
    - Handles pagination and multiple category pages automatically.  
    - Uses clean and modular Python code for customization.  
    - Includes sample output and logs for reference.
---

## 🚀 How to Run

    1. **Clone this repository (or open this folder):**
       ```bash
       git clone https://github.com/abhishekkumar269/web-scraping-portfolio.git
       cd web-scraping-portfolio/Flipkart

    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python flipkart_scraper.py 
    
    4. Output:
        Scraped data → mobile_data.csv
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

<img width="559" height="535" alt="Screenshot 2025-10-07 at 5 16 24 PM" src="https://github.com/user-attachments/assets/5069aa73-07f6-4e0f-b71a-7abc2661071d" />

---
## 📂 Project Structure
      
    Flipkart/
      │── flipkart_scraper.py       # Main scraper script
      │── mobile_data.csv           # Sample scraped data
      │── log.txt                   # Log file for scraping activity
      │── requirements.txt          # Python dependencies
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
