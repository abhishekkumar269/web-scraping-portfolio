# CarDekho Car Listings Scraper 🚗

## 📌 Overview
    This project Scrapes car details, prices, and models from CarDekho. website using Python.  
    It collects real-time market data, processes it, and stores it in a CSV file for further analysis.

---

## ⚙️ Features
    - Extracts product names, prices, and ratings efficiently.  
    - Saves output in **CSV or Excel** format for easy analysis.  
    - Handles pagination and multiple category pages automatically.  
    - Uses clean and modular Python code for customization.  
    - Includes sample output and logs for reference.

---

## 🚀 How to Run

    1. **Clone this repository (or open this folder):**
       ```bash
       git clone https://github.com/abhishekkumar269/web-scraping-portfolio.git
       cd web-scraping-portfolio/CarDekho
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python cardekho_scraper.py
    
    4. Output:
        Scraped data → cars_data.csv
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

<img width="761" height="559" alt="Screenshot 2025-10-07 at 5 12 16 PM" src="https://github.com/user-attachments/assets/9e37c5d3-b989-47b4-bb6d-fc41ae3d88e9" />


---
## 📂 Project Structure
      
    CarDekho
      │── cardekho_scraper.py       # Main scraper script
      │── cars_data.csv             # Sample scraped data
      │── log.txt                   # Log file for scraping activity
      │── requirements.txt          # Python dependencies
      │── README.md                 # Project documentation
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
