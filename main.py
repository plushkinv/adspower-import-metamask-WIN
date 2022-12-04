from typing import KeysView
import requests, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from termcolor import cprint
import pyperclip

def add_network(driver, name_network):
    try:
        networks = {
            'Optimism' : {
            'net_name': 'Optimism',
            'rpc': 'https://mainnet.optimism.io',
            'chain_id': 10,
            'symbol': 'ETH',
            'explorer': 'https://optimistic.etherscan.io/',
            },

            'Arbitrum' : {
            'net_name': 'Arbitrum One',
            'rpc': 'https://arb1.arbitrum.io/rpc',
            'chain_id': 42161,
            'symbol': 'ETH',
            'explorer': 'https://arbiscan.io/',
            },

            'BSC' : {
            'net_name': 'Smart Chain',
            'rpc': 'https://bsc-dataseed.binance.org/',
            'chain_id': 56,
            'symbol': 'BNB',
            'explorer': 'https://bscscan.com',
            },
            
            'Polygon' : {
            'net_name': 'Polygon',
            'rpc': 'https://polygon-rpc.com',
            'chain_id': 137,
            'symbol': 'MATIC',
            'explorer': 'https://polygonscan.com/',
            },
        }

        xpatch = '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div'

        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network')
        
        wait_elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f'{xpatch}[1]/label/input')))

        text = networks[name_network]['net_name']
        net_name = driver.find_element(By.XPATH, f'{xpatch}[1]/label/input').send_keys(text)

        text = networks[name_network]['rpc']
        new_rpc = driver.find_element(By.XPATH, f'{xpatch}[2]/label/input').send_keys(text)

        text = networks[name_network]['chain_id']
        chain = driver.find_element(By.XPATH, f'{xpatch}[3]/label/input').send_keys(text)

        
        text = networks[name_network]['symbol']
        currency_symbol = driver.find_element(By.XPATH, f'{xpatch}[4]/label/input').send_keys(text)

        
        text = networks[name_network]['explorer']
        explorer = driver.find_element(By.XPATH, f'{xpatch}[5]/label/input').send_keys(text)
        time.sleep(1)

        save = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary"]').click()
        time.sleep(2)

        ok = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary"]').click()
        time.sleep(2)

    except:
        cprint(f'network < {name_network} > is already add', 'white')


def main(zero, ads_id, seed, password):
    try:
     
        open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id
        close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id

        resp = requests.get(open_url).json()

        chrome_driver = resp["data"]["webdriver"]
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        driver = webdriver.Chrome(chrome_driver, options=chrome_options)

        url = 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html'

        driver.get(url)
        driver.switch_to.window(driver.window_handles[-1])
        wait_elem = WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, '//*[@class="button btn--rounded btn-primary first-time-flow__button"]')))
        get_started = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary first-time-flow__button"]').click()
        wait_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@class="button btn--rounded btn-secondary page-container__footer-button"]')))
        get_started2 = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-secondary page-container__footer-button"]').click()        
        wait_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@class="button btn--rounded btn-primary first-time-flow__button"]')))
        import_wallet = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary first-time-flow__button"]').click()
        
        wait_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@class="MuiInputBase-input MuiInput-input"]')))
        pyperclip.copy(seed)
        phrase = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-0"]').click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        wait_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
        pyperclip.copy(password)
        new_password = driver.find_element(By.XPATH, '//*[@id="password"]').click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        password_confirm = driver.find_element(By.XPATH, '//*[@id="confirm-password"]').click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        agree_terms = driver.find_element(By.XPATH, '//*[@class="check-box far fa-square"]').click()

        wait_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@class="button btn--rounded btn-primary create-new-vault__submit-button"]')))
        done_import = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary create-new-vault__submit-button"]').click()

        wait_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@class="button btn--rounded btn-primary first-time-flow__button"]')))
        all_done = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary first-time-flow__button"]').click()

        # =================================== if you don't need to add a networks, delete everything below ===================================
        wait_elem = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//*[@class="currency-display-component__suffix"]')))
        add_network(driver, 'BSC')
        add_network(driver, 'Polygon')
        add_network(driver, 'Optimism')
        add_network(driver, 'Arbitrum')
        # ===================================================================================================================================

        driver.quit()
        requests.get(close_url)

        cprint(f'{zero+1}. {ads_id} = done', 'green')

    except Exception as ex:
        cprint(f'{zero+1}. {ads_id} = already done', 'yellow')
        driver.quit()
        requests.get(close_url)


with open("C://Python/adspower-import-metamask-main/id_users.txt", "r") as f:
    id_users = [row.strip() for row in f]

with open("C://Python/adspower-import-metamask-main/seeds.txt", "r") as f:
    seeds = [row.strip() for row in f]
        
zero = -1
for ads_id in id_users:
    zero = zero + 1
    seed = seeds[zero]
    password = 'password123' # password for metamask

    main(zero, ads_id, seed, password)

