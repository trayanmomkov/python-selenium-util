from time import sleep

from selenium.webdriver.common.keys import Keys

import selenium_util

if __name__ == '__main__':
    driver = selenium_util.init('Firefox')
    driver.get('https://www.wikipedia.org/')
    sleep(1)
    selenium_util.find_first_input(driver).send_keys('Slovio' + Keys.RETURN)
