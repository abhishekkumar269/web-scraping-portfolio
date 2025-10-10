# MagicBricks Real Estate Scraper 🏠

## 📌 Overview
    This project Scrapes property listings, locations, and pricing from MagicBricks.website using Python.  
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
       cd web-scraping-portfolio/MagicBricks
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python magicbrick_scraper.py
    
    4. Output:
        Scraped data → magicbricks_data.csv 
          Logs → log.txt

---

## 📊 Sample Output

                                                    TITLE       PRICE
    0   3 BHK Flat for Sale in Essel Towers, Mehrauli ...  ₹\n3.45 Cr
    1   3 BHK Flat for Sale in Sublime Spring Elmas, N...  ₹\n1.89 Cr
    2   3 BHK Flat for Sale in Munirka Enclave, Munirk...  ₹\n3.15 Cr
    3             3 BHK Flat for Sale in Saket, New Delhi   ₹\n99 Lac
    4   2 BHK Flat for Sale in DLF One Midtown, Moti N...  ₹\n3.89 Cr
    5   3 BHK Flat for Sale in Sunworld Vanalika, Sect...  ₹\n1.60 Cr
    

---
## 📸 Sample Screenshot

<img width="554" height="479" alt="Screenshot 2025-10-07 at 5 19 10 PM" src="https://github.com/user-attachments/assets/d78ff74c-19d4-4ae9-824a-45813db2189d" />

---
## 📂 Project Structure
      
    MagicBricks/
      │── magicbrick_scraper.py      # Main scraper script
      │── magicbricks_data.csv       # Sample scraped data
      │── log.txt                    # Log file for scraping activity
      │── requirements.txt           # Python dependencies
      │── README.md                  # Project documentation
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
