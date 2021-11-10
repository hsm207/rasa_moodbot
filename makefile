validate:
	rasa data validate -d domain

check-notbug:
	python main.py --domain_folder ./domain/not_bug

check-bug:
	python main.py --domain_folder ./domain/bug

check-workaround:
	python main.py --domain_folder ./domain/workaround