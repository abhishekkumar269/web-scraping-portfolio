# Flipkart Product Scraper 🛒

## 📌 Overview
    This project scrapes product details (name, price, ratings, and reviews) from **Flipkart** using Python.  
    It collects e-commerce data, processes it, and stores it in a CSV file for market analysis.


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
       cd web-scraping-portfolio/Flipkart

    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python flipkart_scraper.py 
    
    4. Output:
        Scraped data → mobile_data.csv
          Logs → log.txt

---

## 📊 Sample Output

                                                MODEL_NAME    PRICE RATING           REVIEW
    0   Samsung Galaxy Book4 Edge Series Copilot AI-PC...  ₹55,590    4.3     501 Ratings 
    1   Samsung Galaxy Book4 Metal Intel Core i5 13th ...  ₹49,990    4.4  12,838 Ratings 
    2   Samsung Galaxy Book4 Metal Intel Core i5 13th ...  ₹48,990    4.4  12,838 Ratings 
    3   Acer Aspire Go 14 Intel Core Ultra 5 125H - (1...  ₹47,990    4.4      11 Ratings 
        

---
## 📸 Sample Screenshot

<img width="559" height="535" alt="Screenshot 2025-10-07 at 5 16 24 PM" src="https://github.com/user-attachments/assets/5069aa73-07f6-4e0f-b71a-7abc2661071d" />

---
## 📂 Project Structure
      
    Flipkart/
      │── flipkart_scraper.py       # Main scraper script
      │── mobile_data.csv           # Sample scraped data
      │── log.txt                   # Log file for scraping activity
      │── requirements.txt          # Python dependencies
      │── README.md                 # Project documentation
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
