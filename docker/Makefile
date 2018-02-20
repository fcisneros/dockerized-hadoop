
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


run-ecobici-counts: start
	@docker-compose -f docker-compose.yml -f docker-compose-jobs.yml run ecobici-counts

run-datasets: start  # interactive client with acces to HDFS
	@docker-compose -f docker-compose.yml -f docker-compose-jobs.yml run datasets