# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import json
from typing import Any, Text, Dict, List

from google.auth.transport import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType, ConversationPaused, ConversationResumed, SessionStarted, ActionExecuted
from rasa_sdk.executor import CollectingDispatcher
# import Constants
# import chatgrpc
# import mChatService_pb2
# import responseObj as robj

class ActionService(Action):

     def name(self) -> Text:
         return "action_service"

     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/Payment{"issue_type":"Payment"}', "title": "నా చెల్లింపు నవీకరించబడలేదు"},
            {"payload":'/Bounce{"issue_type":"Bounce"}', "title": "నా బౌన్స్ లేదా జరిమానా ఛార్జీలను సమీక్షించండి"},
            {"payload":'/Extra{"issue_type":"Extra"}', "title": "నేను అదనపు ఇఎమ్ఐ లేదా ఛార్జీలు చెల్లించాను"},
            {"payload":'/Uninstall{"issue_type":"Uninstall"}', "title": "నేను అప్లికేషన్‌ను అన్‌ఇన్‌స్టాల్ చేయాలనుకుంటున్నాను"},
            {"payload":'/Locked{"issue_type":"Locked"}', "title": "నా పరికరం లాక్ చేయబడింది"},
            {"payload":'/Different', "title": "నేను వేరే సమస్యను ఎదుర్కొంటున్నాను"},
            {"payload": '/Emi{"issue_type":"Emi"}', "title": "ఇఎమ్ఐ చెల్లించడానికి మరింత సమయం కావాలి"},
            {"payload": '/Human{"issue_type":"Human"}', "title": "మనుషులతో మాట్లాడండి"},

        ]
        dispatcher.utter_message(text="దయచేసి మీ సమస్యను ఎంచుకోండి", buttons=buttons)
      

        return []

def syncpayment():
    client = chatgrpc.mChatServiceClient()
    nbfcloandata= mChatService_pb2.mChatPaymentStatusReq()
    nbfcloandata.loanId="DMI0004179099"
    print("SyncPayment")
    result = client.get_payment_status(nbfcloandata)
    print(result)

class CheckLock(Action):

    def name(self) -> Text:
        return "check_lock"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # restext= robj.getStringResponseLoantype(Constants.ACTION_PAYMENT_SYNC,"You have an overdue emi payment. Please make the payment to unlock the phone","Device")
        print(restext)
        dispatcher.utter_message(text= restext)
		#syncpayment()
        return []


class ShowUIOption(Action):

    def name(self) -> Text:
        return "custom_sync"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        isProgress="yes"
        isFreeText="no"
        isSessionEnd="no"
        # restext= robj.getStringResponseUIOptions(Constants.ACTION_PAYMENT_SYNC,isProgress,isFreeText,isSessionEnd)
        restext= "Declaring restext" # added for testing
        print(restext)
        dispatcher.utter_message(text= restext)
        return []


class CheckPersonalPayment(Action):

    def name(self) -> Text:
        return "check_payment_P"

    def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         message="మీ చెల్లింపు నవీకరించబడింది"
         status="success"
        #  status="failed"
         #restext= robj.getStringResponseLoantype(Constants.ACTION_PAYMENT_SYNC,message,"Personal")
         #print(restext)
         dispatcher.utter_message(text= message)
         return [SlotSet("syncstatus", status)]
    

class CheckDevicePayment(Action):

    def name(self) -> Text:
        return "check_payment_D"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      
        message="కొత్త చెల్లింపులు ఏవీ కనుగొనబడలేదు. దయచేసి చెల్లింపు వివరాలను భాగస్వామ్యం చేయండి"
        status="failed" #added for testing
        #restext= robj.getStringResponseLoantype(Constants.ACTION_PAYMENT_SYNC,message,"Device")
        #print(restext)
        dispatcher.utter_message(text= message)
        return [SlotSet("syncstatus", status)]


class ShowDOBOption(Action):

    def name(self) -> Text:
        return "custom_DOB"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        isProgress="no"
        isFreeText="yes"
        isSessionEnd="no"
        # restext= robj.getStringResponseUIOptions(" ",isProgress,isFreeText,isSessionEnd)
        print(restext)
        dispatcher.utter_message(text= restext)
        return []

class ShowEditTest(Action):

    def name(self) -> Text:
        return "user_freetext"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        isProgress="no"
        isFreeText="yes"
        isSessionEnd ="no"
        # restext= robj.getStringResponseUIOptions(" ",isProgress,isFreeText,isSessionEnd)
        print(restext)
        dispatcher.utter_message(text= restext)
        return []


class ActionTalkToHuman(Action):
#     """
# 	human in the loop action
# 	"""
# 
     def name(self):
         return "action_talk_to_human"
# 
     def run(self, dispatcher, tracker, domain):
         response = "Reaching out to a human agent [{}]...".format(tracker.sender_id)
         dispatcher.utter_message(response)

# 
#         """
# 		seems like rasa will stop listening once conversation
# 		is paused, which means no actions are attempted, therefore
# 		preventing triggering ConversationResumed() in a straightforward way.
# 		"""
         paused = tracker.is_paused()
         print("State",paused,tracker.get_slot("handoff_active"))
         handoffstate=tracker.get_slot("handoff_active")
         print("msg",tracker.get_intent_of_latest_message())
         paused = tracker.is_paused()
         print("State",paused)


         slotset=True
         return [ConversationPaused(),SlotSet("handoff_active",slotset)]



class ActionResumeConversation(Action):
    """Just to inform the user that a conversation has resumed.
This will execute upon next user entry after resume"""

    def name(self):
        return "action_resume_conversation"

    async def run(self, dispatcher, tracker, domain) -> List[EventType]:
        logger.info(f"Resumed the conversation")

        sender_id = tracker.sender_id
        paused = tracker.is_paused()
        print("State",paused)
        dispatcher.utter_message(
            f"Resumed this conversation, with ID: " f"{sender_id}."
        )
        slotset=False
        return [ConversationResumed(),SlotSet("handoff_active",slotset)]
        




class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # the session should begin with a `session_started` event
        events = [SessionStarted()]

        isProgress="no"
        isFreeText="no"
        isSessionEnd="yes"
        # restext= robj.getStringResponseUIOptions(" ",isProgress,isFreeText,isSessionEnd)
        print(restext)
        dispatcher.utter_message(text=restext)

        # any slots that should be carried over should come after the
        # `session_started` event


        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events



class ShowPIDOption(Action):

    def name(self) -> Text:
        return "custom_pid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        isProgress="no"
        isFreeText="yes"
        isSessionEnd="no"
        # restext= robj.getStringResponseUIOptions(" ",isProgress,isFreeText,isSessionEnd)
        print(restext)
        dispatcher.utter_message(text= restext)
        return []

class ActionAskDate(Action):
    def name(self) -> Text:
        return "action_ask_Date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="దయచేసి చెల్లింపు తేదీని జోడించండి(dd-mm-yyyy).")
        return []

class ActionAskPid(Action):
    def name(self) -> Text:
        return "action_ask_pid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="దయచేసి చెల్లింపు IDని భాగస్వామ్యం చేయండి")
        return []

class ActionAskAmount(Action):
    def name(self) -> Text:
        return "action_ask_amount"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="చెల్లింపు మొత్తం ఎంత?")
        return []
