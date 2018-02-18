
build:
	@docker build -t dockerized/base hadoop-base/
	@docker build -t dockerized/master hadoop-master/
	@docker build -t dockerized/slave hadoop-slave/

run start:
	@docker-compose up -d

stop:
	@docker-compose stop

down destroy:
	@docker-compose down

logs:
	@docker-compose logs -f