# Elasticsearch 7.x
multi7-up:
	docker-compose -f docker-compose.multi-node7.yml up --build -d

multi7-down:
	docker-compose -f docker-compose.multi-node7.yml down

# Elasticearch 8.x
multi8-up:
	docker-compose -f docker-compose.multi-node8.yml up --build -d

multi8-down:
	docker-compose -f docker-compose.multi-node8.yml down

multi8-log:
	docker-compose logs -f docker-compose.multi-node8.yml -f

# Elasticsearch 8.x from official guide
multi8-guide-up:
	docker-compose -f docker-compose.guide8.yml up --build -d

multi8-guide-down:
	docker-compose -f docker-compose.guide8.yml down

multi8-guide-log:
	docker-compose logs -f docker-compose.guide8.yml -f

# make venv
venv:
	python3 -m venv venv

# run python script
run:
	python es8_guide.py