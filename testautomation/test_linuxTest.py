import datetime
import time
import platform
import pytest
import pytest_html
from pytest_html import extras

import os
from pathlib import Path

platformtype = pytest.mark.skipif(platform.system() == 'Darwin' or platform.system() == 'Windows', reason="Linux")
folder_path = str(Path(__file__).parents[0])

@platformtype
def test_TowelsLoginMediaScanLogout():
    from selenium import webdriver
    from selenium.webdriver.common import keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    desired_cap = {}
    driver = webdriver.Edge("./msedgedriver", capabilities=desired_cap)
    driver.get("https://dev1.vantagelabs.co/remote/Towels/#!/")

    current_url = driver.current_url

    element = driver.find_elements_by_xpath("/html/body/div/login/div/div[3]/div[5]/input")[0]
    element.clear()
    element.send_keys("tester")

    time.sleep(1)

    element = driver.find_elements_by_xpath("/html/body/div/login/div/div[3]/div[6]/input")[0]
    element.clear()
    element.send_keys("password")

    time.sleep(1)
    dts = datetime.datetime.now().strftime("%Y_%m_%d_%I%M%S%p")

    driver.save_screenshot("./results/loginImg.png_" + dts + ".png")

    extras.image("./results/loginImg.png")

    element = driver.find_elements_by_xpath("/html/body/div/login/div/div[3]/div[8]/button")[0]
    element.click()

    # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))
    new_url = driver.current_url
    print(new_url)
    time.sleep(2)

    print('Insert to Body')
    driver.save_screenshot("./results/scanMedia_" + dts + ".png")

    #import keyboard
    #keyboard.write('048B0F7A835084')
    #keyboard.press_and_release('enter')

    element = driver.find_element_by_tag_name("body")
    element.send_keys("048B0F7A835084")
    element.send_keys(keys.Keys.ENTER)
    time.sleep(2)
    driver.save_screenshot("./results/wrongscanMedia_" + dts + ".png")

    #exit Button
    time.sleep(5)
    element = driver.find_elements_by_xpath("/html/body/div/scan-band/div/div[7]/button")[0]
    element.click()

    time.sleep(2)
    driver.save_screenshot("./results/logoutSuccessful_" + dts + ".png")


    time.sleep(1)

    driver.close()

 #keyboard.write('048B0F7A835084')

    # keyboard.write("0")
    # time.sleep(1)
    # keyboard.write("4")
    # time.sleep(1)
    # keyboard.write("8")
    # time.sleep(1)
    # keyboard.write("b")
    # time.sleep(1)
    # keyboard.write("0")
    # time.sleep(1)
    # keyboard.write("f")
    # time.sleep(1)
    # keyboard.write("7")
    # time.sleep(1)
    # keyboard.write("a")
    # time.sleep(1)
    # keyboard.write("8")
    # time.sleep(1)
    # keyboard.write("3")
    # time.sleep(1)
    # keyboard.write("5")
    # time.sleep(1)
    # keyboard.write("0")
    # time.sleep(1)
    # keyboard.write("8")
    # time.sleep(1)
    # keyboard.write("4")
    # time.sleep(1)

    #keyboard.press_and_release('enter')




    # element = driver.find_element_by_xpath("//body")
    # element.send_keys("0")
    # time.sleep(1)
    # element.send_keys("4")
    # time.sleep(1)
    # element.send_keys("8")
    # time.sleep(1)
    # element.send_keys("b")
    # time.sleep(1)
    # element.send_keys("0")
    # time.sleep(1)
    # element.send_keys("f")
    # time.sleep(1)
    # element.send_keys("7")
    # time.sleep(1)
    # element.send_keys("a")
    # time.sleep(1)
    # element.send_keys("8")
    # time.sleep(1)
    # element.send_keys("3")
    # time.sleep(1)
    # element.send_keys("5")
    # time.sleep(1)
    # element.send_keys("0")
    # time.sleep(1)
    # element.send_keys("8")
    # time.sleep(1)
    # element.send_keys("4")
    # time.sleep(1)
    #element.send_keys(keys.Keys.RETURN)

