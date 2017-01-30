from shutil import rmtree
from time import sleep
from requests import Session
from robobrowser import RoboBrowser
from zipfile import ZipFile
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

SECONDS_TO_DOWNLOAD_RESULT = 5
SECONDS_TO_FILL_OUT_FORM = 30


def get_RNA_secondary_structure_via_browser(pdbId):
    driver = webdriver.Chrome()
    driver.get("http://rnapdbee.cs.put.poznan.pl/")
    driver.find_element_by_id("pdbId").send_keys(pdbId)
    get_button = driver.find_element_by_xpath("//div[@class='column2']/input[2]")
    get_button.click()
    element = WebDriverWait(driver, SECONDS_TO_FILL_OUT_FORM).until(expected_conditions.element_to_be_clickable((By.ID, "commitPdb")))
    element.send_keys(Keys.RETURN)
    WebDriverWait(driver, SECONDS_TO_FILL_OUT_FORM).until(expected_conditions.visibility_of_element_located((By.ID, "downloadResults")))
    driver.find_element_by_class_name("isDotBracket").click()
    driver.find_element_by_id("downloadAllTop").click()
    download_directory = os.path.expanduser('~/Downloads')
    sleep(SECONDS_TO_DOWNLOAD_RESULT)
    driver.close()
    files = [os.path.join(download_directory, file) for file in os.listdir(download_directory) if file.startswith("RNApdbee") and file.endswith(".zip")]
    newest_file = max(files, key=os.path.getctime)

    results_dir = os.path.abspath("results")
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    return _get_result(results_dir, newest_file)


def get_RNA_secondary_structure(pdbId):
    url = "http://rnapdbee.cs.put.poznan.pl/"
    session = Session()
    response = session.post(url + "home/fetch", data={"pdbId": pdbId})
    response.raise_for_status()
    browser = RoboBrowser(parser="html.parser", session=session)
    browser.open(url)
    form = browser.get_form(id="analysePdb")
    form["content"].value = response.text
    form["source"].value = pdbId.upper() + ".pdb"
    browser.submit_form(form)
    
    form = browser.get_form(id="downloadResults")
    form["isDotBracket"].value = "on"
    browser.submit_form(form)
    
    results_dir = os.path.abspath("results")
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    tmp_filename = os.path.join(results_dir, "tmp.zip")
    with open(tmp_filename, "wb") as output:
        output.write(browser.response.content)

    return _get_result(results_dir, tmp_filename)


def _get_result(results_dir, tmp_filename):
    with ZipFile(tmp_filename, "r") as zip_ref:
        zip_ref.extractall(results_dir)
    os.remove(tmp_filename)
    result_filename = _get_result_file(results_dir)
    result = ""
    with open(result_filename, "r") as result_file:
        result = result_file.read()
    rmtree(results_dir)
    return result


def _get_result_file(results_dir):
    result_file = os.path.join(results_dir, os.listdir(results_dir)[0])
    while os.path.isdir(result_file):
        results_dir = result_file
        result_file = os.path.join(results_dir, os.listdir(results_dir)[0])
    return result_file
