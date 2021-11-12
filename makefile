validate:
	rasa data validate

train: validate
	rasa train

test: train
	rasa test -s tests -u /dev/null --fail-on-prediction-errors -vv

shell: train
	rasa shell -vv

run-action-server:
	rasa run actions -vv --auto-reload