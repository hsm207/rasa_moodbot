val:
	rasa data validate

train:
	rasa train

run-bot: val train
	rasa run \
		--enable-api \
		-vv \
		--cors "*"