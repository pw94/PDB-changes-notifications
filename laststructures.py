from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_last_load_query():
    url = "http://www.rcsb.org/pdb/rest/search"
    queryText = """
    <orgPdbQuery>
    <queryType>org.pdb.query.simple.LastLoadQuery</queryType>
    </orgPdbQuery>"""

    req = Request(url, data=queryText.encode())
    f = urlopen(req)

    return f.read().decode().split()

def get_obsoletes():
    url = "http://www.rcsb.org/pdb/rest/getObsolete"
    soup = BeautifulSoup(urlopen(Request(url)).read(), "xml")
    pdbs = soup.find_all("PDB", attrs={ "structureId" : True })
    return [pdb["structureId"] for pdb in pdbs]
