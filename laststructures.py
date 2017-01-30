from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def get_last_load_query():
    """
    Get recently added structures to PDB
    :return: List of recently added structures to PDB
    """
    url = "http://www.rcsb.org/pdb/rest/search"
    queryText = """
    <orgPdbQuery>
    <queryType>org.pdb.query.simple.LastLoadQuery</queryType>
    </orgPdbQuery>"""

    req = Request(url, data=queryText.encode())
    f = urlopen(req)

    return f.read().decode().split()


def get_obsoletes():
    """
    Get the list of obsoletes structures in PDB
    :return: List of obsoletes structures
    """
    url = "http://www.rcsb.org/pdb/rest/getObsolete"
    soup = BeautifulSoup(urlopen(Request(url)).read(), "xml")
    pdbs = soup.find_all("PDB", attrs={"structureId": True})
    return [pdb["structureId"] for pdb in pdbs]
