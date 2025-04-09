# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
# ========================
# 3. Custom Action
# ========================
# actions/actions.py
# actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from rasa_sdk.events import SlotSet 
from actions.form_validation import ValidateBaseForms
#*********************************************Form Actions*****************************************************************************
class ValidateConventionalCardForm(ValidateBaseForms):

    def name(self) -> Text:
        return "validate_conventional_card_form"
    async def extract_conventional_card_type(self, dispatcher: CollectingDispatcher, tracker: Tracker,
                                     domain: Dict[Text, Any]) -> Dict[Text, Any]:
        print("validating card_type")
        return await self.extract_slot_value(tracker, "conventional_card_type")
    
    async def extract_conventional_card_action(self, dispatcher: CollectingDispatcher, tracker: Tracker,
                                     domain: Dict[Text, Any]) -> Dict[Text, Any]:
        print("validating card_action")
        return await self.extract_slot_value(tracker, "conventional_card_action")
    
class ValidateIslamicCardForm(ValidateBaseForms):

    def name(self) -> Text:
        return "validate_islamic_card_form"
    async def extract_islamic_card_type(self, dispatcher: CollectingDispatcher, tracker: Tracker,
                                     domain: Dict[Text, Any]) -> Dict[Text, Any]:
        return await self.extract_slot_value(tracker, "islamic_card_type")
    
    async def extract_islamic_card_action(self, dispatcher: CollectingDispatcher, tracker: Tracker,
                                     domain: Dict[Text, Any]) -> Dict[Text, Any]:
        return await self.extract_slot_value(tracker, "islamic_card_action")
    

    
#***************************************************************************************************************************************
    
########################################## Ask Action Functions ################
class ActionAskMainMenu(Action):
    def name(self) -> Text:
        return "action_ask_main_menu"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        dispatcher.utter_message(
            text="Debit Card Options:\n1. Conventional Banking\n2. Islamic Banking",
            buttons=[
                {"title": "Conventional Banking", "payload": "/inform{\"banking_type\":\"conventional\"}"},
                {"title": "Islamic Banking", "payload": "/inform{\"banking_type\":\"islamic\"}"}
            ]
        )
        return []

class ActionAskConventionalCardType(Action):
    def name(self) -> Text:
        return "action_ask_conventional_card_type"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        print("inside action ask conventional cards")
        dispatcher.utter_message(
            text="Conventional Banking Cards:\n - conventional_banking_bafl_visa_foreign_currency_debit_card\n - conventional_banking_bafl_visa_classic_debit_card\n - conventional_banking_bafl_visa_signature_debit_card\n - conventional_banking_bafl_visa_platinum_debit_card\n - conventional_banking_bafl_visa_gold_debit_card\n - conventional_banking_bafl_visa_pehchaan_debit_card\n - conventional_banking_bafl_paypak_classic_debit_card"
        )
        banking_type="debit_card/conventional_card"
        return[SlotSet("banking_type",banking_type)]
class ActionAskConventionalCardAction(Action):
    def name(self) -> Text:
        return "action_ask_conventional_card_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        dispatcher.utter_message(
            text="Options:\n1. Apply for Card\n2. Features & Benefits\n3. Limits & Charges\n4. Talk to AI",
            buttons=[
                {"title": "Apply for Card", "payload": "request_apply_card"},
                {"title": "Features & Benefits", "payload": "request_features_benefits"},
                {"title": "Limits & Charges", "payload": "request_limits_charges"},
                {"title": "Talk to AI", "payload": "request_ai_assistant"}
            ]
        )
        return []
   
class ActionAskIslamicCardType(Action):
    def name(self) -> Text:
        return "action_ask_islamic_card_type"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        print("inside action ask islamic cards")
        dispatcher.utter_message(
            text="Islamic Banking Cards:\n - bafl_paypak_islamic_classic_debit_card\n - bafl_visa_islamic_signature_card\n - bafl_islamic_power_pack_women_debit_card\n - bafl_islamic_gold_women_debit_card\n - bafl_visa_islamic_foreign_currency_debit_card\n - bafl_islamic_power_pack_signature_debit_card\n - bafl_visa_islamic_classic_debit_card"
        )
        banking_type="debit_card/islamic_card"
        return[SlotSet("banking_type",banking_type)]

 
class ActionAskConventionalActionOptions(Action):
    def name(self) -> Text:
        return "action_ask_islamic_card_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        dispatcher.utter_message(
            text="Options:\n1. Features & Benefits\n2. Limits & Charges\n3. Talk to AI",
            buttons=[
                {"title": "Features & Benefits", "payload": "request_features_benefits"},
                {"title": "Limits & Charges", "payload": "request_limits_charges"},
                {"title": "Talk to AI", "payload": "request_ai_assistant"}
            ]
        )
        return []
    
#*******************************************************************************************************************************
class ActionShowJsonResponse(Action):
    def name(self) -> str:
        return "action_show_json_response"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        banking_type=tracker.get_slot("banking_type")
        if banking_type == "debit_card/conventional_card":
            card_type = tracker.get_slot("conventional_card_type")
            card_action = tracker.get_slot("conventional_card_action")
        else:
            card_type = tracker.get_slot("islamic_card_type")
            card_action = tracker.get_slot("islamic_card_action")


        combined_key = f"{banking_type}/{card_type}/{card_action}"
        dispatcher.utter_message(combined_key)
       

        return []
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class ActionResetSlots(Action):
    def name(self) -> str:
        return "action_reset_slots"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Slots are reset.")
        return [SlotSet(slot, None) for slot in tracker.slots.keys()]
