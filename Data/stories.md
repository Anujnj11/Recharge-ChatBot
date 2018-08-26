## greet_story
* greet
 - utter_greet


## goodbye_story
* goodbye
 - utter_goodbye
 - action_slot_reset

## story 1
* greet
 - utter_greet
* get_recharge_info {"operator" : "vodafone","plan" : "4g","validity" : "68 days"}
 - get_reacharge_plan
* mobile_number {"clientno" : "9022171228"}
 - should_proceed
* affirm
 - payment_confirm
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye
 - action_slot_reset

## story 2
* greet
 - utter_greet
* get_recharge_info {"operator" : "airtel"}
 - ask_plan_validity
* get_recharge_info {"plan":"4g","validity" : "68 days"}
 - get_reacharge_plan
* mobile_number {"clientno" : "9022171228"}
 - should_proceed
* affirm
 - payment_confirm
* thanks
 - utter_thanks
 - action_slot_reset
* goodbye
 - utter_goodbye
 - action_slot_reset

 ## story 3
* greet
 - utter_greet
* get_recharge_info {"operator" : "vodafone","plan" : "4g","validity" : "68 days"}
 - get_reacharge_plan
* mobile_number {"clientno" : "9022171228"}
 - should_proceed
* deny
 - utter_deny
 - action_slot_reset
 * goodbye
 - utter_goodbye
 - action_slot_reset