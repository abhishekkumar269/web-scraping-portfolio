# Business Standard News Scraper 📰

## 📌 Overview
    This project Extracts the latest business and finance headlines from Business Standard. website using Python.  
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

    46    HINDALCO     767.00  -1.25
    47  TATACONSUM   1,123.90  -1.59
    48       TRENT   4,685.00  -1.93
    49    AXISBANK   1,188.00  -2.04
    50  TATAMOTORS     698.10  -2.04
    

---
## 📸 Sample Screenshot

<img width="813" height="566" alt="Screenshot 2025-10-07 at 5 13 27 PM" src="https://github.com/user-attachments/assets/57736467-2f2e-4b9c-b3d8-a21d5ac4cf20" />


---
## 📂 Project Structure
      
      NSE/
      │── nse_scraper.py       # Main scraper script
      │── nse_data.csv         # Sample scraped data
      │── log.txt              # Log file for scraping activity
      │── requirements.txt     # Python dependencies
      │── screenshot.png       # Demo screenshot (sample output/website)
      │── README.md            # Project documentation
---

## 🛠️ Tech Stack

      Python 3
      Requests / BeautifulSoup (web scraping)
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
