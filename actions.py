from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker 
from rasa_sdk.executor import CollectingDispatcher 
from rasa_sdk.forms import FormAction 
from rasa_sdk import Action

class FacebookMessengerList(Action):

    def name(self) -> Text:

        return "action_fbmessenger_list"

    def run(self,dispatcher,tracker,domain):
        bt = {
                    "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "list",
                        "top_element_style": "compact",
                        "elements": [
                        {
                            "title": "Classic T-Shirt Collection",
                            "subtitle": "See all our colors",
                            "image_url": "https://i.picsum.photos/id/1000/5626/3635.jpg",          
                            "buttons": [
                            {
                                "title": "View",
                                "type": "web_url",
                                "url": "https://picsum.photos/id/237/200/300",
                                "messenger_extensions": true,
                                "webview_height_ratio": "tall",
                                "fallback_url": "https://picsum.photos/images"            
                            }
                            ]
                        },
                        {
                            "title": "Classic White T-Shirt",
                            "subtitle": "See all our colors",
                            "default_action": {
                            "type": "web_url",
                            "url": "https://picsum.photos/seed/picsum/200/300",
                            "messenger_extensions": false,
                            "webview_height_ratio": "tall"
                            }
                        },
                        {
                            "title": "Classic Blue T-Shirt",
                            "image_url": "https://picsum.photos/200/300.jpg",
                            "subtitle": "100% Cotton, 200% Comfortable",
                            "default_action": {
                            "type": "web_url",
                            "url": "https://i.picsum.photos/id/1005/5760/3840.jpg",
                            "messenger_extensions": true,
                            "webview_height_ratio": "tall",
                            "fallback_url": "https://picsum.photos/images"
                            },
                            "buttons": [
                            {
                                "title": "Shop Now",
                                "type": "web_url",
                                "url": "https://i.picsum.photos/id/1006/3000/2000.jpg",
                                "messenger_extensions": true,
                                "webview_height_ratio": "tall",
                                "fallback_url": "https://picsum.photos/images"            
                            }
                            ]        
                        }
                        ],
                        "buttons": [
                        {
                            "title": "View More",
                            "type": "postback",
                            "payload": "/enquiry"            
                        }
                        ]  
                    }
                    }
                }
        dispatcher.utter_custom_json(bt)
        return []
