## Generated Story -5206863778872974378
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_location
    - utter_goodbye
    - export
	
## Generated Story -3517135655860914028
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

