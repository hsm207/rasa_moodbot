validate:
	rasa data validate

train: validate
	rasa train --force

run-rasa-server: train
	rasa shell -vv

run-action-server:
	rasa run actions -vv --auto-reload

# 🐝 hello I like chinese food 🐝🐝🐝🐝 bye