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
           City   Date High_Temp Low_Tem                      Condition Precipitation         Wind
1   Chennai  10/10       32°     26°                 Turning cloudy           25%    S 11 km/h
2   Chennai  11/10       31°     25°                  Sunny periods           25%  NNW 13 km/h
3   Chennai  12/10       32°     26°  Partly sunny, a shower or two           80%  NNE 15 km/h
4   Chennai  13/10       32°     25°   An a.m. shower; partly sunny           55%  NNE 15 km/h
5   Chennai  14/10       32°     25°   A little rain in the morning           61%  NNE 13 km/h

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
