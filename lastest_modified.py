import requests

url = "http://www.rcsb.org/pdb/rest/search"
request_body = """
<orgPdbQuery>
<queryType>org.pdb.query.simple.ModifiedStructuresQuery</queryType>
</orgPdbQuery>
"""

r = requests.post(url, request_body)

print(r.status_code)
print(r.text)
