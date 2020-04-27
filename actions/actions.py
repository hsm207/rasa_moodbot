from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker 
from rasa_sdk.executor import CollectingDispatcher 
from rasa_sdk.forms import FormAction 
from rasa_sdk import Action

class FacebookMessengerList(Action):

    def name(self) -> Text:

        return "action_fbmessenger_list"

    def run(self,dispatcher,tracker,domain):
        # bt =  { "text":"custom text",
        #         "attachment":{
        #             "type":"image", 
        #             "payload":{
        #                 "url":"http://www.messenger-rocks.com/image.jpg"
        #             }
        #             }
        # }
        bt= {        "attachment":{
                                "type":"template",
                                "payload":{
                                    "template_type":"generic",
                                    "elements":[
                                                {
                                                    "title":"Welcome!",
                                                    "image_url":"https://petersfancybrownhats.com/company_image.png",
                                                    "subtitle":"We have the right hat for everyone.",
                                                    "default_action": {
                                                                        "type": "web_url",
                                                                        "url": "https://petersfancybrownhats.com/view?item=103",
                                                                        "webview_height_ratio": "tall"
                                                                        },
                                                    "buttons":[
                                                    {
                                                        "type":"web_url",
                                                        "url":"https://petersfancybrownhats.com",
                                                        "title":"View Website"
                                                    }            
                                                    ]      
                                                }
                                    ]
                                }
                }
            }
        

        dispatcher.utter_message(text="fb",json_message=bt)
        return []
