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
# class ValidateConventionalCardForm(ValidateBaseForms):

#     def name(self) -> Text:
#         return "validate_conventional_card_form"
#     async def extract_conventional_card_type(self, dispatcher: CollectingDispatcher, tracker: Tracker,
#                                      domain: Dict[Text, Any]) -> Dict[Text, Any]:
#         print("validating card_type")
#         return await self.extract_slot_value(tracker, "conventional_card_type")
    
#     async def extract_conventional_card_action(self, dispatcher: CollectingDispatcher, tracker: Tracker,
#                                      domain: Dict[Text, Any]) -> Dict[Text, Any]:
#         print("validating card_action")
#         return await self.extract_slot_value(tracker, "conventional_card_action")
    
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

    async def run(self, dispatcher, tracker, domain):
      
        dispatcher.utter_message(
            text="Debit Card Options:",
            buttons=[
                {"title": "Conventional", "payload": "/conventional_banking"},
                {"title": "Islamic", "payload": "/islamic_banking"}
            ]
        )
        return []

class ActionAskConventionalCardType(Action):
    def name(self) -> Text:
        return "action_ask_conventional_card_type"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        if not tracker.get_slot("conventional_card_type"):
            dispatcher.utter_message(
                text="Conventional Banking Cards:",
                buttons=[
                    {
                        "title": "BAFL Visa Foreign Currency",
                        "payload": '/conventional_card_type{"conventional_card_type":"foreign_currency"}'
                    },
                    {
                        "title": "BAFL Visa Classic",
                        "payload": '/conventional_card_type{"conventional_card_type":"classic"}'
                    }
                ]
            )
        return [SlotSet("banking_type", "conventional")] 
class ActionAskConventionalCardAction(Action):
    def name(self) -> Text:
        return "action_ask_conventional_card_action"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Reset the 'inform' slot by returning SlotSet
        # reset_inform_slot = SlotSet("inform", None)

        # Check if conventional_card_action is not set
        if not tracker.get_slot("conventional_card_action"):
            buttons = [
                {
                    "title": "Apply for Card",
                    "payload": '/conventional_card_action{"conventional_card_action":"apply_for_card"}'
                },
                {
                    "title": "Features & Benefits",
                    "payload": '/conventional_card_action{"conventional_card_action":"features_&_benefits"}'
                },
                {
                    "title": "Limits & Charges",
                    "payload": '/conventional_card_action{"conventional_card_action":"limits_&_charges"}'
                }
            ]
            
            dispatcher.utter_message(
                text="Please select an action:",
                buttons=buttons
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
        banking_type="islamic_banking"
        return[SlotSet("banking_type",banking_type)]

 
class ActionAskIslamicCardAction(Action):
    def name(self) -> Text:
        return "action_ask_islamic_card_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        
        dispatcher.utter_message(
            text="Options:\n1. Features & Benefits\n2. Limits & Charges\n3. Talk to AI",
            buttons=[
                {"title": "Features & Benefits", "payload": "features_&_benefits"},
                {"title": "Limits & Charges", "payload": "limits_charges"},
                {"title": "Talk to AI", "payload": "ai_assistant"}
            ]
        )
        
        return []
    
#*******************************************************************************************************************************
class ActionShowJsonResponse(Action):
    def name(self) -> str:
        return "action_show_json_response"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        banking_type=tracker.get_slot("banking_type")
        if banking_type == "conventional_card":
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

#********************************************SET SLOTS************************************************************************************


class ActionSetConventionalCardType(Action):
    def name(self) -> Text:
        return "action_set_conventional_card_type"

    async def run(self, dispatcher, tracker, domain):
        print("hello")
        # In any action
        print(f"Current slots: {tracker.slots}")
        card_type = next(tracker.get_latest_entity_values("conventional_card_type"), None)
        dispatcher.utter_message(f"DEBUG: Setting card type to {card_type}")  
        print(card_type+"Hello")
        return [SlotSet("conventional_card_type", card_type)]
    
# class ActionSetBankingType(Action): 
#     def name(self) -> Text: return "action_set_banking_type"

#     async def run(self, dispatcher, tracker, domain):
#         return [SlotSet("banking_type", "conventional_banking")]
    
class ActionSetConventionalCardAction(Action):
    def name(self) -> Text:
        return "action_set_conventional_card_action"

    async def run(self, dispatcher, tracker, domain):
        card_action = next(tracker.get_latest_entity_values("conventional_card_action"), None)
        print(card_action)
        dispatcher.utter_message(f"DEBUG: Set action to {card_action}")
        return [SlotSet("conventional_card_action", card_action)]
        
        