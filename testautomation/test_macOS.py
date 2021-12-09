import datetime
import time
import platform

import keyboard
import pytest


from pathlib import Path


platformtype = pytest.mark.skipif(platform.system() == 'Windows' or platform.system() == 'Linux', reason="Mac")
folder_path = str(Path(__file__).parents[0])

timesleepseconds = 3


data = [
{"https://dev1.vantagelabs.co/remote/Lanes-Lost-Chambers/#!/"},
{"https://dev1.vantagelabs.co/remote/Towels/#!/"},
{"http://dev1.vantagelabs.co/Vantage-Turnstile/#!/"}
]




@platformtype
@pytest.mark.parametrize('urlinput', data)
def test_LoginManual(urlinput):
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    desired_cap = {}
    driver = webdriver.Edge("./msedgedriver", capabilities=desired_cap)

    strurlinput = "".join(urlinput)
    print("urlStringtoTest", strurlinput)

    driver.get(strurlinput)
    current_url = driver.current_url
    element = driver.find_element_by_css_selector('input[ng-model="formData.username"]')
    element.clear()
    element.send_keys("tester")
    time.sleep(timesleepseconds)
    element = driver.find_element_by_css_selector('input[ng-model="formData.password"]')
    element.clear()
    element.send_keys("password")
    time.sleep(timesleepseconds)
    dts = datetime.datetime.now().strftime("%Y_%m_%d_%I%M%S%p")
    driver.save_screenshot("./results/loginImg_" + dts + ".png")


    info = driver.find_element_by_css_selector('.version.ng-binding')
    print("Version Tested: ", info.text)

    info = driver.find_element_by_css_selector('.header1.v810-abs-pos')
    print("Title Tested: ", info.text)


    element = driver.find_element_by_class_name("primary-button")
    element.click()
    # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 5).until(EC.url_changes(current_url))
    new_url = driver.current_url
    print(driver.title)
    scannediawindow = driver.window_handles
    print(scannediawindow)
    print(new_url)
    time.sleep(timesleepseconds)
    driver.save_screenshot("./results/loginCompleted" + dts + ".png")
    time.sleep(timesleepseconds)



    try:
        info = driver.find_element_by_css_selector('.v810-abs-pos.user-header.ng-binding')
        print("Tester: ", info.text)
    except:
        pass

    try:
        info = driver.find_element_by_css_selector('.header1.v810-abs-pos.center') #Towel
        print("Tester: ", info.text)
    except:
        pass

    element = driver.find_element_by_class_name("primary-button")
    element.click()
    # wait for URL to change with 15 seconds timeout
    new_url = driver.current_url
    print(driver.title)
    scannediawindow = driver.window_handles
    print(scannediawindow)
    print(new_url)
    time.sleep(timesleepseconds)
    driver.save_screenshot("./results/logoutCompleted" + dts + ".png")
    time.sleep(timesleepseconds)

    driver.close()

@pytest.mark.parametrize('urlinput', data)
def test_logout(urlinput):
    from selenium import webdriver
    from selenium.webdriver.common import keys
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    desired_cap = {}
    driver = webdriver.Edge("./msedgedriver", capabilities=desired_cap)
    strurlinput = "".join(urlinput)
    print("urlStringtoTest", strurlinput)
    driver.get(strurlinput)
    current_url = driver.current_url

    print("Page Title", driver.title)

    element = driver.find_element_by_css_selector('input[ng-model="formData.username"]')


    element.clear()
    element.send_keys("tester")
    time.sleep(timesleepseconds)
    element = driver.find_element_by_css_selector('input[ng-model="formData.password"]')
    element.clear()
    element.send_keys("password")
    time.sleep(timesleepseconds)
    dts = datetime.datetime.now().strftime("%Y_%m_%d_%I%M%S%p")
    driver.save_screenshot("./results/loginImg_" + dts + ".png")

    element = driver.find_element_by_class_name("primary-button")
    element.click()
    # wait for URL to change with 15 seconds timeout
    WebDriverWait(driver, 5).until(EC.url_changes(current_url))
    new_url = driver.current_url
    print(driver.title)
    scannediawindow = driver.window_handles
    print(scannediawindow)
    print(new_url)
    time.sleep(timesleepseconds)
    driver.save_screenshot("./results/loginCompleted" + dts + ".png")
    time.sleep(timesleepseconds)

    element = driver.find_element_by_class_name("primary-button")
    element.click()
    # wait for URL to change with 15 seconds timeout
    new_url = driver.current_url
    print(driver.title)
    scannediawindow = driver.window_handles
    print(scannediawindow)
    print(new_url)
    time.sleep(timesleepseconds)
    driver.save_screenshot("./results/logoutCompleted" + dts + ".png")
    time.sleep(timesleepseconds)
    driver.save_screenshot("./results/Logout" + dts + ".png")
    driver.close()

@pytest.mark.parametrize('urlinput', data)
def test_getPageDimension(urlinput):
    from selenium import webdriver
    desired_cap = {}
    driver = webdriver.Edge("./msedgedriver", capabilities=desired_cap)
    strurlinput = "".join(urlinput)
    print("urlStringtoTest", strurlinput)
    driver.get(strurlinput)
    driver.maximize_window()
    intheight = driver.execute_script("return document.body.scrollHeight")
    intwidth = driver.execute_script("return document.body.scrollWidth")

    print("Page Height and Width for ", strurlinput, " H x W ",  intheight, intwidth)
    driver.close()



