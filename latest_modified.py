import urllib.request

url = "http://www.rcsb.org/pdb/rest/search"
queryText = """
<orgPdbQuery>
<queryType>org.pdb.query.simple.ModifiedStructuresQuery</queryType>
</orgPdbQuery>
"""

req = urllib.request.Request(url, data=queryText.encode())
f = urllib.request.urlopen(req)

print(f.read().decode())
