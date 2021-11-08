run-action-server:
	rasa run actions -vv --auto-reload

validate:
	rasa data validate

train: validate
	rasa train

build: train
	rasa run --enable-api -vv

test: train
	rasa test core -s tests -vv

