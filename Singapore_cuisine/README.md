# Singapore Cruise Centre (ferry & cruise)

## 📌 Overview
    This project Singapore Cruise Centre operates 1 cruise & 3 ferry terminals with services to the Riau islands (Batam, Bintan, Karimun) & Malaysia (Desaru).       website using Python.  
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
       cd web-scraping-portfolio/Singapore_cuisine
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python Arrival_scraper.py
    
    4. Output:
        Scraped data → ferri_departure_data.csv
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

<img width="201" height="421" alt="Screenshot 2025-10-07 at 5 21 40 PM" src="https://github.com/user-attachments/assets/287b8149-e3c1-481a-aeb1-cfc54b029704" />


---
## 📂 Project Structure
      
    Singapore_cuisine/
      │── Arrival_scraper.py                # Main scraper script
      │── ferri_departure_data.csv          # Sample scraped data
      │── log.txt                           # Log file for scraping activity
      │── requirements.txt                  # Python dependencies
      │── README.md                         # Project documentation
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
