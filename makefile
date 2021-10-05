train:
	rasa train
	
run-bot: train
	rasa run \
		--enable-api \
		-vv \
		--cors "*"