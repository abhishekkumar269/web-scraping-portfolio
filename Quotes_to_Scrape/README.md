# Quotes to Scrape Extractor 💬

## 📌 Overview
    This project Scrapes quotes, authors, and tags from the QuotesToScrape website. website using Python.  
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
       cd web-scraping-portfolio/Quotes_to_Scrape
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python quotes_scraper.py 
    
    4. Output:
        Scraped data → quotes_data.csv
          Logs → log.txt

---

## 📊 Sample Output
                                                Quote             Author                                            Tags
1   “The world as we have created it is a process ...    Albert Einstein        [change, deep-thoughts, thinking, world]
2   “It is our choices, Harry, that show what we t...       J.K. Rowling                            [abilities, choices]
3   “There are only two ways to live your life. On...    Albert Einstein  [inspirational, life, live, miracle, miracles]
4   “The person, be it gentleman or lady, who has ...        Jane Austen              [aliteracy, books, classic, humor]
5   “Imperfection is beauty, madness is genius and...     Marilyn Monroe                    [be-yourself, inspirational]
6   “Try not to become a man of success. Rather be...    Albert Einstein                     [adulthood, success, value]
7   “It is better to be hated for what you are tha...         André Gide                                    [life, love]
8   “I have not failed. I've just found 10,000 way...   Thomas A. Edison   [edison, failure, inspirational, paraphrased]
9   “A woman is like a tea bag; you never know how...  Eleanor Roosevelt               [misattributed-eleanor-roosevelt]
10  “A day without sunshine is like, you know, nig...       Steve Martin                        [humor, obvious, simile]
                                            
---
## 📸 Sample Screenshot

<img width="828" height="570" alt="Screenshot 2025-10-07 at 5 20 37 PM" src="https://github.com/user-attachments/assets/bea7a738-5b0f-4fec-a243-daa01d112272" />


---
## 📂 Project Structure
      
    Quotes_to_Scrape/
      │── quotes_scraper.py         # Main scraper script
      │── quotes_data.csv           # Sample scraped data
      │── log.txt                   # Log file for scraping activity
      │── requirements.txt          # Python dependencies
      │── screenshot.png            # Demo screenshot (sample output/website)
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
