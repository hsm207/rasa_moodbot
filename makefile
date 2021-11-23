run-action-server:
	rasa run actions -vv --auto-reload

train:
	rasa train

run-shell: train
	rasa shell -vv
