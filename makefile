validate:
	rasa data validate

train: validate
	rasa train

shell: train
	rasa shell -vv

action-server:
	rasa run actions --auto-reload -vv