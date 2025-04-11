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
        if not tracker.get_slot("islamic_card_type"):
            dispatcher.utter_message(
                text="Islamic Banking Cards:",
                buttons=[
                    {
                        "title": "BAFL PayPak Islamic Classic Debit Card",
                        "payload": '/islamic_card_type{"islamic_card_type":"bafl_paypak_islamic_classic_debit_card"}'
                    },
                    {
                        "title": "BAFL Visa Islamic Signature Card",
                        "payload": '/islamic_card_type{"islamic_card_type":"bafl_visa_islamic_signature_card"}'
                    },
                    {
                        "title": "BAFL Islamic Power Pack Women Debit Card",
                        "payload": '/islamic_card_type{"islamic_card_type":"bafl_islamic_power_pack_women_debit_card"}'
                    },
                    {
                        "title": "BAFL Islamic Gold Women Debit Card",
                        "payload": '/islamic_card_type{"islamic_card_type":"bafl_islamic_gold_women_debit_card"}'
                    },
                    {
                        "title": "BAFL Visa Islamic Foreign Currency Debit Card",
                        "payload": '/islamic_card_type{"islamic_card_type":"bafl_visa_islamic_foreign_currency_debit_card"}'
                    },
                    {
                        "title": "BAFL Islamic Power Pack Signature Debit Card",
                        "payload": '/islamic_card_type{"islamic_card_type":"bafl_islamic_power_pack_signature_debit_card"}'
                    },
                    {
                        "title": "BAFL Visa Islamic Classic Debit Card",
                        "payload": '/islamic_card_type{"islamic_card_type":"bafl_visa_islamic_classic_debit_card"}'
                    }
                ]
            )
        return [SlotSet("banking_type", "islamic")]
 

class ActionAskIslamicCardAction(Action):
    def name(self) -> Text:
        return "action_ask_islamic_card_action"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        if not tracker.get_slot("islamic_card_action"):
            buttons = [
                {
                    "title": "Apply for Card",
                    "payload": '/islamic_card_action{"islamic_card_action":"apply_for_card"}'
                },
                {
                    "title": "Features & Benefits",
                    "payload": '/islamic_card_action{"islamic_card_action":"features_&_benefits"}'
                },
                {
                    "title": "Limits & Charges",
                    "payload": '/islamic_card_action{"islamic_card_action":"limits_&_charges"}'
                },
                {
                    "title": "Talk to AI",
                    "payload": '/islamic_card_action{"islamic_card_action":"ai_assistant"}'
                }
            ]
            
            dispatcher.utter_message(
                text="Please select an action:",
                buttons=buttons
            )

        return []
    
#*******************************************************************************************************************************
class ActionShowJsonResponse(Action):
    def name(self) -> str:
        return "action_show_json_response"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        banking_type=tracker.get_slot("banking_type")
        if banking_type == "conventional":
            card_type = tracker.get_slot("conventional_card_type")
            card_action = tracker.get_slot("conventional_card_action")
        else:
            card_type = tracker.get_slot("islamic_card_type")
            card_action = tracker.get_slot("islamic_card_action")


        combined_key = f"{banking_type}/{card_type}/{card_action}"
        dispatcher.utter_message(combined_key)
        options = [

            "Apply for a card",
            "Features & Benefits",
            "Limits & Charges"

        ]

        dispatcher.utter_message(text="What would you like to do next?", buttons=[{"title": option, "payload": f"/conventional_card_action{{\"conventional_card_action\":\"{option.lower().replace(' ', '_')}\"}}" } for option in options])
       
        return [SlotSet("conventional_card_action", None)]
    
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
        
        
class ActionSetIslamicCardType(Action):
    def name(self) -> Text:
        return "action_set_islamic_card_type"

    async def run(self, dispatcher, tracker, domain):
        print("hello")
        # In any action
        print(f"Current slots: {tracker.slots}")
        card_type = next(tracker.get_latest_entity_values("islamic_card_type"), None)
        dispatcher.utter_message(f"DEBUG: Setting card type to {card_type}")  
        print(card_type+"Hello")
        return [SlotSet("islamic_card_type", card_type)]
    
    
class ActionSetIslamicCardAction(Action):
    def name(self) -> Text:
        return "action_set_islamic_card_action"

    async def run(self, dispatcher, tracker, domain):
        card_action = next(tracker.get_latest_entity_values("islamic_card_action"), None)
        print(card_action)
        dispatcher.utter_message(f"DEBUG: Set action to {card_action}")
        return [SlotSet("islamic_card_action", card_action)]
        
        