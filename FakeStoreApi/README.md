# Fake Store API Data Extractor 🛍️

## 📌 Overview
    This project Fetches product data and pricing from FakeStoreAPI for testing/demo. website using Python.  
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
       cd web-scraping-portfolio/FakeStoreApi
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python read_data.py
    
    4. Output:
        Scraped data → products_data.csv
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

<img width="962" height="574" alt="Screenshot 2025-10-07 at 5 15 56 PM" src="https://github.com/user-attachments/assets/8498b83f-40de-41b2-a394-e84ea74dc067" />

---
## 📂 Project Structure
      
    FakeStoreApi/
      │── read_data.py              # Main scraper script
      │── products_data.csv         # Sample scraped data
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
