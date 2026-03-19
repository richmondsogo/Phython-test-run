from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get("https://the-internet.herokuapp.com/dynamic_controls")


assert 'The Internet' in browser.title


assert 'Enable' in browser.page_source


try:
    # Locate and click the "Enable" button
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='swapInput()']"))
    )
    button.click()
    print("Button clicked!")

    # Wait for the input to be enabled
    time.sleep(2)

    # get the inner html of input tag
    elements = browser.find_element(By.ID, "input-example")
    a = elements.get_attribute('innerHTML')
    print(a)

    # Find and interact with the text input
    text_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div/div[1]/form[2]/input")
        )
    )
    browser.execute_script("arguments[0].removeAttribute('disabled')", text_input)
    text_input.send_keys("basic")
    print("Text entered!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(2)
    browser.quit()
