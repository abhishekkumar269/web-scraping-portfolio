# Exposure Basketball Stats Scraper 🏀

## 📌 Overview
    This project Extracts basketball team stats, player data, and results from Exposure. website using Python.  
    It collects real-time market data, processes it, and stores it in a CSV file for further analysis.

---

## ⚙️ Features
    - Extracts business/job listings with details like name, location, and rating.  
    - Handles pagination and dynamic loading smoothly.  
    - Saves output in **CSV/Excel** format.  
    - Includes detailed error-handling and logging.  
    - Built with flexibility to scale for large datasets.
---

## 🚀 How to Run

    1. **Clone this repository (or open this folder):**
       ```bash
       git clone https://github.com/abhishekkumar269/web-scraping-portfolio.git
       cd web-scraping-portfolio/Exposure_Basketball
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python ExposureBasketball_scraper.py
    
    4. Output:
        Scraped data → all_events_data.csv
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

<img width="757" height="365" alt="Screenshot 2025-10-07 at 6 03 50 PM" src="https://github.com/user-attachments/assets/d5847a1d-e16c-4ae2-a3c8-e6dc2e88bd36" />


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
