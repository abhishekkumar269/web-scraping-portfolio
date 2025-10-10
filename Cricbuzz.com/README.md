# Cricbuzz Live Score Scraper 🏏

## 📌 Overview
    This project scrapes Get Live Cricket Scores, Scorecard, Schedules of International and Domestic cricket matches along with Latest News website using Python.  
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
       cd web-scraping-portfolio/Cricbuzz.com
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python cricbuzz_scraper.py
    
    4. Output:
        Scraped data → sport_scores.csv
          Logs → log.txt

---

## 📊 Sample Output
                                  MATCH_TITLE                                              VENUE                                               LINK
    1                   India vs West Indies,                                                 •   https://www.cricbuzz.com/live-cricket-scores/1...
    2       United Arab Emirates vs Malaysia,  at Al Amerat, Al Amerat Cricket Ground (Minist...  https://www.cricbuzz.com/live-cricket-scores/1...
    3                         Nepal vs Japan,  at Al Amerat, Al Amerat Cricket Ground (Minist...  https://www.cricbuzz.com/live-cricket-scores/1...
    4               Oman vs Papua New Guinea,  at Al Amerat, Al Amerat Cricket Ground (Minist...  https://www.cricbuzz.com/live-cricket-scores/1...

---
## 📸 Sample Screenshot

<img width="816" height="473" alt="Screenshot 2025-10-07 at 5 14 17 PM" src="https://github.com/user-attachments/assets/e251a7d3-bbbc-4ed6-8622-02ebd2e49f06" />


---
## 📂 Project Structure
      
    Cricbuzz.com/
      │── cricbuzz_scraper.py      # Main scraper script
      │── sport_scores.csv         # Sample scraped data
      │── log.txt                  # Log file for scraping activity
      │── requirements.txt         # Python dependencies
      │── README.md                # Project documentation
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
