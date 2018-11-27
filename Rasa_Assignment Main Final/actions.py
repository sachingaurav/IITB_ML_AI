from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import pandas as pd
from pandas.io.json import json_normalize
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"460ac97844c91afce31963d150eb23b1"}
		zomato = zomatopy.initialize_app(config)
		counter = 1
		loc_list =['AGRA','AJMER','ALIGARH','ALLAHABAD','AMRAVATI','AMRITSAR','ASANSOL','AURANGABAD','BAREILLY','BELGAUM','BHAVNAGAR','BHIWANDI','BHOPAL','BHUBANESWAR','BIKANER','BOKARO STEEL CITY','CHANDIGARH','COIMBATORE','CUTTACK','DEHRADUN','DHANBAD','DURG-BHILAI NAGAR','DURGAPUR','ERODE','FARIDABAD','FIROZABAD','GHAZIABAD','GORAKHPUR','GULBARGA','GUNTUR','GURGAON','GUWAHATI‚ GWALIOR','HUBLI-DHARWAD','INDORE','JABALPUR','JAIPUR','JALANDHAR','JAMMU','JAMNAGAR','JAMSHEDPUR','JHANSI','JODHPUR','KANNUR','KANPUR','KAKINADA','KOCHI','KOTTAYAM','KOLHAPUR','KOLLAM','KOTA','KOZHIKODE','KURNOOL','LUCKNOW','LUDHIANA','MADURAI','MALAPPURAM','MATHURA','GOA','MANGALORE','MEERUT','MORADABAD','MYSORE','NAGPUR','NANDED','NASHIK','NELLORE','NOIDA','PALAKKAD','PATNA','PONDICHERRY','RAIPUR','RAJKOT','RAJAHMUNDRY','RANCHI','ROURKELA','SALEM','SANGLI','SILIGURI','SOLAPUR','SRINAGAR','SULTANPUR','SURAT','THIRUVANANTHAPURAM','THRISSUR','TIRUCHIRAPPALLI','TIRUNELVELI','TIRUPPUR','UJJAIN','VIJAYAPURA','VADODARA','VARANASI','VASAI-VIRAR CITY','VIJAYAWADA','VISAKHAPATNAM','WARANGAL','AHMEDABAD','BANGALORE','CHENNAI','DELHI','HYDERABAD','KOLKATA','MUMBAI','PUNE']
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		prices = tracker.get_slot('price')
		print(loc)
		print(cuisine)
		print(prices)
		r=range(1000,1700)
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon,str(cuisines_dict.get(cuisine)),"",15000)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
			    if restaurant['restaurant']['average_cost_for_two'] in r:
				    if counter <= 5:
				        response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " with rating "+ restaurant['restaurant']['user_rating']['aggregate_rating']+ " and average price for two is Rs: " +  str(restaurant['restaurant']['average_cost_for_two']) +"\n"
				        counter=counter+1
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

class ActionBudget(Action):
#    RANDOMIZE = False

#    def required_fields():
#        return [
#            EntityFormField("budget", "budget"),
#        ]
#    def name(self):
#	    return 'action_price'

#    def run(self, dispatcher, tracker, domain):
#        dispatcher.utter_message("enter  test budget:")
#        result=tracker.latest_message.text
#        return [SlotSet("price", result)]	

    def name(self):
	    return 'action_location'

    def run(self, dispatcher, tracker, domain):
            loc = tracker.get_slot('location')
            loc_list=['AHMEDABAD','BANGALORE','CHENNAI','DELHI','HYDERABAD','KOLKATA','MUMBAI','PUNE']
            if loc.upper() not in loc_list:
                dispatcher.utter_message("We do not operate in that area yet")
#                dispatcher.utter_message("Do you want to search for another location?""hint:Yes :)")
                return []
            else:
                return [SlotSet('location',loc)]