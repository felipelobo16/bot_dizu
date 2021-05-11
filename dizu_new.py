from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, random, sys
import helper

green = "\033[1;32m"
red = "\033[1;31m"
blue = "\033[1;34m"
white = "\033[1;97m"

def starter(browser,login,senha):
    login_dizu = #login_dizu
    senha_dizu = #senhadizu
    print(f"[+] COMEÇANDO BOT {blue}DIZU{white} LIKES + FOLLOWS")
    browser.get('https://dizu.com.br/login')
    time.sleep(3)
    action = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'login')))
    action.send_keys(login_dizu)
    action = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'senha')))
    action.send_keys(senha_dizu)
    action = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//body/div[1]/section[1]/form[1]/div[5]/button[1]')))
    action.click()
    time.sleep(1)
    print(f"[+] {green}LOGADO COM SUCESSO NO DIZU{white}")
    try: #--LOGIN INTAGRAM
        print(f"[!] CONTA:{blue}{login}{white}")
        browser.execute_script("window.open('https://www.instagram.com/')")
        browser.switch_to.window(browser.window_handles[1])
        action = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.NAME, 'username')))
        action.send_keys(login)
        browser.find_element_by_name('password').send_keys(senha)
        time.sleep(2)
        browser.find_element_by_xpath("//button[@type='submit']").click()
        try:
            action = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='react-root']/section[1]/nav[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/*[1]")))
            action.click()
        except:
            print(f"\n{red}[!] POSSIVEL BLOCK [!]{white}")
            print(f"{red}[!] PRINT SALVO [!]{white}")
            browser.save_screenshot(f'log/block/{login}.png')
            browser.quit()
        try:
            action = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//button[text()='Not Now']")))
            action.click()
        except:
            browser.switch_to.window(browser.window_handles[0])
            print(f"[+] {green}INSTAGRAM LOGADO COM SUCESSO{white}")
    except Exception:
        print(f"\n{red}[!] INSTAGRAM LOGIN ERROR [!]{white}")
        browser.quit()

def pre_bot(login, browser):
    time.sleep(3)
    browser.switch_to.window(browser.window_handles[0])
    foi = False
    count = 0
    while foi == False and count < 3:
        try:
            browser.get('https://dizu.com.br/painel/conectar')
            time.sleep(5)
            action = browser.find_element_by_xpath(f"//option[contains(text(),'{login}')]")
            action.click()
            action = browser.find_element_by_xpath(f"//input[@id='curtida05']")
            action.click()
            time.sleep(1)
            action = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, "//button[@id='iniciarTarefas']")))
            action.click()
            foi = True
        except Exception:
            count += 1
            print(f'\n{red}[!] ERRO PRE BOT REINICIANDO...[!]{white}')
            browser.quit()
            browser = helper.browser(headless)
            starter(browser, login, senha)

def stories(driver, timeout):
    foi = False
    count = 0
    driver.switch_to.window(driver.window_handles[1])
    action = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//body/div[@id='react-root']/section[1]/nav[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/*[1]")))
    action.click()
    while foi == False and count < 5:
        count += 1
        try:
            view = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f"//body/div[@id='react-root']/section[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[{5+count}]/div[1]/button[1]")))
            view.click()
            time.sleep(60)
            action = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//body/div[@id='react-root']/section[1]/div[3]/button[1]")))
            action.click()
            foi = True
        except Exception as e:
            print(f"{red}[!] ERRO STORIES, RESTART [!]{white}")
            timeout += 1

def bot_engine(login, browser, MAX_FOLLOWERS, MAX_LIKES, FOLLOW_DELAY, FOLLOW_PLUS):
    follows = 0
    likes = 0
    view_stories = 0
    jumps = 0
    timeout = 0
    loops = 1
    ultimo = ''
    soft = 0

    print(f'[!] FOLLOW DELAY:{red}{FOLLOW_DELAY}{white} Loops')
    print(f'[!] FOLLOWS:[{blue}{MAX_FOLLOWERS}{red}{white}+{red}[{FOLLOW_PLUS}]{white}]')
    print(f'[!] LIKES:[{blue}{MAX_LIKES}{white}]')
    print(f'[+] BOT:{green}INICIOU{white}')
    print('')

    def painel(timer):
        var1 = "Ultimo:" + blue + ultimo + white
        var2 = "Likes:" + green + str(likes) + white
        var3 = "Follows:" + green + str(follows) + white
        var4 = "Loops:" + blue + str(loops) + white
        var5 = "Timeout:" + red + str(timeout) + white
        var6 = "Stories:" + blue + str(view_stories) + white
        var7 = "Jumps:" + red + str(jumps) + white
        timer = int(time.time() - timer)
        var = f"[!] {var1:>15} -{var2}|{var3}|{var4}|{var5}|{var6}|{var7}|Timer: {green}{timer}{white}"
        sys.stdout.write(f'\r{var}')

    while (likes+follows) < (MAX_LIKES + MAX_FOLLOWERS) and loops < 1000 and timeout < 30:
        timer = time.time()
        try:
            if loops % 20 == 0:
                time.sleep(1)
                stories(browser, timeout)
                time.sleep(1)
                pre_bot(login, browser)
                view_stories += 1
            if loops % FOLLOW_DELAY == 0 and loops < 1000:
                MAX_FOLLOWERS += FOLLOW_PLUS
            url = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "conectar_step_4"))).get_attribute('href')
            page = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "conectar_step_4"))).get_attribute('href').split('/')[-1]
            action = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "conectar_step_4")))
            action.click()
            browser.switch_to.window(browser.window_handles[2])
            letters = ''
            if '/p/' in url:
                person = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//header/div[2]/div[1]/div[1]/span[1]/a[1]'))).get_attribute('href').split('/')[-2]
                browser.close()
                browser.switch_to.window(browser.window_handles[1])
                action = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
                for letters in person.strip(''):
                    time.sleep(.2)
                    action.send_keys(letters)
                action = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, f"//div[contains(text(),'{person}')]")))
                action.click()
                scrolls = random.randrange(1,3)
                while scrolls > 0:
                    scrolls -= 1
                    browser.execute_script("window.scrollBy(0,500)", "")
                    time.sleep(3)
                    if scrolls == 1:
                        browser.execute_script("window.scrollBy(700,0)", "")
                browser.get(url)
                time.sleep(random.randrange(3, 5))
                action = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH,"//body/div[@id='react-root']/section[1]/main[1]/div[1]/div[1]/article[1]/div[3]/section[1]/span[1]/button[1]/div[1]/span[1]/*[@aria-label='Curtir']")))
                action.click()
                time.sleep(1)
                browser.save_screenshot(f'log/action/{login}.png')
                time.sleep(1)
                ultimo = blue + 'LIKE' + white
            else:
                browser.close()
                browser.switch_to.window(browser.window_handles[1])
                action = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
                for letters in page.strip(''):
                    time.sleep(.2)
                    action.send_keys(letters)
                action = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, f"//div[contains(text(),'{page}')]")))
                action.click()
                if MAX_FOLLOWERS > follows:
                    try:
                        time.sleep(random.randrange(4,7))
                        action = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Seguir")]')))
                        time.sleep(random.randrange(4, 7))
                        action.click()
                        time.sleep(1)
                        browser.save_screenshot(f'log/action/{login}.png')
                        time.sleep(1)
                        scrolls = random.randrange(2, 5)
                        while scrolls > 0:
                            scrolls -= 1
                            browser.execute_script("window.scrollBy(0,500)", "")
                            time.sleep(3)
                            if scrolls == 1:
                                browser.execute_script("window.scrollBy(700,0)", "")
                    except:
                        try:
                            time.sleep(1)
                            browser.find_element_by_xpath('//button[contains(text(), "Message")]')
                        except:pass
                    time.sleep(random.randrange(20,25))
                    ultimo = blue + 'FOLLOW' + white
                else:
                    pass
            person = None
            page = None
            url = None
            check = None
            try:
                browser.find_element_by_xpath('//a[contains(text(),"Forgot password?")]')
                check = 'Forgot password'
            except:
                pass
            try:
                browser.find_element_by_xpath('//*[contains(text(),"We\'ve detected suspicious activity on your")]')
                check = 'We\'ve detected suspicious activity on your'
            except:
                pass
            try:
                browser.find_element_by_xpath('//div[contains(text(),"Change your password to continue using")]')
                check = 'Change your password to continue using'
            except:
                pass
            try:
                browser.find_element_by_xpath(
                    "//div[contains(text(),'Your account has been temporarily blocked from')]")
                check = 'Your account has been temporarily blocked from'
            except:
                pass
            try:
                browser.find_element_by_xpath(
                    "//div[contains(text(),'We will send a confirmation code via SMS to your')]")
                check = 'We will send a confirmation code via SMS to your'
            except:
                pass
            try:
                browser.find_element_by_xpath('//*[contains(text(), "We noticed unusual activity from your account")]')
                check = 'We noticed unusual activity from your account'
            except:
                pass
            try:
                if soft < 1:
                    browser.find_element_by_xpath("//*[contains(text(), 'We restrict certain activity to protect our community')]")
                    print(f"\n{red}[!] SOFT [!]")
                    print(f"{green}[!] RESTART... [!]{white}")
                    time.sleep(1)
                    browser.quit()
                    browser = helper.browser(head=headless)
                    starter(browser, login, senha)
                    pre_bot(login, browser)
                    print('')
                    soft += 1
                else:
                    print(f"\n{red}[!] SOFT CONFIRMADO [!]{white}")
                    soft = 0
                    break
            except:
                pass
            if check != None:
                print(f'\n{red}[!] BLOCK: {check} [!]')
                print(f"{green}[!] SCREENSHOT SALVA NA PASTA BLOCK [!]{white}")
                browser.save_screenshot(f'/log/block/{login}.png')
                break
            browser.switch_to.window(browser.window_handles[0])
            if 'LIKE' in ultimo:
                try:
                    confirm = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'confirmar')]")))
                    confirm.click()
                    likes += 1
                    time.sleep(1)
                except:
                    pass
            elif 'FOLLOW' in ultimo:
                if MAX_FOLLOWERS > follows:
                    try:
                        confirm = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'confirmar')]")))
                        confirm.click()
                        follows += 1
                        time.sleep(1)
                    except:
                        pass
                else:
                    try:
                        action = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, "//button[@id='iniciarTarefas']")))
                        action.click()
                        jumps += 1
                        time.sleep(1)
                    except:
                        pass
        except KeyboardInterrupt:
            print(f'{red}[!] STOP!! [!]{white}')
        except TimeoutException or NoSuchElementException:
            timeout += 1
            try:
                action = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, "//button[@id='iniciarTarefas']")))
                action.click()
            except:
                pre_bot(login, browser)
            pass
        loops += 1
        time.sleep(5)
        painel(timer)

if __name__ == '__main__':
    num_contas = input(f'{white}[?] Lista:{red}')
    contas = open(f'contas{num_contas}', 'r')
    headless = True
    MAX_FOLLOWERS = 10
    MAX_LIKES = 50
    FOLLOW_DELAY = 20
    FOLLOW_PLUS = 5
    for info in contas:
        try:
            login = info.strip().split(':')[0]
            senha = info.strip().split(':')[1]
            username = info.strip().split(':')[2]
            start_timer = time.time()
            browser = helper.browser(headless)
            starter(browser,login,senha)
            pre_bot(username, browser)
            print(f"[+] {green}BOT PREPARADO {white}")
            bot_engine(username, browser, MAX_FOLLOWERS, MAX_LIKES, FOLLOW_DELAY, FOLLOW_PLUS)
            browser.quit()
            print(f'\n[+] BOT DUROU {red}{time.time() - start_timer}{white} SEGUNDOS')
            helper.relogio(200)
            print(f'[+] {green}xxxxxx PROXIMA CONTA xxxxxx{white} [+]')
            print('')
        except:
            browser.quit()
            print(f'\n[+] {red}VERIFICAR CONTA [!]{white}')
            print(f'[+] {green}xxxxxx PROXIMA CONTA xxxxxx{white} [+]')
            print('')
