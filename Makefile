multi-up:
	docker-compose -f docker-compose.multi-node8.yml up --build

multi-down:
	docker-compose -f docker-compose.multi-node8.yml down

multi-log:
	docker-compose logs -f docker-compose.multi-node.yml -f