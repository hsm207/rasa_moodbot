import random
import string
import time

from locust import HttpUser, between, task


class RasaRestUser(HttpUser):
    # wait between 1 and 5 seconds for each task
    wait_time = between(1, 5)

    # where is the rasa server?
    host = "http://localhost:5005"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = "".join(random.choices(string.ascii_letters, k=10))

    def _say_something(self, utterance: str) -> None:
        self.client.post(
            "/webhooks/rest/webhook", json={"sender": self.user, "message": utterance}
        )

    @task
    def act_happy(self):
        self._say_something("Hello!")
        self._say_something("I feel great")
        self._say_something("bye bye")

    @task
    def act_sad(self):
        self._say_something("hi")
        self._say_something("I am sad")
        self._say_something("No")
