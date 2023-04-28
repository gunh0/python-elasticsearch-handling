import logging
from elasticsearch import Elasticsearch

logging.basicConfig(
    format="{asctime:} | {lineno:4} | {message}",
    style="{",
    datefmt="%Y/%m/%d %H:%M:%S",
    level=logging.INFO,
)


es = Elasticsearch(
    # "https://localhost:9200", # guide8 use https
    "http://localhost:9200",  # multi-node7 use http
    basic_auth=("elastic", "p@ssw0rd1234"),  # Update with your ELASTIC_PASSWORD
    verify_certs=False,
)


def es_query():
    try:
        logging.info(es)
        logging.info(es.info())
        logging.info(es.cluster.health())
        logging.info(es.cat.indices())
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    logging.info("Started")
    es_query()
