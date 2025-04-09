from typing import Text, List, Any, Dict
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk import FormValidationAction
from datetime import datetime

class ValidateBaseForms(FormValidationAction):
    def name(self) -> Text:
        print("namefunction")
        return "validate_base_forms"
    
    async def extract_slot_value(self, tracker: Tracker, slot_name: Text) -> Dict[Text, Any]:
        print("extract slot")
        if tracker.get_slot(slot_name) is None and tracker.get_slot("requested_slot") == slot_name:
            if tracker.latest_message and tracker.latest_message.get('text'):
                return {slot_name: tracker.latest_message['text']}
        return {}
    
    async def validate_conventional_card_type(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        print("inside validate_card_type")
        return {"conventional_card_type": slot_value} 
    
    async def validate_conventional_card_action(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        print("inside validatecon_card _action")
        return {"conventional_card_action": slot_value} 

    async def validate_islamic_card_type(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        print("inside validate_card_type_islamic_type")
        return {"islamic_card_type": slot_value} 
    
    async def validate_islamic_card_action(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        print("inside validate_islamic_action")
        return {"islamic_card_action": slot_value} 
 