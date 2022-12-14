PATH_PREFIX=~

create-topics:
	docker exec broker \
  kafka-topics --create --if-not-exists \
    --topic monitor \
    --bootstrap-server localhost:9192 \
    --replication-factor 1 \
    --partitions 1
	docker exec broker \
  kafka-topics --create --if-not-exists \
    --topic drone_status\
    --bootstrap-server localhost:9192 \
    --replication-factor 1 \
    --partitions 1
	docker exec broker \
  kafka-topics --create --if-not-exists \
    --topic flying_control \
    --bootstrap-server localhost:9192 \
    --replication-factor 1 \
    --partitions 1
		docker exec broker \
  kafka-topics --create --if-not-exists \
    --topic control_center \
    --bootstrap-server localhost:9192 \
    --replication-factor 1 \
    --partitions 1
	docker exec broker \
  kafka-topics --create --if-not-exists \
    --topic inertial_navigation \
    --bootstrap-server localhost:9192 \
    --replication-factor 1 \
    --partitions 1
	docker exec broker \
  kafka-topics --create --if-not-exists \
    --topic mobile_connection \
    --bootstrap-server localhost:9192 \
    --replication-factor 1 \
    --partitions 1
	docker exec broker \
  kafka-topics --create --if-not-exists \
    --topic situation_control \
    --bootstrap-server localhost:9192 \
    --replication-factor 1 \
    --partitions 1
	docker exec broker \
  kafka-topics --create --if-not-exists \
    --topic sprayer_control \
    --bootstrap-server localhost:9192 \
    --replication-factor 1 \
    --partitions 1

sys-packages:
	# sudo apt install -y docker-compose
	sudo apt install python3-pip -y
	sudo pip install pipenv

broker:
	docker-compose -f kafka/docker-compose.yaml up -d

pipenv:
	pipenv install -r requirements.txt

prepare: sys-packages pipenv build run-broker

prepare-screen:
	# WSL specific preparation
	sudo /etc/init.d/screen-cleanup start


run-screen: broker run-monitor-screen run-drone-screen run-mobile-screen run-control_center-screen

build:
	docker-compose build

run-broker:
	docker-compose up -d zookeeper broker

run:
	docker-compose up -d

restart:
	docker-compose restart

stop-app:
	pkill flask

restart-app: stop-app run


run-monitor-screen:
	screen -dmS monitor bash -c "cd $(PATH_PREFIX)/secure-drone/; pipenv run ./monitor/monitor.py config.ini"

run-monitor:
	cd $(PATH_PREFIX)/secure-drone/; pipenv run ./monitor/monitor.py config.ini

run-drone:
	cd $(PATH_PREFIX)/secure-drone; pipenv run drone/drone.py config.ini

run-drone-screen:
	screen -dmS drone bash -c "cd $(PATH_PREFIX)/secure-drone; pipenv run drone/drone.py config.ini"

run-mobile:
	cd $(PATH_PREFIX)/secure-drone; pipenv run mobile/mobile.py config.ini

run-mobile-screen:
	screen -dmS mobile bash -c "cd $(PATH_PREFIX)/secure-drone; pipenv run mobile/mobile.py config.ini"

run-control_center:
	cd $(PATH_PREFIX)/secure-drone; pipenv run control_center/control_center.py config.ini

run-control_center-screen:
	screen -dmS control_center bash -c "cd $(PATH_PREFIX)/secure-drone; pipenv run control_center/control_center.py config.ini"

test:
	pytest -sv