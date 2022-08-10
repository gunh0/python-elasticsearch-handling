from datetime import datetime
from elasticsearch import Elasticsearch

ES_HOST_ADDRESS = "127.0.0.1"
ES_PORT = "9200"
es = Elasticsearch("http://localhost:9200")

doc = {
    "author": "gunh0",
    "text": "Elasticsearch: cool.",
    "timestamp": datetime.now(),
}
resp = es.index(index="test-index", id=1, document=doc)
print(resp["result"])

resp = es.get(index="test-index", id=1)
print(resp["_source"])

es.indices.refresh(index="test-index")

resp = es.search(index="test-index", query={"match_all": {}})
print("Got %d Hits:" % resp["hits"]["total"]["value"])
for hit in resp["hits"]["hits"]:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
