FROM rasa/rasa:2.8.12-full

USER root
# RUN apt update && \
#     apt install -y build-essential \
#         git \
#         python3-dev
        
# RUN pip install rasa-x \
#     --extra-index-url https://pypi.rasa.com/simple \
#     --use-deprecated=legacy-resolver