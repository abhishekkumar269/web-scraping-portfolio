
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time

# gecko_driver_path = r"/Users/abhishekkumar/Desktop/web_scrapping_project/ambitionbox.com/chromedriver.exe"

# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.202 Safari/537.36")

# service = Service(executable_path=gecko_driver_path)
# driver = None

# try :
    
#     driver = webdriver.Chrome(service=service,options=options)

#     url ='https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav'

#     driver.get(url)
#     time.sleep(3)

# except Exception as e:
#     print(e)


# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# import time

# gecko_driver_path = r"/Users/abhishekkumar/Desktop/web_scrapping_project/ambitionbox.com/geckodriver"

# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0")

# service = Service(executable_path=gecko_driver_path)
# driver = None

# try:
#     driver = webdriver.Firefox(service=service, options=options)
#     url = 'https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav'
#     driver.get(url)
#     time.sleep(3)
#     print(driver.page_source[:500])  # optional: preview page content
# except Exception as e:
#     print("Error:", e)
# finally:
#     if driver:
#         driver.quit()


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# ✅ Path to geckodriver (NO .exe on macOS)
gecko_driver_path = "/Users/abhishekkumar/Desktop/web_scrapping_project/ambitionbox.com/geckodriver"

# ✅ Firefox options
options = Options()
options.add_argument("--headless")
options.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:138.0) Gecko/20100101 Firefox/138.0")

# ✅ Create service and driver
service = Service(executable_path=gecko_driver_path)
driver = None

try:
    driver = webdriver.Firefox(service=service, options=options)
    url = 'https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav'
    driver.get(url)
    time.sleep(5)  # wait for JS content
    print(driver.page_source[:500])  # preview HTML
except Exception as e:
    print("Error:", e)
finally:
    if driver:
        driver.quit()