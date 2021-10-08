build:
	docker-compose up -d \
		--remove-orphans
clean:
	docker-compose down --rmi all
	
train:
	rasa train

run-bot: train
	rasa run \
		--enable-api \
		-vv \
		--cors "*"

get-events:
	curl -G "localhost:8000/events/" \
		--data-urlencode "start_date=2021-10-01" \
		--data-urlencode "end_date=2021-10-31"
