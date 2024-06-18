from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
import time
import pandas as pd

path = C:\Users\Blaise Fonguh\chromedriver-win64 # type: ignore
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
web = 'https://en.wikipedia.org/wiki/1960_European_Nations%27_Cup'

driver.get(web)