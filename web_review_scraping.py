import unicodedata
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.common.keys import Keys
#firefox installer
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.alert import Alerts
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as OP
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import selenium.webdriver.support.ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pynput.keyboard import Key, Controller
#for using proxy Ips
# from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
#for using Firefox
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point
import time
import random
import os
import unidecode
import csv
import pandas as pd
import collections

OP = webdriver.ChromeOptions()
# op = FirefoxOptions()
# op.add_argument("--headless")
OP.add_experimental_option("excludeSwitches", ["enable-automation"])
OP.add_experimental_option('useAutomationExtension', False)
# op.add_argument("start-maximized")
# op.add_argument("--window-size=1100,1000")
# op.add_argument("--headless")
OP.add_argument("--disable-gpu")
OP.add_argument('--disable-dev-shm-usage')
OP.add_argument('--no-sandbox')
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=OP)
# s = Service(executable_path=GeckoDriverManager().install())
# driver = webdriver.Firefox(service=s, firefox_options=op)
# agent = driver.execute_script("return navigator.userAgent")
# # print(agent)
# path =os.getcwd()
# print(path)
# driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
path = 'C:/Users/Fahim Anik/Users/Fahim Anik/Users/Fahim Anik/OneDrive - Advanced Symbolics/Desktop/cca-webscraping/SeleniumAutomation/venv/Lib/Selenium_Maps_Scraping/'


def convert_url_to_point(x):
    split1 = x.split("=")
    split2 = split1[1].split("%2C")
    x_coordinates = split2[0]
    y = split2[1]
    y_coordinates = y.split("&")[0]
    x_coordinates = float(x_coordinates)
    y_coordinates = float(y_coordinates)
    point = Point(x_coordinates, y_coordinates)
    return point


driver.maximize_window()
time_to_sleep = random.randint(1, 3)
print(time_to_sleep)

area = " Atlanta"
h=" in " + area+ " Georgia"
# h = area
print(h)

polygon_area = []
# path = os.getcwd()
# print(path)
for files in os.listdir(path):
    if files.endswith('atlanta_polygon.csv'):
        csv_name = path + files
        df = pd.read_csv(csv_name)
        b = df.columns.values.tolist()
        print(b)
        df['coordinates'] = list(zip(df.Lat, df.Lon))
        print(df)
        for values in df['coordinates']:
            polygon_area.append(values)
        print(polygon_area)
        polygon = Polygon(polygon_area)
        print(polygon)

print(polygon)

for filename in sorted(os.listdir(path)):
    # print("filename is ", filename)
    if filename.endswith('31.csv'):
        csv_name = path + filename
        df = pd.read_csv(csv_name)
        b = df.columns.values.tolist()
        print(b)
        print(df["0"])
        df["0"] = df["0"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        d = df["0"]
        # print(d)
        slwd = 0
        for values in d:
            total_count = collections.Counter(values)
            time_to_sleep = random.randint(1, 3)
            print(values)
            print("We have covered {} number of companies" .format(slwd))
            # trying = len(values)
            list_company_name = []
            list_company_rating = []
            list_google_reviewer_name = []
            list_google_reviewer_rating = []
            list_google_reviewer_comment = []
            list_google_total_review = []
            list_company_details = []
            list_company_values = []
            list_company_number = []
            list_company_province = []
            list_company_desc = []
            try:
                url_web = 'https://www.google.com/search'
                driver.get(url_web)
                driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
                user_agent = driver.execute_script("return navigator.userAgent;")
                print(user_agent)
                time.sleep(time_to_sleep)
                driver.implicitly_wait(5)
                search_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "gLFyf gsfi")]')))
                # search_field = driver.find_element(By.XPATH, '//*[contains(@class, "gLFyf gsfi")]')
                time.sleep(time_to_sleep)
                driver.implicitly_wait(5)
                try:
                    search_field.click()
                except StaleElementReferenceException:
                    print(" error clicking search")
                time.sleep(time_to_sleep)
                driver.implicitly_wait(5)
                search_field.send_keys(str(values) + str(h))
                time.sleep(time_to_sleep)
                driver.implicitly_wait(5)
                search_field.send_keys(Keys.ENTER)
                time.sleep(time_to_sleep)
                more_places = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(text(), "Maps")]')))
                maps_click = more_places[0]
                time.sleep(time_to_sleep)
                driver.implicitly_wait(5)
                try:
                    maps_click.click()
                except ElementNotInteractableException:
                    maps_find = driver.find_element(By.XPATH, '//*[contains(@class, "GOE98c")]')
                    maps_find.click()
                    time.sleep(0.5)
                    more_places = driver.find_elements(By.XPATH, '//*[contains(text(), "Maps")]')
                    maps_click = more_places[0]
                    maps_click.click()
                time.sleep(1)
                driver.implicitly_wait(5)
                try:
                    time.sleep(0.5)
                    driver.implicitly_wait(5)
                    company_name = driver.find_element(By.XPATH, '//*[contains(@class, "x3AX1-LfntMc-header-title-title gm2-headline-5")]')
                    list_company_name.append(company_name.text)
                    print(company_name.text)
                    page_url = driver.find_element(By.XPATH, "(//meta[@itemprop= 'image'])")
                    print("printing url: ")
                    content_for_polygon = page_url.get_attribute("content")
                    print(page_url.get_attribute("content"))
                    point_webpage = convert_url_to_point(content_for_polygon)
                    print(polygon.contains(point_webpage))
                    if polygon.contains(point_webpage):
                        try:
                            company_name = driver.find_element(By.XPATH, '//*[contains(@class, "x3AX1-LfntMc-header-title-title gm2-headline-5")]')
                            list_company_name.append(company_name.text)
                            print(company_name.text)
                            print(driver.current_url)
                        except NoSuchElementException:
                            list_company_name.append("There was no Company name found")
                            print("No company name found")
                        try:
                            time.sleep(0.5)
                            driver.implicitly_wait(5)
                            company_details = driver.find_element(By.XPATH, '(//*[contains(@aria-label, "Information for")])')
                            # company_address = company_loop[0]
                            list_company_details.append(company_details.text)
                            print(company_details.text)
                        except NoSuchElementException:
                            list_company_details.append("There was no Company details")
                            print("No company details found")
                            pass
                        try:
                            time.sleep(0.5)
                            driver.implicitly_wait(5)
                            company_rating = driver.find_element(By.XPATH, '(//*[contains(@class, "OAO0-ZEhYpd-vJ7A6b OAO0-ZEhYpd-vJ7A6b-qnnXGd")])[1]')
                            rating_text = company_rating.text
                            time.sleep(0.2)
                            list_company_rating.append(rating_text)
                            print(company_rating.text)
                        except NoSuchElementException:
                            list_company_rating.append("There was no Company rating found")
                            print("No company rating found")
                            pass
                        list_company_values.append(values)
                        try:
                            time.sleep(0.5)
                            driver.implicitly_wait(5)
                            company_desc = driver.find_element(By.XPATH, "(//*[contains(@class, 'Yr7JMd-pane-hSRGPd')])[4]")
                            # company_desc = review_loop[3]
                            list_company_desc.append(company_desc.text)
                            print(company_desc.text)
                        except NoSuchElementException:
                            try:
                                company_desc_new = driver.find_element(By.XPATH, "(//*[contains(@class, 'h0ySl-wcwwM-E70qVe-list')])")
                                list_company_desc.append(company_desc_new.text)
                                print(company_desc_new.text)
                                print(" printed")
                            except NoSuchElementException:
                                list_company_desc.append(" ")
                                print("No description found")
                        try:
                            time.sleep(1)
                            driver.implicitly_wait(5)
                            review_loop = driver.find_element(By.XPATH, "//*[contains(@class, 'section-star-array')][1]")
                            review_link = driver.find_element(By.XPATH, '(//*[contains(@class, "Yr7JMd-pane-hSRGPd")])[1]')
                            # print(asdc)
                            print(driver.current_url)
                            list_google_total_review.append(review_link.text)
                            print(review_link.text)
                            time.sleep(1)
                            try:
                                review_loop.click()
                            except (StaleElementReferenceException, ElementClickInterceptedException):
                                time.sleep(1)
                                new_review_loop = driver.find_element(By.XPATH, "(//*[contains(@class, 'Yr7JMd-pane-hSRGPd')])[1]")
                                time.sleep(1)
                                new_review_loop.click()
                            try:
                                time.sleep(1)
                                driver.implicitly_wait(5)
                                try:
                                    sort_main = driver.find_element(By.XPATH, "(//*[contains(@class,'GMtm7c gm2-button-alt')])[2]")
                                    sort_main.click()
                                except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
                                    sort_main_new = driver.find_element(By.XPATH, "(//*[contains(@class,'gm2-body-1 k5lwKb')])[2]")
                                    sort_main_new.click()
                                time.sleep(0.5)
                                try:
                                    sort_main_newest = driver.find_element(By.XPATH, "(//*[contains(@class,'nbpPqf-menu-x3Eknd')])[4]")
                                    sort_main_newest.click()
                                except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
                                    sort_main_newest_handle = driver.find_element(By.XPATH, "(//*[contains(@class,'nbpPqf-menu-x3Eknd-text-haAclf')])[2]")
                                    sort_main_newest_handle.click()
                                time.sleep(2)
                                driver.implicitly_wait(5)
                                reviews = driver.find_elements(By.XPATH, "//*[contains(@class,'ODSEW-ShBeI-content')]")
                                for review in range(len(reviews)):
                                    print("filename is ", filename)
                                    print("Company is ", values)
                                    print("Review Number: ", str(review+1))
                                    print("File is stored in: ", (str(path)+ '/scraped_company_reviews'))
                                    if review <= 10:
                                        print(driver.current_url)
                                        review_source = reviews[review]
                                        # print(review_source)
                                        try:
                                            time.sleep(0.75)
                                            reviewer_name = review_source.find_element(By.XPATH, ".//*[contains(@class, 'ODSEW-ShBeI-title')]")
                                            print(reviewer_name.text)
                                            list_google_reviewer_name.append(reviewer_name.text)
                                            try:
                                                reviewer_rating = review_source.find_element(By.XPATH, ".//*[contains(@class, 'ODSEW-ShBeI-H1e3jb')]")
                                                reviewer_rating_value = reviewer_rating.get_attribute('aria-label')
                                                list_google_reviewer_rating.append(reviewer_rating_value)
                                            except NoSuchElementException:
                                                print("I'm here")
                                                reviewer_rating_new = review_source.find_element(By.XPATH, ".//*[contains(@class, 'ODSEW-ShBeI-RGxYjb-wcwwM')]")
                                                q = reviewer_rating_new.text
                                                vc = q.replace("/", " out of ")
                                                print(vc)
                                                list_google_reviewer_rating.append(vc)
                                            try:
                                                try:
                                                    # print("in review rating loop")
                                                    more_link = review_source.find_element(By.XPATH, './/*[contains(@class, "ODSEW-KoToPc-ShBeI gXqMYb-hSRGPd")]')
                                                    more_link.click()
                                                    driver.implicitly_wait(10)
                                                    google_review_comment = review_source.find_element(By.XPATH, './/*[contains(@class, "ODSEW-ShBeI-text")]')
                                                    print(google_review_comment.text)
                                                    list_google_reviewer_comment.append(google_review_comment.text)
                                                except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                                                    try:
                                                        # print("in review rating exception loop")
                                                        driver.implicitly_wait(10)
                                                        google_review_comment = review_source.find_element(By.XPATH, './/*[contains(@class, "ODSEW-ShBeI-text")]')
                                                        print(google_review_comment.text)
                                                        list_google_reviewer_comment.append(google_review_comment.text)
                                                    except NoSuchElementException:
                                                        print("No reviews for user")
                                                        list_google_reviewer_comment.append("No reviews for user")
                                            except NoSuchElementException:
                                                print("Has no reviews probably")
                                                list_google_reviewer_name.append("No reviews for company")
                                                list_google_reviewer_rating.append("No reviews for company")
                                                list_google_reviewer_comment.append("No reviews for company")
                                                list_google_total_review.append("No reviews for company")
                                        except NoSuchElementException:
                                            print("Has no reviews probably")
                                            list_google_reviewer_name.append("No reviews for company")
                                            list_google_reviewer_rating.append("No reviews for company")
                                            list_google_reviewer_comment.append("No reviews for company")
                                            list_google_total_review.append("No reviews for company")
                            except StaleElementReferenceException:
                                print("This method is handled")
                                try:
                                    sort_main_newest = driver.find_element(By.XPATH, "(//*[contains(@class,'nbpPqf-menu-x3Eknd')])[4]")
                                    sort_main_newest.click()
                                except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
                                    sort_main_newest_handle = driver.find_element(By.XPATH, "(//*[contains(@class,'nbpPqf-menu-x3Eknd-text-haAclf')])[2]")
                                    sort_main_newest_handle.click()
                                time.sleep(2)
                                driver.implicitly_wait(5)
                                reviews1 = driver.find_elements(By.XPATH, "//*[contains(@class,'ODSEW-ShBeI-content')]")
                                for review in range(len(reviews1)):
                                    print("filename is ", filename)
                                    print("Company is ", values)
                                    print("Review Number: ", str(review+1))
                                    print("File is stored in: ", (str(path)+ '/scraped_company_reviews'))
                                    if review <= 10:
                                        review_source1 = reviews1[review]
                                        # print(review_source)
                                        try:
                                            time.sleep(0.75)
                                            reviewer_name = review_source1.find_element(By.XPATH, ".//*[contains(@class, 'ODSEW-ShBeI-title')]")
                                            print(reviewer_name.text)
                                            list_google_reviewer_name.append(reviewer_name.text)
                                            try:
                                                reviewer_rating = review_source1.find_element(By.XPATH, ".//*[contains(@class, 'ODSEW-ShBeI-H1e3jb')]")
                                                reviewer_rating_value = reviewer_rating.get_attribute('aria-label')
                                                list_google_reviewer_rating.append(reviewer_rating_value)
                                            except NoSuchElementException:
                                                print("I'm here")
                                                reviewer_rating_new = review_source1.find_element(By.XPATH, ".//*[contains(@class, 'ODSEW-ShBeI-RGxYjb-wcwwM')]")
                                                q = reviewer_rating_new.text
                                                vc = q.replace("/", " out of ")
                                                print(vc)
                                                list_google_reviewer_rating.append(vc)
                                            try:
                                                try:
                                                    # print("in review rating loop")
                                                    more_link = review_source1.find_element(By.XPATH, './/*[contains(@class, "ODSEW-KoToPc-ShBeI gXqMYb-hSRGPd")]')
                                                    more_link.click()
                                                    driver.implicitly_wait(10)
                                                    google_review_comment = review_source1.find_element(By.XPATH, './/*[contains(@class, "ODSEW-ShBeI-text")]')
                                                    print(google_review_comment.text)
                                                    list_google_reviewer_comment.append(google_review_comment.text)
                                                except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                                                    try:
                                                        # print("in review rating exception loop")
                                                        driver.implicitly_wait(10)
                                                        google_review_comment = review_source1.find_element(By.XPATH, './/*[contains(@class, "ODSEW-ShBeI-text")]')
                                                        print(google_review_comment.text)
                                                        list_google_reviewer_comment.append(google_review_comment.text)
                                                    except NoSuchElementException:
                                                        print("No reviews for user")
                                                        list_google_reviewer_comment.append("No reviews for user")
                                            except NoSuchElementException:
                                                print("Has no reviews probably")
                                                list_google_reviewer_name.append("No reviews for company")
                                                list_google_reviewer_rating.append("No reviews for company")
                                                list_google_reviewer_comment.append("No reviews for company")
                                                list_google_total_review.append("No reviews for company")
                                        except NoSuchElementException:
                                            print("Has no reviews probably")
                                            list_google_reviewer_name.append("No reviews for company")
                                            list_google_reviewer_rating.append("No reviews for company")
                                            list_google_reviewer_comment.append("No reviews for company")
                                            list_google_total_review.append("No reviews for company")
                        except NoSuchElementException:
                            list_google_reviewer_name.append("No reviews for company")
                            list_google_reviewer_rating.append("No reviews for company")
                            list_google_reviewer_comment.append("No reviews for company")
                            list_google_total_review.append("No reviews for company")
                    googleReview = {
                        'Actual Company Name': list_company_values,
                        'Company Name': list_company_name,
                        'Company Rating': list_company_rating,
                        'Company Details': list_company_details,
                        'Company Description': list_company_desc,
                        'Total Reviews': list_google_total_review,
                        'Reviewer Name': list_google_reviewer_name,
                        'Reviewer Comment': list_google_reviewer_comment,
                        'Reviewer Rating': list_google_reviewer_rating
                    }
                    # googleReview_df = pd.DataFrame(googleReview)
                    df = pd.DataFrame.from_dict(googleReview, orient='index')
                    df = df.transpose()
                    df['Reviewer Rating'] = df['Reviewer Rating'].astype(str).str.replace(',$', '')
                    df['Reviewer Comment'] = df['Reviewer Comment'].astype(str).str.replace(r'…More$', '')

                    df['Reviewer Name'] = df['Reviewer Name'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                    df['Company Name'] = df['Company Name'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                    df['Company Details'] = df['Company Details'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                    df['Reviewer Comment'] = df['Reviewer Comment'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                    df['Company Description'] = df['Company Description'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                    df['Reviewer Rating'] = df['Reviewer Rating'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                    # filename = filename.replace('.csv$', ' ')
                    alphanumeric = ''
                    for character in values:
                        if character.isalnum():
                            alphanumeric += character
                    x = ''.join(e for e in values if e.isalnum())
                    x_short = x[:30]
                    y = ''.join(p for p in filename if p.isalnum())
                    # y = y.strip("Finaleditedresu")
                    y = y.strip(".csv")
                    googleReview_df_to_csv = df.to_csv(path + "/scraped_company_reviews/" + "file- " + str(slwd) + str(x_short) + "_" + str(area) + ".csv")
                    slwd+=1
                except NoSuchElementException:
                    try:
                        # print("here")
                        time.sleep(1)
                        driver.implicitly_wait(5)
                        company_name_block = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@class, "a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")]')))
                        # print(company_name_block)
                        print("here 2")
                        n_l = 0
                        # print("we're outside loop", str(values))
                        for exs in range(len(company_name_block)):
                            time.sleep(1)
                            elements = company_name_block[exs]
                            # print(elements)
                            try:
                                clicking = company_name_block[exs].get_attribute('aria-label')
                                time.sleep(1)
                                try:
                                    elements.click()
                                except ElementClickInterceptedException:
                                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                                print(clicking)
                            except StaleElementReferenceException:
                                company_name_block1 = driver.find_elements(By.XPATH, '//*[contains(@class, "a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")]')
                                clicking1 = company_name_block1[exs].get_attribute('aria-label')
                                time.sleep(1)
                                try:
                                    elements.click()
                                except StaleElementReferenceException:
                                    company_name_block1 = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@class, "a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")]')))
                                    elements1 = company_name_block1[exs]
                                    try:
                                        elements1.click()
                                    except ElementClickInterceptedException:
                                        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                                print(clicking1)
                            list_company_name.clear()
                            page_url = driver.find_element(By.XPATH, "(//meta[@itemprop= 'image'])")
                            print("printing url: ")
                            content_for_polygon = page_url.get_attribute("content")
                            print(page_url.get_attribute("content"))
                            point_webpage = convert_url_to_point(content_for_polygon)
                            print(polygon.contains(point_webpage))
                            if polygon.contains(point_webpage):
                                company_name1 = driver.find_element(By.XPATH, "//*[contains(@class, 'x3AX1-LfntMc-header-title-title gm2-headline-5')]")
                                list_company_name.append(company_name1.text)
                                print(company_name1.text)
                                try:
                                    list_company_rating.clear()
                                    time.sleep(time_to_sleep)
                                    company_rating1 = driver.find_element(By.XPATH, '(//*[contains(@class, "OAO0-ZEhYpd-vJ7A6b OAO0-ZEhYpd-vJ7A6b-qnnXGd")])[1]')
                                    list_company_rating.append(company_rating1.text)
                                    print(company_rating1.text)
                                except NoSuchElementException:
                                    print("No rating found for company")
                                try:
                                    list_company_details.clear()
                                    time.sleep(0.5)
                                    driver.implicitly_wait(5)
                                    company_details = driver.find_element(By.XPATH, '(//*[contains(@aria-label, "Information for")])')
                                    # company_address = company_loop[0]
                                    list_company_details.append(company_details.text)
                                    print(company_details.text)
                                except NoSuchElementException:
                                    list_company_details.append("There was no Company details")
                                    print("No company details found")
                                list_company_values.append(values)
                                try:
                                    list_company_desc.clear()
                                    time.sleep(0.5)
                                    driver.implicitly_wait(5)
                                    company_desc1 = driver.find_element(By.XPATH, "(//*[contains(@class, 'Yr7JMd-pane-hSRGPd')])[4]")
                                    # company_desc = review_loop[3]
                                    list_company_desc.append(company_desc1.text)
                                    print(company_desc1.text)
                                except NoSuchElementException:
                                    try:
                                        company_desc_new = driver.find_element(By.XPATH, "(//*[contains(@class, 'h0ySl-wcwwM-E70qVe-list')])")
                                        list_company_desc.append(company_desc_new.text)
                                        print(company_desc_new.text)
                                        print(" printed")
                                    except NoSuchElementException:
                                        list_company_desc.append(" ")
                                        print("No description found")
                                try:
                                    list_google_total_review.clear()
                                    time.sleep(1)
                                    driver.implicitly_wait(5)
                                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                                    review_loop = driver.find_element(By.XPATH, "//*[contains(@class, 'section-star-array')][1]")
                                    review_link = driver.find_element(By.XPATH, '(//*[contains(@class, "Yr7JMd-pane-hSRGPd")])[1]')
                                    list_google_total_review.append(review_link.text)
                                    print(review_link.text)
                                    time.sleep(1)
                                    try:

                                        review_loop.click()
                                    except (StaleElementReferenceException, ElementClickInterceptedException):
                                        time.sleep(1)
                                        new_review_loop = driver.find_element(By.XPATH, "(//*[contains(@class, 'Yr7JMd-pane-hSRGPd')])[1]")
                                        time.sleep(1)
                                        new_review_loop.click()
                                    try:
                                        time.sleep(1)
                                        driver.implicitly_wait(5)
                                        try:
                                            sort_main = driver.find_element(By.XPATH, "(//*[contains(@class,'GMtm7c gm2-button-alt')])[2]")
                                            sort_main.click()
                                        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
                                            sort_main_new = driver.find_element(By.XPATH, "(//*[contains(@class,'gm2-body-1 k5lwKb')])[2]")
                                            sort_main_new.click()
                                        time.sleep(0.5)
                                        try:
                                            sort_main_newest = driver.find_element(By.XPATH, "(//*[contains(@class,'nbpPqf-menu-x3Eknd')])[4]")
                                            sort_main_newest.click()
                                        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
                                            sort_main_newest_handle = driver.find_element(By.XPATH, "(//*[contains(@class,'nbpPqf-menu-x3Eknd-text-haAclf')])[2]")
                                            sort_main_newest_handle.click()
                                        time.sleep(2)
                                        driver.implicitly_wait(5)
                                        reviews = driver.find_elements(By.XPATH, "//*[contains(@class,'ODSEW-ShBeI-content')]")
                                        list_google_reviewer_comment.clear()
                                        list_google_reviewer_name.clear()
                                        list_google_reviewer_rating.clear()
                                        for review in range(len(reviews)):
                                            print("filename is ", filename)
                                            print("Company is ", values)
                                            print("Review Number: ", str(review+1))
                                            print("File is stored in: ", (str(path)+ '/scraped_company_reviews'))
                                            print("we're in the {} company in the search list".format(str(exs + 1)))
                                            if review <= 10:
                                                review_source = reviews[review]
                                                # print(review_source)
                                                try:
                                                    time.sleep(0.75)
                                                    reviewer_name = review_source.find_element(By.XPATH, ".//*[contains(@class, 'ODSEW-ShBeI-title')]")
                                                    print(reviewer_name.text)
                                                    list_google_reviewer_name.append(reviewer_name.text)
                                                    try:
                                                        reviewer_rating = review_source.find_element(By.XPATH, ".//*[contains(@class, 'ODSEW-ShBeI-H1e3jb')]")
                                                        reviewer_rating_value = reviewer_rating.get_attribute('aria-label')
                                                        print(reviewer_rating_value)
                                                        list_google_reviewer_rating.append(reviewer_rating_value)
                                                    except NoSuchElementException:
                                                        print("I'm here")
                                                        reviewer_rating_new = review_source.find_element(By.XPATH, ".//*[contains(@class, 'ODSEW-ShBeI-RGxYjb-wcwwM')]")
                                                        q = reviewer_rating_new.text
                                                        vc = q.replace("/", " out of ")
                                                        print(vc)
                                                        list_google_reviewer_rating.append(vc)
                                                    try:
                                                        try:
                                                            # print("in review rating loop")
                                                            more_link = review_source.find_element(By.XPATH, './/*[contains(@class, "ODSEW-KoToPc-ShBeI gXqMYb-hSRGPd")]')
                                                            more_link.click()
                                                            driver.implicitly_wait(10)
                                                            google_review_comment = review_source.find_element(By.XPATH, './/*[contains(@class, "ODSEW-ShBeI-text")]')
                                                            print(google_review_comment.text)
                                                            list_google_reviewer_comment.append(google_review_comment.text)
                                                        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                                                            try:
                                                                # print("in review rating exception loop")
                                                                driver.implicitly_wait(10)
                                                                google_review_comment = review_source.find_element(By.XPATH, './/*[contains(@class, "ODSEW-ShBeI-text")]')
                                                                print(google_review_comment.text)
                                                                list_google_reviewer_comment.append(google_review_comment.text)
                                                            except NoSuchElementException:
                                                                print("No reviews for user")
                                                                list_google_reviewer_comment.append("No reviews for user")
                                                    except NoSuchElementException:
                                                        print("Has no reviews probably")
                                                        list_google_reviewer_name.append("No reviews for company")
                                                        list_google_reviewer_rating.append("No reviews for company")
                                                        list_google_reviewer_comment.append("No reviews for company")
                                                        list_google_total_review.append("No reviews for company")
                                                except NoSuchElementException:
                                                    print("Has no reviews probably")
                                                    list_google_reviewer_name.append("No reviews for company")
                                                    list_google_reviewer_rating.append("No reviews for company")
                                                    list_google_reviewer_comment.append("No reviews for company")
                                                    list_google_total_review.append("No reviews for company")
                                        list_company_values.append(values)
                                        time.sleep(time_to_sleep)
                                        try:
                                            go_back = driver.find_element(By.XPATH, '//*[contains(@class, "NMm5M hhikbc")]')
                                            go_back.click()
                                        except StaleElementReferenceException:
                                            time.sleep(1)
                                            go_back2 = driver.find_element(By.XPATH, '//*[contains(@class, "NMm5M hhikbc")]')
                                            go_back2.click()
                                    except StaleElementReferenceException:
                                        print("This method is handled")
                                        try:
                                            sort_main_newest = driver.find_element(By.XPATH, "(//*[contains(@class,'nbpPqf-menu-x3Eknd')])[4]")
                                            sort_main_newest.click()
                                        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
                                            sort_main_newest_handle = driver.find_element(By.XPATH, "(//*[contains(@class,'nbpPqf-menu-x3Eknd-text-haAclf')])[2]")
                                            sort_main_newest_handle.click()
                                        time.sleep(2)
                                        driver.implicitly_wait(5)
                                        reviews = driver.find_elements(By.XPATH, "//*[contains(@class,'ODSEW-ShBeI-content')]")
                                        list_google_reviewer_comment.clear()
                                        list_google_reviewer_name.clear()
                                        list_google_reviewer_rating.clear()
                                        for review in range(len(reviews)):
                                            if review <= 10:
                                                review_source = reviews[review]
                                                # print(review_source)
                                                try:
                                                    time.sleep(0.75)
                                                    reviewer_name = review_source.find_element(By.XPATH, ".//*[contains(@class, 'ODSEW-ShBeI-title')]")
                                                    print(reviewer_name.text)
                                                    list_google_reviewer_name.append(reviewer_name.text)
                                                    try:
                                                        reviewer_rating = review_source.find_element(By.XPATH, ".//*[contains(@class, 'ODSEW-ShBeI-H1e3jb')]")
                                                        reviewer_rating_value = reviewer_rating.get_attribute('aria-label')
                                                        print(reviewer_rating_value)
                                                        list_google_reviewer_rating.append(reviewer_rating_value)
                                                    except NoSuchElementException:
                                                        reviewer_rating_new = review_source.find_element(By.XPATH, ".//*[contains(@class, 'ODSEW-ShBeI-RGxYjb-wcwwM')]")
                                                        q = reviewer_rating_new.text
                                                        vc = q.replace("/", " out of ")
                                                        print(vc)
                                                        list_google_reviewer_rating.append(vc)
                                                    try:
                                                        try:
                                                            print("in review rating loop")
                                                            more_link = review_source.find_element(By.XPATH, './/*[contains(@class, "ODSEW-KoToPc-ShBeI gXqMYb-hSRGPd")]')
                                                            more_link.click()
                                                            time.sleep(1)
                                                            driver.implicitly_wait(10)
                                                            google_review_comment = review_source.find_element(By.XPATH, '.(//*[contains(@class, "ODSEW-ShBeI-text")])')
                                                            print(google_review_comment.text)
                                                            list_google_reviewer_comment.append(google_review_comment.text)
                                                        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                                                            try:
                                                                print("in review rating exception loop")
                                                                driver.implicitly_wait(10)
                                                                time.sleep(1)
                                                                google_review_comment = review_source.find_element(By.XPATH, '.(//*[contains(@class, "ODSEW-ShBeI-text")])')
                                                                print(google_review_comment.text)
                                                                list_google_reviewer_comment.append(google_review_comment.text)
                                                            except NoSuchElementException:
                                                                print("No reviews for user")
                                                                list_google_reviewer_comment.append("No reviews for user")
                                                    except NoSuchElementException:
                                                        print("Has no reviews probably")
                                                        list_google_reviewer_name.append("No reviews for company")
                                                        list_google_reviewer_rating.append("No reviews for company")
                                                        list_google_reviewer_comment.append("No reviews for company")
                                                        list_google_total_review.append("No reviews for company")
                                                except NoSuchElementException:
                                                    print("Has no reviews probably")
                                                    list_google_reviewer_name.append("No reviews for company")
                                                    list_google_reviewer_rating.append("No reviews for company")
                                                    list_google_reviewer_comment.append("No reviews for company")
                                                    list_google_total_review.append("No reviews for company")
                                        time.sleep(time_to_sleep)
                                        go_back1 = driver.find_element(By.XPATH, '//*[contains(@class, "NMm5M hhikbc")]')
                                        go_back1.click()
                                except NoSuchElementException:
                                    print("No Reviews found")
                                    list_company_name.clear()
                                    list_company_details.clear()
                                    list_company_rating.clear()
                                    list_google_reviewer_rating.clear()
                                    list_company_desc.clear()
                                    list_google_total_review.clear()
                                    list_google_reviewer_name.clear()
                                    list_google_reviewer_comment.clear()
                                googleReview = {
                                    'Actual Company Name': list_company_values,
                                    'Company Name': list_company_name,
                                    'Company Rating': list_company_rating,
                                    'Company Details': list_company_details,
                                    'Company Description': list_company_desc,
                                    'Total Reviews': list_google_total_review,
                                    'Reviewer Name': list_google_reviewer_name,
                                    'Reviewer Comment': list_google_reviewer_comment,
                                    'Reviewer Rating': list_google_reviewer_rating
                                }
                                # googleReview_df = pd.DataFrame(googleReview)
                                df = pd.DataFrame.from_dict(googleReview, orient='index')
                                df = df.transpose()
                                df['Reviewer Rating'] = df['Reviewer Rating'].astype(str).str.replace(',$', '')
                                df['Reviewer Comment'] = df['Reviewer Comment'].astype(str).str.replace(r'…More$', '')

                                df['Reviewer Name'] = df['Reviewer Name'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                                df['Company Name'] = df['Company Name'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                                df['Company Details'] = df['Company Details'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                                df['Reviewer Comment'] = df['Reviewer Comment'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                                df['Company Description'] = df['Company Description'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                                df['Reviewer Rating'] = df['Reviewer Rating'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                                # filename = filename.replace('.csv$', ' ')
                                alphanumeric = ''
                                for character in values:
                                    if character.isalnum():
                                        alphanumeric += character
                                x = ''.join(e for e in values if e.isalnum())
                                x_short = x[:30]
                                y = ''.join(p for p in filename if p.isalnum())
                                # y = y.strip("Finaleditedresu")
                                y = y.strip(".csv")
                                googleReview_df_to_csv = df.to_csv(path + "/scraped_company_reviews/" + "file- " + str(slwd) + str(x_short) + "_" + str(exs + 1) + "_" + str(area) + ".csv")
                                # driver.close()
                            googleReview = {
                                'Actual Company Name': list_company_values,
                                'Company Name': list_company_name,
                                'Company Rating': list_company_rating,
                                'Company Details': list_company_details,
                                'Company Description': list_company_desc,
                                'Total Reviews': list_google_total_review,
                                'Reviewer Name': list_google_reviewer_name,
                                'Reviewer Comment': list_google_reviewer_comment,
                                'Reviewer Rating': list_google_reviewer_rating
                            }
                            # googleReview_df = pd.DataFrame(googleReview)
                            df = pd.DataFrame.from_dict(googleReview, orient='index')
                            df = df.transpose()
                            df['Reviewer Rating'] = df['Reviewer Rating'].astype(str).str.replace(',$', '')
                            df['Reviewer Comment'] = df['Reviewer Comment'].astype(str).str.replace(r'…More$', '')

                            df['Reviewer Name'] = df['Reviewer Name'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                            df['Company Name'] = df['Company Name'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                            df['Company Details'] = df['Company Details'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                            df['Reviewer Comment'] = df['Reviewer Comment'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                            df['Company Description'] = df['Company Description'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                            df['Reviewer Rating'] = df['Reviewer Rating'].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
                            # filename = filename.replace('.csv$', ' ')
                            alphanumeric = ''
                            for character in values:
                                if character.isalnum():
                                    alphanumeric += character
                            x = ''.join(e for e in values if e.isalnum())
                            x_short = x[:30]
                            y = ''.join(p for p in filename if p.isalnum())
                            # y = y.strip("Finaleditedresu")
                            y = y.strip(".csv")
                            googleReview_df_to_csv = df.to_csv(path + "/scraped_company_reviews/" + "file- " + str(slwd) + str(x_short) + "_" + str(exs + 1) + "_" + str(area) + ".csv")
                            # driver.close()
                            try:
                                time.sleep(0.5)
                                go_main_page = driver.find_element(By.XPATH, '//*[contains(@class, "xoLGzf-icon")]')
                                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                                go_main_page.click()
                            except NoSuchElementException:
                                pass
                            except ElementNotInteractableException:
                                print("couldn't go to the main page, some error occured")
                    except NoSuchElementException:
                        print("No results found")
                    slwd+=1
            except NoSuchElementException:
                list_google_reviewer_name.append("No reviews for company")
                list_google_reviewer_rating.append("No reviews for company")
                list_google_reviewer_comment.append("No reviews for company")
                list_google_total_review.append("No reviews for company")
                print("No reviews for company")
            except IndexError:
                print("There was index error-maybe the company wasn't located")
            try:
                driver.get(url_web)
            except InvalidSessionIdException:
                driver.get(url_web)
 # # print(type(clicking))
                            # try:
                            #     time.sleep(1)
                            #     x1 = clicking
                            #     x1 = unicodedata.normalize('NFD', x1).encode('ascii', 'ignore').decode("utf-8")
                            #     x1 = x1.lower()
                            #     x1_new = ''.join(filter(str.isalnum, x1))
                            #     print(x1_new)
                            #     print("here")
                            # except StaleElementReferenceException:
                            #     time.sleep(1)
                            #     # x1 = unidecode.unidecode(x1)
                            #     x1 = unicodedata.normalize('NFD', x1).encode('ascii', 'ignore').decode("utf-8")
                            #     x1 = x1.lower()
                            #     x1_new = ''.join(filter(str.isalnum, x1))
                            #     print(x1_new)
                            #     # print(x1)
                            #     # print("here error")
                            # values_new = ''.join(filter(str.isalnum, values))
                            # print("n_l is " + str(n_l))
                            # print("we're in loop", str(values))
                            # if (values_new.lower()) in x1_new:
                            #     print("found name, it is: ", str(x1))
                            #     time.sleep(0.5)
                            #     driver.implicitly_wait(2)
                            #     try:
                            #         print("click loop")
                            #         time.sleep(1)
                            #         driver.implicitly_wait(2)
                            #         elements.click()
                            #         time.sleep(1)
                            #         driver.implicitly_wait(2)
                            #         time.sleep(0.5)
                            #
                            #
                            #     except ElementClickInterceptedException:
                            #         print("handled click")
                            #         print(x1)
                            #         list_company_name.append(x1)
                            #         elements.click()
                            #     except IndexError:
                            #         print("Index error occured")
                            # n_l+=1
