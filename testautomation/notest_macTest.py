import datetime
import time
import platform

import keyboard
import pytest


from pathlib import Path

from selenium.webdriver import ActionChains, Keys

platformtype = pytest.mark.skipif(platform.system() == 'Windows' or platform.system() == 'Linux', reason="Mac")
folder_path = str(Path(__file__).parents[0])

@platformtype
def test_TowelsLoginMediaScanLogout():
    from selenium import webdriver
    from selenium.webdriver.common import keys
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
    driver.save_screenshot("./results/loginImg_" + dts + ".png")
    element = driver.find_elements_by_xpath("/html/body/div/login/div/div[3]/div[8]/button")[0]
    element.click()
    # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))
    new_url = driver.current_url
    print(driver.title)
    scannediawindow = driver.window_handles
    print(scannediawindow)
    print(new_url)
    time.sleep(5)


    driver.save_screenshot("./results/scanMedia_" + dts + ".png")

    print("Send Keyboard Event")
    #keyboard.write("04 13 03 7a 83 50 85")
    keyboard.write("")
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(1)
    driver.save_screenshot("./results/scanMedia_" + dts + ".png")
    element = driver.find_element_by_tag_name('body')
    element.send_keys("04 ac 0d 7a 83 50 84")
    time.sleep(1)
    print('sending ', 'enter')
    element.send_keys(keys.Keys.ENTER)
    driver.save_screenshot("./results/scanMedia_" + dts + ".png")
    time.sleep(2)

    #Guest Information Page
    #/html/body/div/hotel-guests/div/div[7]/button
    driver.save_screenshot("./results/hotelguestsPage_" + dts + ".png")
    element = driver.find_elements_by_xpath("/html/body/div/hotel-guests/div/div[7]/button")[0]
    element.click()
    time.sleep(2)

    #Get Two Towel
    #/html/body/div/issue-towels/div/div[7]/button
    element = driver.find_elements_by_xpath("/html/body/div/issue-towels/div/div[7]/button")[0]
    element.click()
    element = driver.find_elements_by_xpath("/html/body/div/issue-towels/div/div[7]/button")[0]
    element.click()

    time.sleep(3)


    #/html/driver.save_screenshot("./results/towelAssign2Pieces" + dts + ".png")body/div/issue-towels/div/div[15]/button
    element = driver.find_elements_by_xpath("/html/body/div/issue-towels/div/div[15]/button")[0]
    element.click()
    time.sleep(3)

    #Logout
    driver.save_screenshot("./results/towelAssignedLogout" + dts + ".png")
    element = driver.find_elements_by_xpath("/html/body/div/scan-band/div/div[7]/button")[0]
    element.click()
    time.sleep(2)

    driver.save_screenshot("./results/Logout" + dts + ".png")
    #/html/body/div/scan-band/div/div[7]/button

    # #Wrong Scan media
    # time.sleep(5)
    # driver.save_screenshot("./results/wrongscanMedia_" + dts + ".png")
    # # exit Button
    # time.sleep(5)
    # element = driver.find_elements_by_xpath("/html/body/div/scan-band/div/div[7]/button")[0]
    # element.click()



    #time.sleep(2)
    #driver.save_screenshot("./results/logoutSuccessful_" + dts + ".png")
    #time.sleep(1)
    driver.close()



