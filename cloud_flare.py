import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By

uc_options = uc.ChromeOptions()
uc_options.headless = False
driver = uc.Chrome(options=uc_options)

driver.execute_script(
    f"window.open('https://community.cloudflare.com/t/how-to-check-my-website-is-using-cloudflare/183049?__cf_chl_rt_tk=_5epmX8MTiQYIca6h4d9WDoBl0vRtPEGB..Vj1sbQ_Y-1708633550-0.0-3943"
    f"&pageSize=15&businessId=881071&bbbId=1116&sort=reviewDate%20desc,%20id%20desc', '_blank');")
time.sleep(20)

driver.switch_to.window(driver.window_handles[1])

# Wait for 5 seconds (optional)
time.sleep(5)

# Switch back to the first window
driver.switch_to.window(driver.window_handles[0])
time.sleep(7)
# Close the first window handle
driver.close()






# Wait for 10 seconds after closing the first window
time.sleep(10)

# Switch to the second window
driver.switch_to.window(driver.window_handles[0])

time.sleep(5)









