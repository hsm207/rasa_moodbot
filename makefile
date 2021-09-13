jupyter:
	jupyter lab --allow-root

build-haystack:
	`git clone --branch v0.9.0 --depth 1 https://github.com/deepset-ai/haystack.git || true` && \
		cd haystack/rest_api/ && \
		awk '{sub(/localhost/,"elasticsearch")}1' pipelines.yaml > pipelines.yaml.bk && \
		cat pipelines.yaml.bk > pipelines.yaml && \
		rm pipelines.yaml.bk && \
		cd .. && \
		awk '{sub(/#image: \"elasticsearch:7.9.2\"/,"image: \"elasticsearch:7.9.2\"")}1' docker-compose.yml > docker-compose.yml.bk && \
		awk '{sub(/image: \"deepset\/elasticsearch-game-of-thrones\"/,"#image: \"deepset/elasticsearch-game-of-thrones\"")}1' docker-compose.yml.bk > docker-compose.yml && \
		rm docker-compose.yml.bk && \
		docker-compose build