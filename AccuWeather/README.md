# AccuWeather Forecast Scraper 🌦️

## 📌 Overview
    This project Fetches live weather updates and forecasts from AccuWeather. website using Python.  
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
       cd web-scraping-portfolio/AccuWeather
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python Chennai_scraper.py
    
    4. Output:
        Scraped data → chennai_weather_data.csv 
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

<img width="621" height="323" alt="Screenshot 2025-10-07 at 5 08 24 PM" src="https://github.com/user-attachments/assets/34f09233-6671-4333-8232-46e5c5600b56" />


---
## 📂 Project Structure
      
      ACUWEATER/
      │── Chennai_scraper.py             # Main scraper script
      │── chennai_weather_data.csv       # Sample scraped data
      │── log.txt                        # Log file for scraping activity
      │── requirements.txt               # Python dependencies
      │── README.md                      # Project documentation
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
