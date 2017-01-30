import requests
from bs4 import BeautifulSoup


def contains_RNA_chains(id):
    """
    Check if structure contains RNA chains
    :param id: ID of structure in PDB
    :return: True if structure contains RNA chains, False otherwise
    """
    r = requests.get("http://www.rcsb.org/pdb/rest/describeMol", params={"structureId": id})
    soup = BeautifulSoup(r.text, "xml")
    return len(soup.find_all("polymer", attrs={"type": "rna"})) > 0
