
## Generated Story 934254555062669203
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_prompt{"location": "colombo"}
    - slot{"location": "colombo"}
    - action_validate_location
    - slot{"location": "unsupported_location"}
    - utter_unsupported_location
    - action_wipe_data
    - slot{"location": null}
    - slot{"budget": null}
    - slot{"cuisine": null}
    - slot{"do_send_email": null}
    - slot{"confirm_email_prompt": false}
    - slot{"email": null}
    - slot{"email_data": null}
    - utter_goodbye
    - export

## Generated Story 9342543291062669203
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_prompt{"location": "bhind"}
    - slot{"location": "bhind"}
    - action_validate_location
    - slot{"location": "unsupported_location"}
    - utter_unsupported_location
    - action_wipe_data
    - slot{"location": null}
    - slot{"budget": null}
    - slot{"cuisine": null}
    - slot{"do_send_email": null}
    - slot{"confirm_email_prompt": false}
    - slot{"email": null}
    - slot{"email_data": null}
    - utter_goodbye
    - export

## Generated Story -AK 3310983267892
* greet
    - utter_greet
* restaurant_search
    - action_multiple_input
    - slot{"location": "unsupported_cuisine"}
    - utter_unsupported_cuisine
    - action_wipe_data
    - utter_goodbye
    - export
    
## Generated Story 8693208924796927691
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_prompt{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - action_validate_location
    - slot{"location": "jodhpur"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget_prompt{"budget": "900"}
    - slot{"budget": "900"}
    - action_process_budget
    - slot{"budget": "high"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* goodbye
    - action_confirm_email_prompt
    - slot{"do_send_email": false}
    - action_wipe_data
    - slot{"location": null}
    - slot{"budget": null}
    - slot{"cuisine": null}
    - slot{"do_send_email": null}
    - slot{"confirm_email_prompt": false}
    - slot{"email": null}
    - slot{"email_data": null}
    - utter_goodbye
    - export

## Generated Story -1176678374570051187
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_prompt{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* cuisine_prompt
    - action_validate_cuisine
    - utter_unsupported_cuisine
    - action_wipe_data
    - slot{"location": null}
    - slot{"budget": null}
    - slot{"cuisine": null}
    - slot{"do_send_email": null}
    - slot{"confirm_email_prompt": false}
    - slot{"email": null}
    - slot{"email_data": null}
    - utter_goodbye
    - export

## Generated Story 5856995535006609435
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_prompt{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* budget_prompt{"budget": "1000"}
    - slot{"budget": "1000"}
    - action_process_budget
    - slot{"budget": "high"}
    - action_search_restaurant
    - slot{"email_data": "Found Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore with rating 4.9 and average price for two is Rs: 1600\nFound Brew and Barbeque - A Microbrewery Pub in 36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore with rating 4.9 and average price for two is Rs: 1400\nFound Big Pitcher in LR Arcade,4121, Old Airport Road, Bangalore with rating 4.8 and average price for two is Rs: 2000\nFound House Of Commons in 122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore with rating 4.8 and average price for two is Rs: 1000\nFound TBC Sky Lounge in Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore with rating 4.8 and average price for two is Rs: 1000\nFound Biergarten in 2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore with rating 4.8 and average price for two is Rs: 1500\nFound Sea Lions BBQ & Grills in 24, 46th Cross, 5th Block Jayanagar, Bangalore with rating 4.8 and average price for two is Rs: 1100\nFound Truffles in 28, 4th 'B' Cross, Koramangala 5th Block, Bangalore with rating 4.7 and average price for two is Rs: 900\nFound Hammered in 18, Ali Askar Road, Cunningham Road, Bangalore with rating 4.7 and average price for two is Rs: 1000\nFound House Of Commons in 1085, 14th Main, 18th Cross, Sector 3, HSR, Bangalore with rating 4.7 and average price for two is Rs: 1000"}
    - utter_ask_email_confirmation
* confirm_email_prompt{"confirm_email_prompt": "yes"}
    - slot{"confirm_email_prompt": "yes"}
    - action_confirm_email_prompt
    - slot{"do_send_email": true}
    - utter_ask_email
* email_fetch{"email": "atulkr369@gmail.com"}
    - slot{"email": "atulkr369@gmail.com"}
    - action_send_email
    - action_wipe_data
    - slot{"location": null}
    - slot{"budget": null}
    - slot{"cuisine": null}
    - slot{"do_send_email": null}
    - slot{"confirm_email_prompt": false}
    - slot{"email": null}
    - slot{"email_data": null}
    - utter_goodbye
    - export

## Generated Story -1604836761965861698
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "bangalore", "budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bangalore"}
    - action_multiple_input
    - slot{"location": "bangalore"}
    - slot{"cuisine": "mexican"}
    - slot{"budget": "500"}
    - action_process_budget
    - slot{"budget": "medium"}
    - action_search_restaurant
    - slot{"email_data": "Found Onesta in Rooftop, 90/3, Opposite Innovative Multiplex, Beside World of Titan, Outer Ring Road, Marathahalli, Bangalore with rating 4.7 and average price for two is Rs: 600"}
    - utter_ask_email_confirmation
* goodbye
    - action_confirm_email_prompt
    - slot{"do_send_email": false}
    - action_wipe_data
    - slot{"location": null}
    - slot{"budget": null}
    - slot{"cuisine": null}
    - slot{"do_send_email": null}
    - slot{"confirm_email_prompt": false}
    - slot{"email": null}
    - slot{"email_data": null}
    - utter_goodbye
    - export

## Generated Story -2090901030876798210
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "bangalore", "budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bangalore"}
    - action_multiple_input
    - slot{"location": "bangalore"}
    - slot{"cuisine": "mexican"}
    - slot{"budget": "500"}
    - action_process_budget
    - slot{"budget": "medium"}
    - action_search_restaurant
    - slot{"email_data": "Found Onesta in Rooftop, 90/3, Opposite Innovative Multiplex, Beside World of Titan, Outer Ring Road, Marathahalli, Bangalore with rating 4.7 and average price for two is Rs: 600"}
    - utter_ask_email_confirmation
* confirm_email_prompt{"confirm_email_prompt": "yes"}
    - slot{"confirm_email_prompt": "yes"}
    - action_confirm_email_prompt
    - slot{"do_send_email": true}
    - utter_ask_email
* email_fetch{"email": "atulkr369@gmail.com"}
    - slot{"email": "atulkr369@gmail.com"}
    - action_send_email
    - action_wipe_data
    - slot{"location": null}
    - slot{"budget": null}
    - slot{"cuisine": null}
    - slot{"do_send_email": null}
    - slot{"confirm_email_prompt": false}
    - slot{"email": null}
    - slot{"email_data": null}
    - utter_goodbye
    - export

## Generated Story 7327810558115051164
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - action_multiple_input
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget_prompt{"budget": "1600"}
    - slot{"budget": "1600"}
    - action_process_budget
    - slot{"budget": "high"}
    - action_search_restaurant
    - slot{"email_data": "Found Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore with rating 4.9 and average price for two is Rs: 1600\nFound Brew and Barbeque - A Microbrewery Pub in 36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore with rating 4.9 and average price for two is Rs: 1400\nFound The Black Pearl in 20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore with rating 4.9 and average price for two is Rs: 1500\nFound Big Pitcher in LR Arcade,4121, Old Airport Road, Bangalore with rating 4.8 and average price for two is Rs: 2000\nFound House Of Commons in 122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore with rating 4.8 and average price for two is Rs: 1000\nFound TBC Sky Lounge in Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore with rating 4.8 and average price for two is Rs: 1000\nFound AB's - Absolute Barbecues in 90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore with rating 4.8 and average price for two is Rs: 1400\nFound Biergarten in 2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore with rating 4.8 and average price for two is Rs: 1500\nFound The Globe Grub in 2nd Floor, Soul Space Paradigm,\nLandmark- Next to Innovative Multiplex, Above Bata Showroom, Outer Ring Road Marathahalli, Bangalore with rating 4.8 and average price for two is Rs: 1300\nFound AB's - Absolute Barbecues in 100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore with rating 4.8 and average price for two is Rs: 1400"}
    - utter_ask_email_confirmation
* confirm_email_prompt{"confirm_email_prompt": "yes"}
    - slot{"confirm_email_prompt": "yes"}
    - action_confirm_email_prompt
    - slot{"do_send_email": true}
    - utter_ask_email
* email_fetch{"email": "atulkr369@gmail.com"}
    - slot{"email": "atulkr369@gmail.com"}
    - action_send_email
    - action_wipe_data
    - slot{"location": null}
    - slot{"budget": null}
    - slot{"cuisine": null}
    - slot{"do_send_email": null}
    - slot{"confirm_email_prompt": false}
    - slot{"email": null}
    - slot{"email_data": null}
    - utter_goodbye
    - export

## Generated Story 7327810558115051164
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - action_multiple_input
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget_prompt{"budget": "1600"}
    - slot{"budget": "1600"}
    - action_process_budget
    - slot{"budget": "high"}
    - action_search_restaurant
    - slot{"email_data": "Found Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore with rating 4.9 and average price for two is Rs: 1600\nFound Brew and Barbeque - A Microbrewery Pub in 36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore with rating 4.9 and average price for two is Rs: 1400\nFound The Black Pearl in 20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore with rating 4.9 and average price for two is Rs: 1500\nFound Big Pitcher in LR Arcade,4121, Old Airport Road, Bangalore with rating 4.8 and average price for two is Rs: 2000\nFound House Of Commons in 122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore with rating 4.8 and average price for two is Rs: 1000\nFound TBC Sky Lounge in Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore with rating 4.8 and average price for two is Rs: 1000\nFound AB's - Absolute Barbecues in 90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore with rating 4.8 and average price for two is Rs: 1400\nFound Biergarten in 2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore with rating 4.8 and average price for two is Rs: 1500\nFound The Globe Grub in 2nd Floor, Soul Space Paradigm,\nLandmark- Next to Innovative Multiplex, Above Bata Showroom, Outer Ring Road Marathahalli, Bangalore with rating 4.8 and average price for two is Rs: 1300\nFound AB's - Absolute Barbecues in 100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore with rating 4.8 and average price for two is Rs: 1400"}
    - utter_ask_email_confirmation
* confirm_email_prompt{"confirm_email_prompt": "no"}
    - slot{"confirm_email_prompt": "no"}
    - action_confirm_email_prompt
    - slot{"do_send_email": false}
    - action_wipe_data
    - slot{"location": null}
    - slot{"budget": null}
    - slot{"cuisine": null}
    - slot{"do_send_email": null}
    - slot{"confirm_email_prompt": false}
    - slot{"email": null}
    - slot{"email_data": null}
    - utter_goodbye
    - export



