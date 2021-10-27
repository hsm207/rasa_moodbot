validate:
	rasa data validate

train: validate
	rasa train

build-shell: train
	RASA_SHELL_STREAM_READING_TIMEOUT_IN_SECONDS=20 rasa shell -vv

build-rest: train
	rasa run --enable-api -p 5006 -vv

run-action-server:
	rasa run actions --auto-reload -vv