train:
	rasa train

test: train
	rasa test -s tests \
		-vv \
		-u /dev/null \
		--fail-on-prediction-errors