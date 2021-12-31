import time
from selenium import webdriver
from selenium.webdriver.common.by import By

LINKEDIN_EMAIL = "YOUR_USERNAME"
LINKEDIN_PASSWORD = "YOUR_PASSWORD"
LINKEDIN_URL_LOGIN = "https://www.linkedin.com/login/"
LINKEDIN_URL_NETWORK = "https://www.linkedin.com/mynetwork/invitation-manager/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)

def login(url):
    driver.get(url)
    username = driver.find_element(By.ID, 'username')
    username.send_keys(LINKEDIN_EMAIL)
    password = driver.find_element(By.ID, 'password')
    password.send_keys(LINKEDIN_PASSWORD)
    loginBtn = driver.find_element(By.XPATH, '//*[@type="submit"]')
    loginBtn.click()
    print("Successfully logged in !")

def go_to_networkpage(url):
    driver.get(url)
    print("Redirecting to your Network Manager ...")

def acceptinvites():
    try:
        list_btn=driver.find_element(By.CLASS_NAME, "invitation-card__action-btn")
        for btn in list_btn:
            btn_click=btn.get_attribute("aria-label")
            if btn_click[0:10]=="Accept":
                btn.click()
        print("All invites accepted !")
    except:
        print("There is not invites pending !")
    
def main():
    login(LINKEDIN_URL_LOGIN)
    go_to_networkpage(LINKEDIN_URL_NETWORK)    
    time.sleep(5)
    acceptinvites()

main()