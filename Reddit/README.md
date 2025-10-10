# Reddit Post Scraper 🔥

## 📌 Overview
    This project Fetches post titles, upvotes, and comments from Reddit subreddits. website using Python.  
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
       cd web-scraping-portfolio/Reddit
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python readditcar_scraper.py
    
    4. Output:
        Scraped data → reddit_car_data.csv
          Logs → log.txt

---

## 📊 Sample Output

                                          POST_TITLE                                          POST_LINK POST_DATE POST_UPVOTE        comment
1              What’s happenings with the EV market?  https://www.reddit.com/r/electricvehicles/comm...   2mo ago   245 votes   302 comments
2            Buying an EV is a absolute game changer  https://www.reddit.com/r/electricvehicles/comm...   1mo ago  2.1K votes  1.2K comments
3                  The worst part about owning an EV  https://www.reddit.com/r/electricvehicles/comm...   1mo ago   871 votes   485 comments
4  Update https://www.reddit.com/r/electricvehicl...  https://www.reddit.com/r/electricvehicles/comm...   25d ago      1 vote     4 comments        
    

---
## 📸 Sample Screenshot

<img width="691" height="234" alt="Screenshot 2025-10-07 at 5 21 22 PM" src="https://github.com/user-attachments/assets/870d268c-bd6a-4690-b753-c2822ff7d6e5" />


---
## 📂 Project Structure
      
    Reddit/
      │── readditcar_scraper.py         # Main scraper script
      │── reddit_car_data.csv           # Sample scraped data
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
