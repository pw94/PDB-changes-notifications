import requests
from bs4 import BeautifulSoup


def get_obsoletes_for(structures):
    pairs = []
    for structure in structures:
        obsolete = get_obsolete(structure)
        if obsolete is not None:
            pairs.append((obsolete, structure))

    return pairs


def get_obsolete(id):
    r = requests.get("http://www.rcsb.org/pdb/rest/idStatus", params={"structureId": id})
    soup = BeautifulSoup(r.text, "xml")
    return soup.find("record").get("replaces")


def get_supersedings_for(structures):
    pairs = []
    for structure in structures:
        superseding = get_obsolete(structure)
        if superseding is not None:
            pairs.append((structure, superseding))

    return pairs


def get_superseding(id):
    r = requests.get("http://www.rcsb.org/pdb/rest/idStatus", params={"structureId": id})
    soup = BeautifulSoup(r.text, "xml")
    return soup.find("record").get("replacedBy")
