import pandas as pd
from selenium import webdriver
import time

def fill_form():
    # read the data
    data = pd.read_csv('../wallet.csv')
    recycle = data.shape[0]
    
    # define webdriver
    driver = webdriver.Chrome(executable_path='directory webdrivermu')
    
    # define the XPaths of the radio buttons
    radio_button_xpaths = [
        '//*[@id="i15"]/div[3]/div',
        '//*[@id="i25"]/div[3]/div',
        '//*[@id="i44"]/div[3]/div',
        '//*[@id="i60"]/div[3]/div',
        '//*[@id="i82"]/div[3]/div',
        '//*[@id="i95"]/div[3]/div',
        '//*[@id="i108"]/div[3]/div',
    ]

    # loop over the rows
    for i in range(recycle):
        print(i)
        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeEU-k4UpVquAue374i3RPbsdCF2KM5Kz_q-nYG_IBr-C87DQ/viewform')
        time.sleep(1)
        
        # fill in the wallet address
        wallet_address = data.iloc[i]['wallet_address']
        input_wallet = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        for j in wallet_address:
            input_wallet.send_keys(j)
            time.sleep(0.1)
        
        # loop over the radio buttons and click them with a delay
        for xpath in radio_button_xpaths:
            radio_buttons = driver.find_elements("xpath", xpath)
            for button in radio_buttons:
                button.click()
                time.sleep(0.1)
        
        # submit the form
        submit = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit.click()
        time.sleep(1)
        
    driver.quit()


if __name__ == '__main__':
    fill_form()
