from shutil import rmtree
from time import sleep
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
    """
    Get RNA secondary structure for structure from PDB in Dot-Bracket Notation
    :param pdbId: ID of structure in PDB
    :return: RNA secondary structure in Dot-Bracket Notation
    """
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


def _get_result(results_dir, tmp_filename):
    """
    Get result from downloaded zip file
    :param results_dir: Directory with results
    :param tmp_filename: Temporary downloaded zip file
    :return: Content of result file
    """
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
    """
    Find filename of file with result from downloaded files
    :param results_dir: Directory with results
    :return: Filename of file with result
    """
    result_file = os.path.join(results_dir, os.listdir(results_dir)[0])
    while os.path.isdir(result_file):
        results_dir = result_file
        result_file = os.path.join(results_dir, os.listdir(results_dir)[0])
    return result_file
