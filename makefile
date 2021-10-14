train-bot:
	rasa data validate && \
		rasa train

run-bot: train-bot
	rasa run \
		--enable-api \
		-vv \
		--cors "*"