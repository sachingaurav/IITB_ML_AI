## Generated Story -4933789856182862093
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "cheap"}
    - slot{"price": "cheap"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

