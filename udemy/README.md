# Udemy Course Data Scraper 🎯

## 📌 Overview
    This project Scrapes course titles, instructors, and prices from Udemy website using Python.  
    It collects real-time market data, processes it, and stores it in a CSV file for further analysis.

---

## ⚙️ Features
    - Collects structured course/movie information (title, author, price, etc.).  
    - Outputs clean, formatted data in **CSV/JSON** format.  
    - Supports dynamic pages with Selenium or BeautifulSoup.  
    - Easy to adapt for similar websites or datasets.  
    - Comes with sample dataset and screenshots.
---

## 🚀 How to Run

    1. **Clone this repository (or open this folder):**
       ```bash
       git clone https://github.com/abhishekkumar269/web-scraping-portfolio.git
       cd web-scraping-portfolio/Udemy
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python udemy_scraper.py 
    
    4. Output:
        Scraped data → udemy_courses_data.csv
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

<img width="758" height="369" alt="Screenshot 2025-10-07 at 5 22 17 PM" src="https://github.com/user-attachments/assets/e4cd9fe7-7d2f-4456-8551-66ebe3f003b4" />


---
## 📂 Project Structure
      
    Udemy/
      │── udemy_scraper.py              # Main scraper script
      │── udemy_courses_data.csv        # Sample scraped data
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
