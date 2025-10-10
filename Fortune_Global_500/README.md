# Fortune Global 500 Scraper 🌍

## 📌 Overview
    This project Collects company rankings and details from the Fortune Global 500 list. website using Python.  
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
       cd web-scraping-portfolio/Fortune_Global_500
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python wikipedia_scraper.py 
    
    4. Output:
        Scraped data → fortune500_data.csv
          Logs → log.txt

---

## 📊 Sample Output

                                                Name                        Industry  ...      Employees         Country
    Rank                                                                           ...                               
    1                                     Walmart                          Retail  ...      2,100,000   United States
    2                                      Amazon  Retail\ninformation technology  ...      1,556,000                
    3             State Grid Corporation of China                     Electricity  ...      1,361,423           China
    4                                Saudi Aramco                     Oil and gas  ...         73,311    Saudi Arabia

---
## 📸 Sample Screenshot

<img width="605" height="455" alt="Screenshot 2025-10-07 at 5 16 45 PM" src="https://github.com/user-attachments/assets/3e8b49cb-78d4-47a4-9a66-19166fe9f4bd" />


---
## 📂 Project Structure
      
    Fortune_Global_500/
      │── wikipedia_scraper.py       # Main scraper script
      │── fortune500_data.csv        # Sample scraped data
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
