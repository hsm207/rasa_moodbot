validate:
	rasa data validate

train: validate
	rasa train --force

run: train
	rasa shell -vv


# 🐝 hello I like chinese food 🐝🐝🐝🐝 bye