from requests import Session
from robobrowser import RoboBrowser
from zipfile import ZipFile
import os

def get_RNA_secondary_structure(pdbId):
    url = "http://rnapdbee.cs.put.poznan.pl/"
    session = Session()
    response = session.post(url + "home/fetch", data={"pdbId":pdbId})
    response.raise_for_status()
    browser = RoboBrowser(parser="html.parser", session=session)
    browser.open(url)
    form = browser.get_form(id="analysePdb")
    datasource = browser.select("#datasourcePdb")
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
    
    with ZipFile(tmp_filename,"r") as zip_ref:
        zip_ref.extractall(results_dir)
    
    os.remove(tmp_filename)
    
    return os.path.join(results_dir, os.listdir(results_dir)[0])
