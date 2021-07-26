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

    def _say_something(self, utterance: str, label: str) -> None:
        self.client.post(
            "/webhooks/rest/webhook",
            json={"sender": self.user, "message": utterance},
            name=label,
        )

    @task
    def act_happy(self):
        conv_label = "happy_conv"
        self._say_something("Hello!", label=conv_label)
        self._say_something("I feel great", label=conv_label)
        self._say_something("bye bye", label=conv_label)

    @task
    def act_sad(self):
        conv_label = "sad_conv"
        self._say_something("hi", label=conv_label)
        self._say_something("I am sad", label=conv_label)
        self._say_something("No", label=conv_label)
