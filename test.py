from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# Define options for the Android device and application
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "11"  # api level
options.device_name = "emulator-5554"  # device id
options.app = "D:\\m_project\\AutomationAppiumPython\\ShudokkhoAutomation\\Shudokkho_QA_Debug_1.9.6.apk"  # Path to your APK
options.no_reset = True  # Optional, prevents resetting the app on each run

# Start the driver
driver = webdriver.Remote(command_executor="http://localhost:4723", options=options)
time.sleep(5)
print("App launched successfully on Android Emulator!")
driver.quit()
# --- closure: the app should be launched in the emulator