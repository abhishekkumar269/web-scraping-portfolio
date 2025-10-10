# Adam Choi Football Match Scraper ⚽

## 📌 Overview
    This project scrapes stock market data from the **NSE (National Stock Exchange of India)** website using Python.  
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
       cd web-scraping-portfolio/Adamchoi
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python adamchoi_scraper.py
    
    4. Output:
        Scraped data → LaLiga_data.csv
          Logs → log.txt

---

## 📊 Sample Output

            DATE         TEAM-A RESULT      TEAM-B
    0    27-09-2025       Mallorca  1 - 0      Alaves
    1    24-09-2025         Getafe  1 - 1      Alaves
    2    20-09-2025         Alaves  1 - 2     Sevilla
    3    13-09-2025  Athletic Club  0 - 1      Alaves
    4    30-08-2025         Alaves  1 - 1  Ath Madrid
        

---
## 📸 Sample Screenshot

<img width="352" height="523" alt="Screenshot 2025-10-07 at 5 08 54 PM copy" src="https://github.com/user-attachments/assets/5da6a434-76a7-47df-9898-91a1e840bc58" />

---
## 📂 Project Structure
      
    Adamchoi/
      │── adamchoi_scraper.py   # Main scraper script
      │── LaLiga_data.csv       # Sample scraped data
      │── log.txt               # Log file for scraping activity
      │── requirements.txt      # Python dependencies
      │── README.md             # Project documentation
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
