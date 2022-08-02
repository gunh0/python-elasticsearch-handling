import logging
import os

from dotenv import load_dotenv
from elasticsearch import Elasticsearch


logging.basicConfig(
    format="{asctime:} | {lineno:4} | {message}",
    style="{",
    datefmt="%Y/%m/%d %H:%M:%S",
    level=logging.INFO,
)
load_dotenv()
client = Elasticsearch("http://localhost:9200")


def es_query():
    logging.info(client)
    logging.info(client.info())
    logging.info(client.cluster.health())
    logging.info(client.cat.indices())


if __name__ == "__main__":
    logging.info("Started")
    es_query()
