# Books to Scrape Data Extractor 📚

## 📌 Overview
    This project Scrapes book details, prices, and ratings from the BooksToScrape website. website using Python.  
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
       cd web-scraping-portfolio/Books_to_Scrape
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python ScienceFiction_scraper.py
    
    4. Output:
        Scraped data → book_data.csv
          Logs → log.txt

---

## 📊 Sample Output
                                     TITLE   PRICE AVALIBITY                                        PRODUCT_URL DATE_SCRAPPING
    0              It's Only the Himalayas  £45.17  In stock  https://books.toscrape.com/catalogue/its-only-...     2025-10-10
    1            Full Moon over Noah’s ...  £49.43  In stock  https://books.toscrape.com/catalogue/full-moon...     2025-10-10
    2       See America: A Celebration ...  £48.87  In stock  https://books.toscrape.com/catalogue/see-ameri...     2025-10-10
    3   Vagabonding: An Uncommon Guide ...  £36.94  In stock  https://books.toscrape.com/catalogue/vagabondi...     2025-10-10
    4                 Under the Tuscan Sun  £37.33  In stock  https://books.toscrape.com/catalogue/under-the...     2025-10-10
        

---
## 📸 Sample Screenshot
<img width="1231" height="455" alt="Screenshot 2025-10-07 at 6 06 43 PM" src="https://github.com/user-attachments/assets/76288323-c8e0-43a3-bf51-4ff539d2bc7d" />


---
## 📂 Project Structure
      
    Books_to_Scrape/
      │── ScienceFiction_scraper.py      # Main scraper script
      │── book_data.csv                  # Sample scraped data
      │── log.txt                        # Log file for scraping activity
      │── requirements.txt               # Python dependencies
      │── README.md                      # Project documentation
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
