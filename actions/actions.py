from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from rasa_sdk.events import SlotSet 

####################################################### Debit Card Flow #############################################################
# Ask Action Functions
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
                        "title": "BAFL Visa Foreign Currency Debit Card",
                        "payload": '/conventional_card_type{"conventional_card_type":"conventional_banking_bafl_visa_foreign_currency_debit_card"}'
                    },
                    {
                        "title": "BAFL Visa Classic Debit Card",
                        "payload": '/conventional_card_type{"conventional_card_type":"conventional_banking_bafl_visa_classic_debit_card"}'
                    },
                    {
                        "title": "BAFL Visa Signature Debit Card",
                        "payload": '/conventional_card_type{"conventional_card_type":"conventional_banking_bafl_visa_signature_debit_card"}'
                    },
                    {
                        "title": "BAFL Visa Platinum Debit Card",
                        "payload": '/conventional_card_type{"conventional_card_type":"conventional_banking_bafl_visa_platinum_debit_card"}'
                    },
                    {
                        "title": "BAFL Visa Gold Debit Card",
                        "payload": '/conventional_card_type{"conventional_card_type":"conventional_banking_bafl_visa_gold_debit_card"}'
                    },
                    {
                        "title": "BAFL Visa Pehchaan Debit Card",
                        "payload": '/conventional_card_type{"conventional_card_type":"conventional_banking_bafl_visa_pehchaan_debit_card"}'
                    },
                    {
                        "title": "BAFL PayPak Classic Debit Card",
                        "payload": '/conventional_card_type{"conventional_card_type":"conventional_banking_bafl_paypak_classic_debit_card"}'
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
                    "title": "Card Limits & Annual Charges",
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
                    "title": "Card Limits & Annual Charges",
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
            options = [

            "Apply for a card",
            "Features & Benefits",
            "Limits & Charges",
            "Talk to AI Assistant"
            ]
            dispatcher.utter_message(text="What would you like to do next?", buttons=[{"title": option, "payload": f"/conventional_card_action{{\"conventional_card_action\":\"{option.lower().replace(' ', '_')}\"}}" } for option in options])
            combined_key = f"{banking_type}/{card_type}/{card_action}"
            dispatcher.utter_message(combined_key)
            SlotSet("conventional_card_action", None)

        elif banking_type == "islamic":
            card_type = tracker.get_slot("islamic_card_type")
            card_action = tracker.get_slot("islamic_card_action")
            options = [
            "Features & Benefits",
            "Limits & Charges",
            "Talk to AI Assistant"
            ]
            dispatcher.utter_message(text="What would you like to do next?", buttons=[{"title": option, "payload": f"/conventional_card_action{{\"conventional_card_action\":\"{option.lower().replace(' ', '_')}\"}}" } for option in options])
            combined_key = f"{banking_type}/{card_type}/{card_action}"
            dispatcher.utter_message(combined_key)
            SlotSet("islamic_card_action", None)

        elif banking_type == "credit_card":
            card_type = tracker.get_slot("credit_card_type")
            card_action = tracker.get_slot("credit_card_action")
            combined_key = f"{banking_type}/{card_type}/{card_action}"
            dispatcher.utter_message(combined_key)
            SlotSet("credit_card_action", None)

        
        
       
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
        
########################################### Credit Card Flow ########################################################
class ActionAskCreditCardType(Action):
    def name(self) -> Text:
        return "action_ask_credit_card_type"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        credit_card_options = [
            "Bank Alfalah Mastercard Optimus Credit Card",
            "Bank Alfalah Visa Platinum  Credit Card",
            "Bank Alfalah Visa Gold Credit Card",
            "Bank Alfalah Visa Classic Credit Card",
            "Bank Alfalah American Express Credit Card",
            "Bank Alfalah Ultra Cashback Credit Card"
        ]
        
        if not tracker.get_slot("credit_card_type"):
            dispatcher.utter_message(
                text="Please select your credit card type:",
                buttons=[{
                    "title": option,
                    "payload": f'/credit_card_type{{"credit_card_type":"{option.lower().replace(" ", "_")}"}}'
                } for option in credit_card_options]
            )
        
        return [SlotSet("banking_type", "credit_card")]
class ActionAskCreditCardAction(Action):
    def name(self) -> Text:
        return "action_ask_credit_card_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        options = [
            "Apply for a card",
            "Features & Benefits",
            "Card Limits & Annual Charges",
            "Talk to AI Assistant"
        ]
        
        if not tracker.get_slot("credit_card_action"):
            dispatcher.utter_message(
                text="What would you like to do next?",
                buttons=[{
                    "title": option,
                    "payload": f'/credit_card_action{{"credit_card_action":"{option.lower().replace(" ", "_").replace("&", "and")}"}}'
                } for option in options]
            )
        
        return []
    
#**************************************************************************************************************************************
class ActionSetCreditCardType(Action):
    def name(self) -> Text:
        return "action_set_credit_card_type"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        card_type = next(tracker.get_latest_entity_values("credit_card_type"), None)
        dispatcher.utter_message(f"DEBUG: Setting credit card type to {card_type}")
        print(f"Setting credit card type slot to: {card_type}")   
        return [SlotSet("credit_card_type", card_type)]


class ActionSetCreditCardAction(Action):
    def name(self) -> Text:
        return "action_set_credit_card_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        card_action = next(tracker.get_latest_entity_values("credit_card_action"), None)
        dispatcher.utter_message(f"DEBUG: Setting credit card action to {card_action}")
        print(f"Setting credit card action slot to: {card_action}")
        
        return [SlotSet("credit_card_action", card_action)]
    
#***********************************************************************************************************************************
#***************************************************Roshan Digital Account *********************************************************
class ActionAskRoshanDigitalAccountType(Action):
    def name(self) -> Text:
        return "action_ask_roshan_digital_account_type"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        rda_options = [
            "Conventional RDA",
            "Islamic RDA"
        ]
        
        if not tracker.get_slot("roshan_digital_account_type"):
            dispatcher.utter_message(
                text="Please select your Roshan Digital Account type:",
                buttons=[{
                    "title": option,
                    "payload": f'/roshan_digital_account_type{{"roshan_digital_account_type":"{option.lower().replace(" ", "_")}"}}'
                } for option in rda_options]
            )
        
        return [SlotSet("banking_type", "roshan_digital_account")]

class ActionAskRoshanDigitalAccountAction(Action):
    def name(self) -> Text:
        return "action_ask_roshan_digital_account_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        options = [
            "Roshan Product",
            "Eligibility Criteria",
            "Features & Benefits",
            "Documents Required",
            "Talk to AI Assistant"
        ]
        
        if not tracker.get_slot("roshan_account_action"):
            dispatcher.utter_message(
                text="What would you like to know about the Roshan Digital Account?",
                buttons=[{
                    "title": option,
                    "payload": f'/roshan_account_action{{"roshan_account_action":"{option.lower().replace(" ", "_").replace("&", "and")}"}}'
                } for option in options]
            )
        
        return []
#*************************************************************************************************************************************
class ActionSetRoshanDigitalAccountType(Action):
    def name(self) -> Text:
        return "action_set_roshan_digital_account_type"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        account_type = next(tracker.get_latest_entity_values("roshan_digital_account_type"), None)
        dispatcher.utter_message(f"DEBUG: Setting Roshan Digital Account type to {account_type}")
        print(f"Setting Roshan Digital Account type slot to: {account_type}")   
        return [SlotSet("roshan_digital_account_type", account_type)]


class ActionSetRoshanDigitalAccountAction(Action):
    def name(self) -> Text:
        return "action_set_roshan_digital_account_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        account_action = next(tracker.get_latest_entity_values("roshan_digital_account_action"), None)
        dispatcher.utter_message(f"DEBUG: Setting Roshan Digital Account action to {account_action}")
        print(f"Setting Roshan Digital Account action slot to: {account_action}")
        
        return [SlotSet("roshan_digital_account_action", account_action)]
    
#**************************************************************************************************************************************
class ActionShowLoanPath(Action):

    def name(self) -> Text:
        return "action_show_loan_path"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        loan_type = tracker.get_slot("loan_type")
        print(loan_type)

        if loan_type == "personal_loan":
            loan_action = tracker.get_slot("personal_loan_action")
            print(loan_action)
            combined_key = loan_action
            dispatcher.utter_message(combined_key)
            [SlotSet("personal_loan_action", None)]  
            options = [
                "Product Offering",
                "Documents Required",
                "Eligibility Criteria",
                "Personal Loan Calculator",
                "Talk to AI Assistant"
            ]
        
            dispatcher.utter_message(
                text="What would you like to know about Personal Loans?",
                buttons=[{
                    "title": option,
                    "payload": f'/personal_loan_action{{"personal_loan_action": "personal_loan/{option.lower().replace(" ", "_").replace("&", "and")}"}}'
                } for option in options]
            )

        elif loan_type == "home_finance":
            loan_action = tracker.get_slot("home_finance_action")
            print(loan_action)
            combined_key = loan_action
            dispatcher.utter_message(combined_key)
            [SlotSet("home_finance_action", None)]
            options = [
                "Policy",
                "Documents Required",
                "Eligibility Criteria",
                "Markup Rates",
                "Apply for Auto Loan",
                "Talk to AI Assistant"
            ]
        
            dispatcher.utter_message(
                text="What would you like to know about Home Finance?",
                buttons=[{
                    "title": option,
                    "payload": f'/home_finance_action{{"home_finance_action": "home_finance/{option.lower().replace(" ", "_").replace("&", "and")}"}}'
                } for option in options]
            )

        elif loan_type == "instant_loan":
            loan_action = tracker.get_slot("instant_loan_action")
            print(loan_action)
            combined_key = loan_action
            dispatcher.utter_message(combined_key)
            [SlotSet("instant_loan_action", None)]
            options = [
                "Product Offering",
                "Documents Required",
                "Eligibility Criteria",
                "Markup Rates",
                "Apply for Auto Loan",
                "Talk to AI Assistant"
            ]
        
            dispatcher.utter_message(
                text="What would you like to know about Instant Loans?",
                buttons=[{
                    "title": option,
                    "payload": f'/instant_loan_action{{"instant_loan_action": "instant_loan/{option.lower().replace(" ", "_").replace("&", "and")}"}}'
                } for option in options]
            )

        elif loan_type == "auto_loan":
            loan_action = tracker.get_slot("auto_loan_action")
            print(loan_action)
            combined_key = loan_action
            dispatcher.utter_message(combined_key)
            [SlotSet("auto_loan_action", None)]
            options = [
                "Product Offering",
                "Documents Required",
                "Eligibility Criteria",
                "Markup Rates",
                "Apply for Auto Loan",
                "Talk to AI Assistant"
            ]
        
            dispatcher.utter_message(
                text="What would you like to know about Auto Loans?",
                buttons=[{
                    "title": option,
                    "payload": f'/auto_loan_action{{"auto_loan_action": "auto_loan/{option.lower().replace(" ", "_").replace("&", "and")}"}}'
                } for option in options]
            )

        return []
#################################################### Types of Loans ############################################################
 #********************************************* Personal Loan ******************************************************************
class ActionAskPersonalLoanAction(Action):
    def name(self) -> Text:
        return "action_ask_personal_loan_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        options = [
            "Product Offering",
            "Documents Required",
            "Eligibility Criteria",
            "Personal Loan Calculator",
            "Talk to AI Assistant"
        ]
        
        if not tracker.get_slot("personal_loan_action"):
            dispatcher.utter_message(
                text="What would you like to know about Personal Loans?",
                buttons=[{
                    "title": option,
                    "payload": f'/personal_loan_action{{"personal_loan_action": "personal_loan/{option.lower().replace(" ", "_").replace("&", "and")}"}}'
                } for option in options]
            )
        
        return [SlotSet("loan_type", "personal_loan")]
        
class ActionSetPersonalLoanAction(Action):
    def name(self) -> Text:
        return "action_set_personal_loan_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        personal_loan_action = next(tracker.get_latest_entity_values("personal_loan_action"), None)
        dispatcher.utter_message(f"DEBUG: Setting Personal Loan action to {personal_loan_action}")
        print(f"Setting Personal Loan action slot to: {personal_loan_action}")
        
        return [SlotSet("personal_loan_action", personal_loan_action)]
#***************************************** Auto Loan***************************************************************************

class ActionAskAutoLoanAction(Action):
    def name(self) -> Text:
        return "action_ask_auto_loan_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        options = [
            "Product Offering",
            "Documents Required",
            "Eligibility Criteria",
            "Markup Rates",
            "Apply for Auto Loan",
            "Talk to AI Assistant"
        ]
        
        if not tracker.get_slot("auto_loan_action"):
            dispatcher.utter_message(
                text="What would you like to know about Auto Loans?",
                buttons=[{
                    "title": option,
                    "payload": f'/auto_loan_action{{"auto_loan_action": "auto_loan/{option.lower().replace(" ", "_").replace("&", "and")}"}}'
                } for option in options]
            )
        
        return [SlotSet("loan_type", "auto_loan")]

class ActionSetAutoLoanAction(Action):
    def name(self) -> Text:
        return "action_set_auto_loan_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        auto_loan_action = next(tracker.get_latest_entity_values("auto_loan_action"), None)
        dispatcher.utter_message(f"DEBUG: Setting Auto Loan action to {auto_loan_action}")
        print(f"Setting Auto Loan action slot to: {auto_loan_action}")
        
        return [SlotSet("auto_loan_action", auto_loan_action)]
#********************************************** Home Finance  *********************************************************************
class ActionAskHomeFinanceAction(Action):
    def name(self) -> Text:
        return "action_ask_home_finance_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        options = [
            "Policy",
            "Documents Required",
            "Eligibility Criteria",
            "Markup Rates",
            "Apply for Auto Loan",
            "Talk to AI Assistant"
        ]
        
        if not tracker.get_slot("home_finance_action"):
            dispatcher.utter_message(
                text="What would you like to know about Home Finance?",
                buttons=[{
                    "title": option,
                    "payload": f'/home_finance_action{{"home_finance_action": "home_finance/{option.lower().replace(" ", "_").replace("&", "and")}"}}'
                } for option in options]
            )
        
        return [SlotSet("loan_type", "home_finance")]

class ActionSetHomeFinanceAction(Action):
    def name(self) -> Text:
        return "action_set_home_finance_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        home_finance_action = next(tracker.get_latest_entity_values("home_finance_action"), None)
        dispatcher.utter_message(f"DEBUG: Setting Home Finance action to {home_finance_action}")
        print(f"Setting Home Finance action slot to: {home_finance_action}")
        
        return [SlotSet("home_finance_action", home_finance_action)]
#********************************************Instant Loan ****************************************************************
class ActionAskInstantLoanAction(Action):
    def name(self) -> Text:
        return "action_ask_instant_loan_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        options = [
            "Product Offering",
            "Documents Required",
            "Eligibility Criteria",
            "Markup Rates",
            "Apply for Auto Loan",
            "Talk to AI Assistant"
        ]
        
        if not tracker.get_slot("instant_loan_action"):
            dispatcher.utter_message(
                text="What would you like to know about Instant Loans?",
                buttons=[{
                    "title": option,
                    "payload": f'/instant_loan_action{{"instant_loan_action": "instant_loan/{option.lower().replace(" ", "_").replace("&", "and")}"}}'
                } for option in options]
            )
        
        return [SlotSet("loan_type", "instant_loan")]

class ActionSetInstantLoanAction(Action):
    def name(self) -> Text:
        return "action_set_instant_loan_action"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        instant_loan_action = next(tracker.get_latest_entity_values("instant_loan_action"), None)
        dispatcher.utter_message(f"DEBUG: Setting Instant Loan action to {instant_loan_action}")
        print(f"Setting Instant Loan action slot to: {instant_loan_action}")
        
        return [SlotSet("instant_loan_action", instant_loan_action)]
