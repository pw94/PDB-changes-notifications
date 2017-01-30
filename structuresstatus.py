import requests
from bs4 import BeautifulSoup


def get_obsoletes_for(structures):
    """
    Get obsolete structures from PDB for structures
    :param structures: List of structure IDs
    :return: List of pairs: obsolete and superseding structure
    """
    pairs = []
    for structure in structures:
        obsolete = get_obsolete(structure)
        if obsolete is not None:
            pairs.append((obsolete, structure))

    return pairs


def get_obsolete(id):
    """
    Get obsolete structure from PDB for structure
    :param id: ID of superseding structure
    :return: ID of obsolete structure or None if obsolete structure do not exist
    """
    r = requests.get("http://www.rcsb.org/pdb/rest/idStatus", params={"structureId": id})
    soup = BeautifulSoup(r.text, "xml")
    return soup.find("record").get("replaces")


def get_supersedings_for(structures):
    """
    Get superseding structures from PDB for structures
    :param structures: List of structure IDs
    :return: List of pairs: obsolete and superseding structure
    """
    pairs = []
    for structure in structures:
        superseding = get_obsolete(structure)
        if superseding is not None:
            pairs.append((structure, superseding))

    return pairs


def get_superseding(id):
    """
    Get superseding structure from PDB for structure
    :param id: ID of obsolete structure
    :return: ID of superseding structure or None if superseding structure do not exist
    """
    r = requests.get("http://www.rcsb.org/pdb/rest/idStatus", params={"structureId": id})
    soup = BeautifulSoup(r.text, "xml")
    return soup.find("record").get("replacedBy")
