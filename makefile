jupyter:
	jupyter lab --allow-root

build-haystack:
	`git clone https://github.com/deepset-ai/haystack.git || true` && \
		cd haystack && \
		docker-compose pull
