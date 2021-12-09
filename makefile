validate:
	rasa data validate

train: validate
	rasa train

build: train
	rasa run --enable-api -vv

run-action-server:
	rasa run actions --auto-reload -vv