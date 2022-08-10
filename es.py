import logging

from elasticsearch import Elasticsearch


logging.basicConfig(
    format="{asctime:} | {lineno:4} | {message}",
    style="{",
    datefmt="%Y/%m/%d %H:%M:%S",
    level=logging.INFO,
)
es = Elasticsearch("http://localhost:9200")


def es_query():
    logging.info(es)
    logging.info(es.info())
    logging.info(es.cluster.health())
    logging.info(es.cat.indices())


if __name__ == "__main__":
    logging.info("Started")
    es_query()
