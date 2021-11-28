validate:
	rasa data validate

train: validate
	rasa train

run-bot: train
	rasa run \
		--enable-api \
		-vv \
		--cors "*"