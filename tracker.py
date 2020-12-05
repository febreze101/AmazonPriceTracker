from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import smtplib

PATH = "C:\Program Files (x86)\chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_argument('headless') # run without opening browser
driver = webdriver.Chrome(PATH, options=option) # shows what browser to use and location of driver

# check if price has lowered
def amazon_tracker(item: str, now:float, URL: str):
    # Go to the page
    driver.get(URL)

    driver.implicitly_wait(5)
    # get the price
    price = driver.find_element_by_id("priceblock_ourprice").text
    price_newest = float(price[1:7])

    # check if price lowered
    if(price_newest < now):
        send_email(URL, item)

    driver.quit()

# function to send mail
def send_email(URL: str, item):
    # set up a server to send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("xfabro14@gmail.com", 'dxmftzoywsnudljj')

    subject = "The " + item +" price has lowered!"
    body = "Check this link: " + URL

    msg = f"Subject: {subject} \n\n{body}"

    server.sendmail(
        'xfabro14@gmail.com',
        'fkbokovi@gmail.com',
        msg
    )

    server.quit()
