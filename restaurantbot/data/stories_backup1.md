
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

## Generated Story -1741448597883564725
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_prompt{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget_prompt{"budget": "1600"}
    - slot{"budget": "1600"}
    - action_process_budget
    - slot{"budget": "high"}
    - action_search_restaurant
    - slot{"email_data": "Found Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore with rating 4.9 and average price for two is Rs: 1600\nFound Brew and Barbeque - A Microbrewery Pub in 36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore with rating 4.9 and average price for two is Rs: 1400\nFound The Black Pearl in 20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore with rating 4.9 and average price for two is Rs: 1500\nFound Big Pitcher in LR Arcade,4121, Old Airport Road, Bangalore with rating 4.8 and average price for two is Rs: 2000\nFound House Of Commons in 122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore with rating 4.8 and average price for two is Rs: 1000\n"}
    - utter_ask_email_confirmation
* goodbye
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

## Generated Story 8762898517883390913
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_prompt{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* cuisine_prompt{"location": "mexican"}
    - slot{"location": "mexican"}
    - action_validate_cuisine
    - utter_ask_budget
* budget_prompt{"budget": "600"}
    - slot{"budget": "600"}
    - action_process_budget
    - slot{"budget": "medium"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* confirm_email_prompt{"confirm_email_prompt": "yes"}
    - slot{"confirm_email_prompt": "yes"}
    - utter_ask_email
* email_fetch{"email": "purnendu@gmail.com"}
    - slot{"email": "purnendu@gmail.com"}
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

## Generated Story -5002265239123262928
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_prompt{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget_prompt{"budget": "500"}
    - slot{"budget": "500"}
    - action_process_budget
    - slot{"budget": "medium"}
    - action_search_restaurant
    - slot{"email_data": ""}
    - utter_ask_email_confirmation
* confirm_email_prompt{"confirm_email_prompt": "yes"}
    - slot{"confirm_email_prompt": "yes"}
    - action_confirm_email_prompt
    - slot{"do_send_email": true}
    - utter_ask_email
* email_fetch{"email": "purnendu@gmail.com"}
    - slot{"email": "purnendu@gmail.com"}
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

## Generated Story 355706069323404492_1
* greet
    - utter_greet
* restaurant_search
    - action_multiple_input
    - utter_ask_location
* location_prompt{"location": "in bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* budget_prompt{"budget": "50"}
    - slot{"budget": "50"}
    - action_process_budget
    - slot{"budget": "low"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* confirm_email_prompt{"confrim_email_prompt": "yes"}
    - action_confirm_email_prompt
    - slot{"do_send_email": true}
    - utter_ask_email
* email_fetch{"email": "puru@yahoo.com"}
    - action_send_email
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story AK 355706069323404492_2
* greet
    - utter_greet
* restaurant_search
    - action_multiple_input
    - utter_ask_location
* location_prompt{"location": "in salem"}
    - action_validate_location
    - slot{"location": "salem"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* budget_prompt{"budget": "low"}
    - slot{"budget": "low"}
    - action_process_budget
    - slot{"budget": "low"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* confirm_email_prompt{"confrim_email_prompt": "no"}
    - action_confirm_email_prompt
    - slot{"do_send_email": false}
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story 355706069323404492
* greet
    - utter_greet
* restaurant_search
    - action_multiple_input
    - utter_ask_location
* location_prompt{"location": "In nanded"}
    - action_validate_location
    - slot{"location": "nanded"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* budget_prompt{"budget": "600"}
    - slot{"budget": "600"}
    - action_process_budget
    - slot{"budget": "medium"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* confirm_email_prompt{"confrim_email_prompt": "no"}
    - action_confirm_email_prompt
    - slot{"do_send_email": false}
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story 1993277579540566202
* greet
    - utter_greet
* restaurant_search
    - action_multiple_input
    - utter_ask_location
* location_prompt{"location": "IN delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
	- utter_ask_budget
* budget_prompt{"budget": "high"}
    - slot{"budget": "high"}
    - action_process_budget
    - slot{"budget": "high"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* confirm_email_prompt{"confrim_email_prompt": "yes"}
    - action_confirm_email_prompt
    - slot{"do_send_email": true}
    - utter_ask_email
* email_fetch{"email": "atul.kumar@happiestminds.com"}
    - action_send_email
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story 1993287570540566202
* greet
    - utter_greet
* restaurant_search
    - action_multiple_input
    - utter_ask_location
* location_prompt{"location": "in Patna"}
    - action_validate_location
    - slot{"location": "Patna"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
	- utter_ask_budget
* budget_prompt{"budget": "200 to 250"}
    - slot{"budget": "200 to 250"}
    - action_process_budget
    - slot{"budget": "low"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* confirm_email_prompt{"confrim_email_prompt": "no"}
    - action_confirm_email_prompt
    - slot{"do_send_email": false}
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story -4639179087166749998
* greet
    - utter_greet
* restaurant_search
    - action_multiple_input
    - utter_ask_location
* location_prompt{"location": "In Jaipur"}
    - action_validate_location
    - slot{"location": "Jaipur"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* budget_prompt{"budget": "546"}
    - slot{"budget": "546"}
    - action_process_budget
    - slot{"budget": "medium"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* confirm_email_prompt{"confrim_email_prompt": "yes"}
    - action_confirm_email_prompt
    - slot{"do_send_email": true}
    - utter_ask_email
* email_fetch{"email": "kumarRandom@yahoo.co.in"}
    - action_send_email
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story -4639179088166759998
* greet
    - utter_greet
* restaurant_search
    - action_multiple_input
    - utter_ask_location
* location_prompt{"location": "In Chennai"}
    - action_validate_location
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
	- utter_ask_budget
* budget_prompt{"budget": "734"}
    - slot{"budget": "734"}
    - action_process_budget
    - slot{"budget": "high"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* confirm_email_prompt{"confrim_email_prompt": "no"}
    - action_confirm_email_prompt
    - slot{"do_send_email": false}
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story 4963448062290237512
* greet
    - utter_greet
* location_prompt{"location": "in gurgaon"}
    - action_validate_location
    - slot{"location": "gurgaon"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
	- utter_ask_budget
* budget_prompt{"budget": "low"}
    - slot{"budget": "low"}
    - action_process_budget
    - slot{"budget": "low"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* confirm_email_prompt{"confrim_email_prompt": "yes"}
    - action_confirm_email_prompt
    - slot{"do_send_email": true}
    - utter_ask_email
* email_fetch{"email": "atul.kumr@outlook.co.in"}
    - action_send_email
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story 4923458063290237512
* greet
    - utter_greet
* location_prompt{"location": "In Jodhpur"}
    - action_validate_location
    - slot{"location": "Jodhpur"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
	- utter_ask_budget
* budget_prompt{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_process_budget
    - slot{"budget": "medium"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* confirm_email_prompt{"confrim_email_prompt": "no"}
    - action_confirm_email_prompt
    - slot{"do_send_email": false}
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story -AK_8002713770671756757
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - action_multiple_input
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* budget_prompt{"budget": "1600"}
    - slot{"budget": "1600"}
    - action_process_budget
    - slot{"budget": "high"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* confirm_email_prompt{"confrim_email_prompt": "yes"}
    - action_confirm_email_prompt
    - slot{"do_send_email": true}
    - utter_ask_email
* email_fetch{"email": "atul.kumar@yahoo.com"}
    - action_send_email
- action_wipe_data
    - utter_goodbye
* goodbye
    - export

## Generated Story AK 4356112647709050640
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - action_multiple_input
    - slot{"location": "pune"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* budget_prompt{"budget": "high"}
    - slot{"budget": "high"}
    - action_process_budget
    - slot{"budget": "high"}
    - action_search_restaurant
    - utter_ask_email_confirmation
* confirm_email_prompt{"confrim_email_prompt": "no"}
    - action_confirm_email_prompt
    - slot{"do_send_email": false}
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story AK 5356113647700150620
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - action_multiple_input
    - slot{"location": "pune"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "odiya"}
    - action_validate_cuisine
    - slot{"cuisine": "unsupported_cuisine"}
    - utter_unsupported_cuisine
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story AK 5556116647720150630
* greet
    - utter_greet
* restaurant_search{"cuisine": "kerala"}
    - action_multiple_input
    - slot{"cuisine": "unsupported_cuisine"}
    - utter_unsupported_cuisine
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story AK 9356113649900150620
* greet
    - utter_greet
* restaurant_search{"location": "pune", "cuisine": "bihari"}
    - action_multiple_input
    - slot{"location": "pune", "cuisine": "unsupported_cuisine"}
    - utter_unsupported_cuisine
    - action_wipe_data
    - utter_goodbye
    - export

## Generated Story 3249036703767254124
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_prompt{"location": "salem"}
    - slot{"location": "salem"}
    - action_validate_location
    - slot{"location": "salem"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* budget_prompt{"budget": "312"}
    - slot{"budget": "312"}
    - action_process_budget
    - slot{"budget": "medium"}
    - action_search_restaurant
    - slot{"email_data": "Found Cheesy Juicy Burgers in Santham Shopping Complex, Saradha College Road, Alagapuram Pudur, Salem with rating 0 and average price for two is Rs: 300\nFound Diet Kitchen  in Reliance MegaMall, Five Junction Road Alagapuram, Alagapuram Pudur, Salem with rating 0 and average price for two is Rs: 300\n"}
    - utter_ask_email_confirmation
* confirm_email_prompt{"confirm_email_prompt": "yes"}
    - slot{"confirm_email_prompt": "yes"}
    - action_confirm_email_prompt
    - slot{"do_send_email": true}
    - utter_ask_email
* email_fetch
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

## Generated Story 976046183567373418
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location_prompt{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_validate_location
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* cuisine_prompt{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* budget_prompt{"budget": "600"}
    - slot{"budget": "600"}
    - action_process_budget
    - slot{"budget": "medium"}
    - action_search_restaurant
    - slot{"email_data": "Found My Place Cafe in 1, Sunder Nagar, Girdhar Marg, Malviya Nagar, Jaipur with rating 4.3 and average price for two is Rs: 550\nFound Shack - The Resto Cafe in White Mushroom Jaipur V-Inn, I-7, C - 2, Sindhi Colony, Bani Park, Jaipur with rating 4.2 and average price for two is Rs: 600\nFound Restro NH 11 in 53, Radha Swami Nagar, Iskon Road, Mansarovar, Jaipur with rating 4.1 and average price for two is Rs: 500\nFound Hey Dosa! in Near LBS College, Pandit Devi Shankar Tiwari Marg, Tilak Marg, Raja Park, Jaipur with rating 4.1 and average price for two is Rs: 300\nFound Hey Dosa! in 180, Opposite Talwakars GYM, Rathod Nagar, Amrapali Marg, Vaishali Nagar, Jaipur with rating 4.1 and average price for two is Rs: 500\nFound Vitthal's Kitchen in 29-A, Opposite Laxmi Mandir Cinema, Tonk Road, Jaipur with rating 4.0 and average price for two is Rs: 300\nFound Bayleaf Restaurant in B 222, Vaishali Marg, Vaishali Nagar, Jaipur with rating 4.0 and average price for two is Rs: 400\n"}
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


