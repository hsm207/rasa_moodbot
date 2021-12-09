import asyncio
import inspect
import json
import logging
from asyncio import Queue, CancelledError
from sanic import Blueprint, response
from sanic.request import Request
from typing import Text, Dict, Any, Optional, Callable, Awaitable

import rasa.utils.endpoints
from rasa.core import utils
from rasa.core.channels.channel import (
    UserMessage,
    OutputChannel,
    InputChannel,
)

from rasa.core.channels.rest import RestInput

from sanic.response import HTTPResponse


class CustomRestInput(RestInput):
    @classmethod
    def name(cls) -> Text:
        return "custom_rest"

    def get_metadata(self, request: Request) -> Dict[Text, Any]:
        return request.json["metadata"]
