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

                    DATE  TIME     STATUS
    0   Fri, 10 Oct 2025  1500    ARRIVED
    1   Fri, 10 Oct 2025  1510    ARRIVED
    2   Fri, 10 Oct 2025  1510  CONFIRMED
    3   Fri, 10 Oct 2025  1530  CONFIRMED
    4   Fri, 10 Oct 2025  1550  CONFIRMED
        

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
