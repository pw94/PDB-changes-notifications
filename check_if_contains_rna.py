import requests
from bs4 import BeautifulSoup

def contains_RNA_chains(id):
    r = requests.get("http://www.rcsb.org/pdb/rest/describeMol", params={ "structureId" : id })
    soup = BeautifulSoup(r.text, "xml")
    return len(soup.find_all("polymer",attrs={"type" : "rna"})) > 0
