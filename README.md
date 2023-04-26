# Elasticsearch Docker Compose & Python Client Testbed

> This is a sample project that demonstrates how to set up an Elasticsearch cluster using Docker Compose. The project consists of a set of Docker Compose files that can be used to deploy Elasticsearch on a single node or on multiple nodes.

<br/>

### Prerequisites

Before running the project, you must have the following software installed on your system:

-   Docker Engine
-   Docker Compose

<br/>

### Installation

```bash
# Create isolated Python environments
python3 -m pip install virtualenv
python3 -m virtualenv venv

# Activation
source ./venv/bin/activate
pip3 install -r requirements.txt

# Output installed packages in requirements format
pip freeze > requirements.txt
```

```bash
# Set up & Run ES
docker-compose up -d

# Stops containers and remove containers
docker-compose down
docker-compose rm
```

<br/>

### Usage

-   `Makefile`

```bash
multi7-up:
	docker-compose -f docker-compose.multi-node7.yml up --build -d

multi7-down:
	docker-compose -f docker-compose.multi-node7.yml down

multi8-up:
	docker-compose -f docker-compose.multi-node8.yml up --build -d

multi8-down:
	docker-compose -f docker-compose.multi-node8.yml down

multi8-log:
	docker-compose logs -f docker-compose.multi-node8.yml -f

multi-guide:
	docker-compose -f docker-compose.guide8.yml up --build -d
```

-   `es.py` : This script creates an index in Elasticsearch, adds a document to the index, and searches for the document. If Elasticsearch is running correctly, the script should output the results of the search.

<br/>
### Reference

-   For more information about how to use Elasticsearch with Docker, see the official Elasticsearch Docker documentation: https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
