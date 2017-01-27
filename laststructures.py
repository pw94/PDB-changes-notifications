from urllib import request

def get_last_load_query():
    url = "http://www.rcsb.org/pdb/rest/search"
    queryText = """
    <orgPdbQuery>
    <queryType>org.pdb.query.simple.LastLoadQuery</queryType>
    </orgPdbQuery>"""

    req = request.Request(url, data=queryText.encode())
    f = request.urlopen(req)

    return f.read().decode().split()