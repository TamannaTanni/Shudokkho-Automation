from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "11"  # Your device's API level
options.device_name = "emulator-5554"  # Your device ID
options.app = "D:\\m_project\\AutomationAppiumPython\\ShudokkhoAutomation\\Shudokkho_QA_Debug_1.9.6.apk"  # Path to your APK
options.no_reset = True  # Ensures app data isn't reset
# options.full_reset = False  # Ensures app isn't reinstalled

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)

# Step 1: Read the CSV file
# csv_file_path = "ai.csv"
# with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
# print(f"Processing service for: {row['Farmer Name']}")

instant_service = driver.find_element("xpath",
                                      '//android.widget.FrameLayout[@resource-id="com.mpower.android.app.lpin.crm:id/cvTreatment"]/android.widget.LinearLayout')
instant_service.click()

type = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '(//android.widget.TextView[@resource-id="android:id/text1"])[1]'))).click()

ai = driver.find_element("xpath",
                         '//android.widget.TextView[@resource-id="android:id/text1" and @text="কৃত্রিম প্রজনন"]')
ai.click()

name = driver.find_element("xpath",
                           '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvNameTreatment"]').send_keys(
    "Karim")
mobile = driver.find_element("xpath",
                             '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvMobileTreatment"]').send_keys(
    "01234567890")
adress = driver.find_element("xpath",
                             '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvAddressTreatment"]').send_keys(
    "test avenue")
animal_secondary = driver.find_element("xpath",
                                       '(//android.widget.TextView[@resource-id="android:id/text1"])[3]').click()
animal_sec_type = driver.find_element("xpath",
                                      '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="গাভী"]').click()
species_dropdown = driver.find_element("xpath",
                                       '(//android.widget.TextView[@resource-id="android:id/text1"])[4]').click()
species = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="দেশী"]'))).click()
animal_age = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '(//android.widget.TextView[@resource-id="android:id/text1"])[5]'))).click()
age_select = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="৪ দাঁত"]'))).click()
animal_color = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '(//android.widget.TextView[@resource-id="android:id/text1"])[6]'))).click()
color_select = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="কালো"]'))).click()
ai_date = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    '//android.widget.TextView[@resource-id="com.mpower.android.app.lpin.crm:id/tvMatingDate"]'))).click()
date_select = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'))).click()
sign_dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '(//android.widget.TextView[@resource-id="android:id/text1"])[7]'))).click()
sign_select = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="হাটুতে দাগ"]'))).click()
failed_ai = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '(//android.widget.TextView[@resource-id="android:id/text1"])[8]'))).click()
failedAI_select = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="২ বার"]'))).click()
bull_species = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="বাছাই করুন"]'))).click()
species_select = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="রেড চিটাগাং"]'))).click()
driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.mpower.android.app.lpin.crm:id/mbSubmitTreatment"))')

time.sleep(2)
blood_percentage = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//android.widget.TextView[@resource-id="android:id/text1"])[5]'))).click()
blood_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="৫০%"]'))).click()
bull_info = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//android.widget.TextView[@resource-id="android:id/text1"])[6]'))).click()
info_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="লিখুন"]'))).click()
bull_id = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etBullId"]'))).send_keys(
    "redctg_1")
bull_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etBullName"]'))).send_keys(
    "redbull")
bull_price = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etBullPrice"]'))).send_keys(
    "1200")
animal_number = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//android.widget.TextView[@resource-id="android:id/text1"])[7]'))).click()
number_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="৬ - ১০"]'))).click()

camera = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.ImageButton[@resource-id="com.mpower.android.app.lpin.crm:id/acibCameraProfile"]')
    )
).click()
shutter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.ImageView[@content-desc="Shutter"]')
    )
).click()
picture_confirm = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.ImageButton[@content-desc="Done"]')
    )
).click()
picture_preview = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="com.mpower.android.app.lpin.crm:id/textViewUpload"]')
    )
).click()

milk_produce = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="বাছাই করুন"]'))).click()
milk_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="হ্যাঁ"]'))).click()

med = driver.find_element("xpath",
                          '//android.widget.ImageButton[@resource-id="com.mpower.android.app.lpin.crm:id/fabMedicine"]').click()
disease_dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsDisease"]'))).click()
disease = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="অপুষ্টি"]'))).click()

med_dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    '(//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsMedicines"])[1]'))).click()

med_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="Liq. A Zinc vet"]'))).click()
med_submit = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    '//android.widget.ImageView[@resource-id="com.mpower.android.app.lpin.crm:id/acivSubmitDialog"]'))).click()

driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.mpower.android.app.lpin.crm:id/mbSubmitMedicine"))')

time.sleep(2)

med_confirm = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitMedicine"]'))
)
if med_confirm.is_enabled():
    med_confirm.click()
else:
    print("Button is not enabled.")

ad_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.ImageView[@resource-id="com.mpower.android.app.lpin.crm:id/btnDialogClose"]'))
).click()

driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.mpower.android.app.lpin.crm:id/mbSubmitTreatment"))')

time.sleep(2)

nextday = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/acetNextDayTreatment"]'))
).send_keys("1")

follow_time = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsMidDayNewVisit"]'))
).click()
follow_pm = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="PM"]'))
).click()
collection = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbCollectionTreatment"]'))
).click()
med_price = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/acetMed"]'))
).send_keys("100")

fee = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f'(//android.widget.RadioButton[@text="300"])[1]'))
).click()

payment = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f'(//android.widget.RadioButton[@text="200"])[2]'))
).click()

submit_treatment = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitTreatment"]'))
).click()
no_message = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="com.mpower.android.app.lpin.crm:id/actvNegCustomDialog"]'))
).click()

# service_save = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitTreatment"]'))
# ).click()
# no_message = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@resource-id="com.mpower.android.app.lpin.crm:id/actvNegCustomDialog"]'))
# ).click()
time.sleep(2)
# Quit driver
driver.quit()
