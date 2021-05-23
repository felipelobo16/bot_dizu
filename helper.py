from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time, random

green = "\033[1;32m"
red = "\033[1;31m"
blue = "\033[1;34m"
white = "\033[1;97m"


def relogio(segundos):
    print('')
    for i in range(segundos, 0, -1):
        time.sleep(1)
        timer = red + str(i) + white
        print('%s....' % timer, end='\r')

def browser(head):
    agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.78 Safari/537.36',
        'Mozilla/5.0(X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4324.192 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4324.192 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4324.192 Safari/537.36']
    r1 = random.randrange(len(agent)) - 1
    chrome_options = Options()
    chrome_options.headless = head
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--mute-audio')
    chrome_options.add_argument(f'user-agent={agent[r1]}')
    PATH = "chromedriver"
    driver = webdriver.Chrome(PATH, options=chrome_options)
    # print(branco+f"Agent:" + azul + f"{agent[r1]}" + branco)
    driver.get('https://www.google.com')
    print(white)
    return driver
