# AmbitionBox Company Reviews Scraper 💼
## 📌 Overview
    This project Collects company reviews, ratings, and salary data from AmbitionBox. website using Python.  
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
       cd web-scraping-portfolio/AmbitionBox
    
    2. Install dependencies:
        pip install -r requirements.txt
    
    3. Run the scraper:
        python ambition_scraper.py
    
    4. Output:
        Scraped data → company_details.csv
        Logs → log.txt

---

## 📊 Sample Output

[                      NAME REVIEW NO_OF_PEOPLE_RATINGS              COMAPANY TYPE                              COMANY_HEADQUARTES
0                      TCS    3.4                 (1L)  IT Services & Consulting       Bangalore / Bengaluru +423 other locations
1                Accenture    3.7              (66.9k)  IT Services & Consulting       Bangalore / Bengaluru +236 other locations
2                    Wipro    3.7                (60k)  IT Services & Consulting       Bangalore / Bengaluru +363 other locations
3                Cognizant    3.7                (57k)  IT Services & Consulting    Hyderabad / Secunderabad +220 other locations

---
## 📸 Sample Screenshot

<img width="842" height="312" alt="Screenshot 2025-10-07 at 6 06 12 PM" src="https://github.com/user-attachments/assets/fbc3e162-fd06-416c-87e2-bd2bab3d2ef9" />


---
## 📂 Project Structure
      
    AmbitionBox/
      │── ambition_scraper.py       # Main scraper script
      │── company_details.csv       # Sample scraped data
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
