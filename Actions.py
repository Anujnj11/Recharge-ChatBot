from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet, AllSlotsReset
import requests
import json
from random import randint
import datetime
import os

class ActionRechargePlan(Action):
    def name(self):
        return 'get_reacharge_plan'

    def run(self,dispatcher,tracker,domain):
        try:
         
            print("User Message : " + tracker.latest_message.text)

            operator = tracker.get_slot('operator')
            print("operator :" + operator)
            
            plan = tracker.get_slot('plan')
            print("plan :" + plan)

            validity = tracker.get_slot('validity')
            print("validity :" + validity)

            dispatcher.utter_message('test')
            return [SlotSet('operator',operator),SlotSet('plan',plan),SlotSet('validity',validity)]
        except Exception:
            print(Exception)
            dispatcher.utter_message("Unable to process your request")
            return [SlotSet('stock_name','')] 





class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 
	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]		


# def run():
#     nse = Nse()
#     isValid = nse.is_valid_code('5PAISA')
#     print(isValid)
#     if isValid == True:
#         response = nse.get_quote('5PAISA')
#         print(response)
#         print("lastPrice: " + str(response["lastPrice"]))
#     else :
#         print('not valid')


# def run():
#         try:
#             # print('Inside get stock')
#             nse = Nse()
#             response = nse.get_top_gainers()
#             print(response)
#             GainerHtml = ''
#             for GainerVal in response:
#                 GainerHtml += "------{}------ \n".format(GainerVal["symbol"]) 
#                 # GainerHtml += "Company Symbol {} \n".format(GainerVal["symbol"])
#                 GainerHtml += "openPrice Rs {} \n".format(GainerVal["openPrice"]) 
#                 GainerHtml += "highPrice Rs {} \n".format(GainerVal["highPrice"]) 
#                 GainerHtml += "lowPrice Rs {} \n".format(GainerVal["lowPrice"]) 
#                 GainerHtml += "Last trading price Rs {} \n".format(GainerVal["ltp"]) 
#                 GainerHtml += "previousPrice Rs {} \n".format(GainerVal["previousPrice"]) 
#                 GainerHtml += "tradedQuantity {} \n".format(GainerVal["tradedQuantity"]) 
#                 GainerHtml += "-------------- \n\n"
            
#             print(GainerHtml)

#         except Exception:
#             print(Exception)
        

# if __name__ == '__main__':
#     # train("./data/nlu_data.json","./config.yml","./models/nlu")
#     run()