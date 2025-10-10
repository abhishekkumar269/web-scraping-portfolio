# Fake Store API Data Extractor 🛍️

## 📌 Overview
    This project Fetches product data and pricing from FakeStoreAPI for testing/demo. website using Python.  
    It collects real-time market data, processes it, and stores it in a CSV file for further analysis.

---

## ⚙️ Features
    - Fetches and parses API or web data automatically.  
    - Converts raw JSON to clean, readable CSV files.  
    - Integrates with schedulers for automated runs.  
    - Logs all activities for transparency.  
    - Simple, reusable, and well-documented codebase.
---

## 🚀 How to Run

    1. **Clone this repository (or open this folder):**
       ```bash
       git clone https://github.com/abhishekkumar269/web-scraping-portfolio.git
       cd web-scraping-portfolio/FakeStoreApi
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python read_data.py
    
    4. Output:
        Scraped data → products_data.csv
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

<img width="962" height="574" alt="Screenshot 2025-10-07 at 5 15 56 PM" src="https://github.com/user-attachments/assets/8498b83f-40de-41b2-a394-e84ea74dc067" />

---
## 📂 Project Structure
      
    ID                                              TITLE   PRICE  ...                                              IMAGE RATING VOTE_PEOPLE
0    1  Fjallraven - Foldsack No. 1 Backpack, Fits 15 ...  109.95  ...  https://fakestoreapi.com/img/81fPKd-2AYL._AC_S...    3.9         120
1    2             Mens Casual Premium Slim Fit T-Shirts    22.30  ...  https://fakestoreapi.com/img/71-3HjGNDUL._AC_S...    4.1         259
2    3                                 Mens Cotton Jacket   55.99  ...  https://fakestoreapi.com/img/71li-ujtlUL._AC_U...    4.7         500
3    4                               Mens Casual Slim Fit   15.99  ...  https://fakestoreapi.com/img/71YXzeOuslL._AC_U...    2.1         430
4    5  John Hardy Women's Legends Naga Gold & Silver ...  695.00  ...  https://fakestoreapi.com/img/71pWzhdJNwL._AC_U...    4.6         400
5    6                       Solid Gold Petite Micropave   168.00  ...  https://fakestoreapi.com/img/61sbMiUnoGL._AC_U...    3.9          70
6    7                         White Gold Plated Princess    9.99  ...  https://fakestoreapi.com/img/71YAIFU48IL._AC_U...    3.0         400
7    8  Pierced Owl Rose Gold Plated Stainless Steel D...   10.99  ...  https://fakestoreapi.com/img/51UDEzMJVpL._AC_U...    1.9         100
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
