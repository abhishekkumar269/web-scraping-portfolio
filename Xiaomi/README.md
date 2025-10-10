# Xiaomi Product Scraper 📱

## 📌 Overview
    This project Fetches Xiaomi product data, specifications, and prices. website using Python.  
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
       cd web-scraping-portfolio/Xiaomi
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python redmimobile_scraper.py
    
    4. Output:
        Scraped data → mi_data.csv
          Logs → log.txt

---

## 📊 Sample Output

                         name
    0                Redmi A5
    1            Redmi 14C 5G
    2   Redmi Note 14 Pro+ 5G
    3    Redmi Note 14 Pro 5G
    4        Redmi Note 14 5G
    5             Redmi A4 5G
    6             Redmi 13 5G
    7               Redmi A3X

---
## 📸 Sample Screenshot

<img width="208" height="372" alt="Screenshot 2025-10-10 at 5 45 13 PM" src="https://github.com/user-attachments/assets/efae244b-0c94-4b3a-917b-a3e28a7ee9d6" />


---
## 📂 Project Structure
      
    Xiaomi/
      │── redmimobile_scraper.py        # Main scraper script
      │── mi_data.csv                   # Sample scraped data
      │── log.txt                       # Log file for scraping activity
      │── requirements.txt              # Python dependencies
      │── README.md                     # Project documentation
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
