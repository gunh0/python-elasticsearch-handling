multi7-up:
	docker-compose -f docker-compose.multi-node7.yml up --build -d

multi8-down:
	docker-compose -f docker-compose.multi-node7.yml down

multi8-up:
	docker-compose -f docker-compose.multi-node8.yml up --build -d

multi8-down:
	docker-compose -f docker-compose.multi-node8.yml down

multi8-log:
	docker-compose logs -f docker-compose.multi-node8.yml -f