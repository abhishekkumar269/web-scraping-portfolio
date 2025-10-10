# IPL 2022 Stats Scraper 🏆

## 📌 Overview
    This project Scrapes IPL 2022 match results, team stats, and player performance. website using Python.  
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
       cd web-scraping-portfolio/IPL_2022
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python ipl2025.py
    
    4. Output:
        Scraped data → ipl_auction.csv
          Logs → log.txt

---

## 📊 Sample Output

    sno                                       team       fun_rem over_ply totl_ply
    0   1          \n\n\n\n\nChennai Super Kings\n\n  ₹2,95,00,000        8       25
    1   2               \n\n\n\n\nDelhi Capitals\n\n    ₹10,00,000        7       24
    2   3               \n\n\n\n\nGujarat Titans\n\n    ₹15,00,000        8       23
    3   4        \n\n\n\n\nKolkata Knight Riders\n\n    ₹45,00,000        8       25
    4   5         \n\n\n\n\nLucknow Super Giants\n\n            ₹0        7       21

---
## 📸 Sample Screenshot

<img width="481" height="549" alt="Screenshot 2025-10-07 at 5 17 53 PM" src="https://github.com/user-attachments/assets/3517a52a-d0b1-45a8-9771-4dc9e863f99b" />

---
## 📂 Project Structure
      
    IPL_2022/
      │── ipl2025.py           # Main scraper script
      │── ipl_auction.csv      # Sample scraped data
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
