validate:
	rasa data validate

train: validate
	rasa train -vv

run: train
	python -m debugpy --listen 0.0.0.0:5678 -m rasa run -vv --enable-api --endpoints endpoints.yml

restart:
	docker-compose down && \
	docker-compose up -d