from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point
# import geopandas
import time
import openpyxl
import os
import csv
import pandas as pd

# object of Options class
op = webdriver.ChromeOptions()
# add user Agent
op.add_argument
("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
 + "AppleWebKit/537.36 (KHTML, like Gecko)"
 + "Chrome/87.0.4280.141 Safari/537.36")
# set chromedriver.exe path
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe",
# options=op)

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=op)
agent = driver.execute_script("return navigator.userAgent")
print(agent)
driver.maximize_window()

# path = 'C:/Users/Fahim Anik/Users/Fahim Anik/Users/Fahim Anik/OneDrive - Advanced Symbolics/Desktop/cca-webscraping/SeleniumAutomation/venv/Lib/Selenium_Maps_Scraping/'

polygon_area = []
path = os.getcwd()
print(path)
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


area = "Atlanta"

h = " in " + area + " Georgia"

path = os.getcwd()
print(path)
for files in os.listdir(path):
    if files.endswith('categories.csv'):
        with open(files, newline='', encoding='utf-8') as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in data:
                g = (' '.join(row))
                print(g)
                a = 0
                temp_list = []
                url_web = ('https://www.google.com/search')
                driver.get(url_web)
                try:
                    time.sleep(2)
                    driver.implicitly_wait(5)
                    search_field = driver.find_element(By.XPATH, '//*[contains(@class, "gLFyf gsfi")]')
                    time.sleep(1)
                    driver.implicitly_wait(5)
                    search_field.click()
                    time.sleep(0.5)
                    driver.implicitly_wait(5)
                    search_field.send_keys(str(g) + str(h))
                    time.sleep(0.5)
                    driver.implicitly_wait(5)
                    search_field.send_keys(Keys.ENTER)
                    more_places = driver.find_element(By.XPATH, '//*[contains(@class, "wUrVib OSrXXb")]')
                    time.sleep(0.5)
                    driver.implicitly_wait(5)
                    more_places.click()
                    span_next = driver.find_element(By.XPATH, '//*[contains(@class, "AaVjTc")]')
                    page_next = span_next.find_elements(By.XPATH, './/*[contains(text(), "Next")]')
                    element_1 = driver.find_elements(By.XPATH, '//*[contains (@class, "C8TUKc")]')
                    print(len(page_next))
                    print('--')
                    if len(page_next) > 0:
                        while len(page_next) > 0:
                            element_1 = driver.find_elements(By.XPATH, '//*[contains (@class, "C8TUKc")]')
                            element_name = driver.find_elements(By.XPATH,
                                                                '//*[contains (@class, "dbg0pd OSrXXb eDIkBe")]')
                            time.sleep(3)
                            # element_3 = driver.find_element(By.CSS_SELECTOR, '#pnnext')
                            element_2 = driver.find_elements(By.XPATH, '//*[contains(@aria-label, "Page")]')
                            for i in range(0, len(element_1)):
                                print("path is: ", str(path))
                                print("we're in page: ", str(a + 1))
                                print("we're in file: ", files)
                                print("we're in category: ", str(g))
                                print("we're in element: ", str(i + 1))
                                # for j in range(0,4):
                                try:
                                    coordinates_class_link = driver.find_elements(By.XPATH,
                                                                                  "//*[contains(@class, 'rllt__mi')]")
                                    coordinates_class = coordinates_class_link[i]
                                    coordinates_x = coordinates_class.get_attribute('data-lat')
                                    coordinates_y = coordinates_class.get_attribute('data-lng')
                                    coordinates_y = float(coordinates_y)
                                    coordinates_x = float(coordinates_x)
                                    lat_long = (coordinates_x, coordinates_y)
                                    gdf = Point(lat_long)
                                    print(gdf)
                                    print(polygon.contains(gdf))
                                    if polygon.contains(gdf):
                                        time.sleep(1)
                                        driver.implicitly_wait(2)
                                        element_1 = driver.find_elements(By.XPATH, '//*[contains (@class, "C8TUKc")]')
                                        driver.implicitly_wait(5)
                                        element_to_print = element_1[i]
                                        print(element_to_print.text)
                                        temp_list.append(element_to_print.text)
                                        # print("page is:", x)
                                except IndexError:
                                    print("There was index element error but data is added and handled")
                                    # print(element_to_print.text)
                                    try:
                                        try:
                                            coordinates_class_link = driver.find_elements(By.XPATH,
                                                                                          "//*[contains(@class, 'rllt__mi')]")
                                            coordinates_class = coordinates_class_link[i]
                                            coordinates_x = coordinates_class.get_attribute('data-lat')
                                            coordinates_y = coordinates_class.get_attribute('data-lng')
                                            coordinates_y = float(coordinates_y)
                                            coordinates_x = float(coordinates_x)
                                            lat_long = (coordinates_x, coordinates_y)
                                            gdf = Point(lat_long)
                                            print(gdf)
                                            print(polygon.contains(gdf))
                                            if polygon.contains(gdf):
                                                element_to_print = element_1[i]
                                                temp_list.append(element_to_print.text)
                                        except IndexError:
                                            try:
                                                element_to_print = element_1[i]
                                                temp_list.append(element_to_print.text)
                                            except IndexError:
                                                pass
                                    except StaleElementReferenceException:
                                        print(
                                            "Stale element Reference exception-There were no results shown for the page")
                                        # df.to_csv('resut.csv')
                                    # temp_list.append(element_to_print.text)
                                    # print(elements_to_print.text)
                            try:
                                page_next[0].click()
                            except StaleElementReferenceException:
                                span_next1 = driver.find_element(By.XPATH, '//*[contains(@class, "AaVjTc")]')
                                page_next1 = span_next1.find_element(By.XPATH, './/*[contains(text(), "Next")]')
                                try:
                                    page_next1.click()
                                except (ElementNotInteractableException, ElementClickInterceptedException):
                                    break
                                print("Stale Element Exception pagination")
                            except NoSuchElementException:
                                print("No more pages left")
                            except IndexError:
                                print("Index error pagination")
                            a += 1
                    else:
                        for i in range(0, len(element_1)):
                            print("path is: ", str(path))
                            print("we're in page: ", str(a + 1))
                            print("we're in file: ", files)
                            print("we're in category: ", str(g))
                            print("we're in element: ", str(i + 1))
                            # for j in range(0,4):
                            try:
                                time.sleep(1)
                                driver.implicitly_wait(2)
                                element_1 = driver.find_elements(By.XPATH, '//*[contains (@class, "C8TUKc")]')
                                driver.implicitly_wait(5)
                                coordinates_class_link = driver.find_elements(By.XPATH,
                                                                              "//*[contains(@class, 'rllt__mi')]")
                                coordinates_class = coordinates_class_link[i]
                                coordinates_x = coordinates_class.get_attribute('data-lat')
                                coordinates_y = coordinates_class.get_attribute('data-lng')
                                coordinates_y = float(coordinates_y)
                                coordinates_x = float(coordinates_x)
                                lat_long = (coordinates_x, coordinates_y)
                                gdf = Point(lat_long)
                                print(gdf)
                                print(polygon.contains(gdf))
                                if polygon.contains(gdf):
                                    element_to_print = element_1[i]
                                    print(element_to_print.text)
                                    temp_list.append(element_to_print.text)
                                # print("page is:", x)
                            except IndexError:
                                print("There was index element error but data is added and handled")
                                # print(element_to_print.text)
                                try:
                                    coordinates_class_link = driver.find_elements(By.XPATH,
                                                                                  "//*[contains(@class, 'rllt__mi')]")
                                    coordinates_class = coordinates_class_link[i]
                                    coordinates_x = coordinates_class.get_attribute('data-lat')
                                    coordinates_y = coordinates_class.get_attribute('data-lng')
                                    coordinates_y = float(coordinates_y)
                                    coordinates_x = float(coordinates_x)
                                    lat_long = (coordinates_x, coordinates_y)
                                    gdf = Point(lat_long)
                                    print(gdf)
                                    print(polygon.contains(gdf))
                                    if polygon.contains(gdf):
                                        temp_list.append(element_to_print.text)
                                except StaleElementReferenceException:
                                    print("Stale element Reference exception-There were no results shown for the page")
                                    # df.to_csv('resut.csv')
                                # temp_list.append(element_to_print.text)
                                # print(elements_to_print.text)
                                except IndexError:
                                    temp_list.append(element_to_print.text)
                    print("Completed category: ", str(g))
                    print(len(temp_list))
                    df = pd.DataFrame(temp_list, columns=['Company Info'])
                    df1 = df['Company Info'].str.split("\n", expand=True)
                    df1.to_csv(str(path) + "/scraped_company_names/" + str(area) + "_results_main_" + str(g) + ".csv",
                               encoding='utf-8')

                except StaleElementReferenceException:
                    print("Stale element exception df")
                    print("Completed category: ", str(g))
                    df = pd.DataFrame(temp_list, columns=['Company Info'])
                    df1 = df['Company Info'].str.split("\n", expand=True)
                    df1.to_csv(str(path) + "/scraped_company_names/" + str(area) + "_results_main_" + str(g) + ".csv",
                               encoding='utf-8')
                except NoSuchElementException:
                    print("No such element exception df")
                    print("Completed category: ", str(g))
                    print(len(temp_list))
                    df = pd.DataFrame(temp_list, columns=['Company Info'])
                    df1 = df['Company Info'].str.split("\n", expand=True)
                    df1.to_csv(str(path) + "/scraped_company_names/" + str(area) + "_results_main_" + str(g) + ".csv",
                               encoding='utf-8')
driver.close()
