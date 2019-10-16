from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
from ruamel import yaml
import os
import smtplib
import re
import string

SLOT_LOCATION = 'location'
SLOT_CUISINE = 'cuisine'
SLOT_EMAIL = 'email'
SLOT_BUDGET = 'budget'
SLOT_CONFIRM_EMAIL_PROMPT = 'confirm_email_prompt'
SLOT_DO_SEND_EMAIL = 'do_send_email'
SLOT_EMAIL_DATA = 'email_data'

UNSUPPORTED_LOCATION = "unsupported_location"
UNSUPPORTED_CUISINE = "unsupported_cuisine"

secrets = yaml.safe_load(open(os.path.join('secrets','secrets.yml')))
zomato_api_key = secrets['zomato_api_key']

# Read the sender email id and password
sender_email = secrets['sender_email']
sender_password = secrets['sender_password']

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurant'

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message("ActionSearchRestaurants.run")
            config={ "user_key":zomato_api_key}
            zomato = zomatopy.initialize_app(config)

            ProcessMultipleInput().normalize_slots(dispatcher, tracker, domain)
            ProcessMultipleInput().run(dispatcher, tracker, domain)

            loc = tracker.get_slot(SLOT_LOCATION)
            cuisine = tracker.get_slot(SLOT_CUISINE)
            budget = tracker.get_slot(SLOT_BUDGET)

            if loc == None or cuisine == None or budget == None:
                dispatcher.utter_message("Please retry. Wrong data.")
                return([])

            if loc == UNSUPPORTED_LOCATION:
                return([SlotSet(SLOT_LOCATION, UNSUPPORTED_LOCATION)])
            if cuisine == UNSUPPORTED_CUISINE:
                return([SlotSet(SLOT_CUISINE, UNSUPPORTED_CUISINE)])

            if budget == "low":
                price_range = range(1, 300)
            elif budget == "medium":
                price_range = range(300, 701)
            else:
                price_range = range(701, 50001)

            criteria = "Location:{0}; Cuisine:{1}; Budget:{2}-{3}".format(
                        loc, cuisine, price_range[0], price_range[-1])
            dispatcher.utter_message("Search Criteria [{0}]".format(criteria))

            location_detail = zomato.get_location(loc, 1)
            d1 = json.loads(location_detail)
            lat = d1["location_suggestions"][0]["latitude"]
            lon = d1["location_suggestions"][0]["longitude"]

            cuisine_code = ProcessCuisine().get_cuisine_code(cuisine)
            results = zomato.restaurant_search("", lat, lon, cuisine_code, 15000)
            d = json.loads(results)

            response_list = []
            if d['results_found'] == 0:
                response= "no results"
            else:
                counter = 1

                for restaurant in d['restaurants']:
                    if restaurant['restaurant']['average_cost_for_two'] in price_range:
                        if counter <= 10:
                            response_list.append("Found " + \
                                restaurant['restaurant']['name'] + " in " + \
                                restaurant['restaurant']['location']['address'] + " with rating " + \
                                restaurant['restaurant']['user_rating']['aggregate_rating'] + \
                                " and average price for two is Rs: " + \
                                str(restaurant['restaurant']['average_cost_for_two'])
                            )
                            counter = counter + 1

            dispatcher.utter_message('Results (in the descending rating order) are')
            for item in response_list[0:5]:
                dispatcher.utter_message(item)

            return([SlotSet(SLOT_EMAIL_DATA, '\n'.join(response_list))])
        except Exception as e:
            dispatcher.utter_message("Please retry. Processing Error: {0}".format(str(e)))
            return([])


class ProcessCuisine():
    def get_cuisine_code(self, cuisine):
        if cuisine == None:
            return None

        cuisines_dict = {'american':1,'chinese':25,'mexican':73,
                'italian':55,'north indian':50,'south indian':85}

        cuisine_l = str(cuisine).lower().strip()
        if cuisine_l not in cuisines_dict.keys():
            return None
        else:
            return str(cuisines_dict.get(cuisine_l))

    def run(self, dispatcher, tracker, domain):
        cuisine = tracker.get_slot(SLOT_CUISINE)
        dispatcher.utter_message("ProcessCuisine.run {0}".format(cuisine))

        if cuisine == None:
            return([])

        if self.get_cuisine_code(cuisine) == None:
            return([SlotSet(SLOT_CUISINE, UNSUPPORTED_CUISINE)])
        else:
            return([SlotSet(SLOT_CUISINE, cuisine)])


class ActionValidateCuisine(Action):
    def name(self):
        return 'action_validate_cuisine'

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message(
                "ActionValidateCuisine.run {0}".format(tracker.get_slot(SLOT_CUISINE)))
            return ProcessCuisine().run(dispatcher, tracker, domain)
        except Exception as e:
            dispatcher.utter_message("Please retry. Processing Error: {0}".format(str(e)))
            return([])

        #return(Utility().rewrite_all_slots(dispatcher, tracker, domain))

class ProcessBudget():
    def run(self, dispatcher, tracker, domain):
        #dispatcher.utter_message("ProcessBudget.run")
        budget_data = tracker.get_slot(SLOT_BUDGET)
        dispatcher.utter_message("ProcessBudget.run {0}".format(budget_data))
        if budget_data == None:
            return([])
        budget_data = budget_data.strip()

        if budget_data in ['low', 'medium', 'high']:
            return [SlotSet(SLOT_BUDGET, budget_data)]

        slot_value = None

        try:
            all_numbers = re.findall("\d+", budget_data)

            if len(all_numbers) == 1 or len(all_numbers) == 2:
                all_numbers_int = [int(x) for x in all_numbers]
                all_numbers_int.sort()

                if len(all_numbers_int) == 1:
                    if all_numbers_int[0] > 0 and all_numbers_int[0] < 300:
                        slot_value = "low"
                    elif all_numbers_int[0] >= 300 and all_numbers_int[0] <= 700:
                        slot_value = "medium"
                    elif all_numbers_int[0] >= 700:
                        slot_value = "high"

                    #dispatcher.utter_message("ProcessBudget.run 1 slot_value {0}".format(slot_value))
                else:
                    if all_numbers_int[1] < 300:
                        slot_value = "low"
                    elif all_numbers_int[1] <= 700:
                        slot_value = "medium"
                    elif all_numbers_int[1] > 700:
                        slot_value = "high"

                    #dispatcher.utter_message("ProcessBudget.run 2 slot_value {0}".format(slot_value))
        except Exception as e:
            dispatcher.utter_message("Please retry. Processing Error: {0}".format(str(e)))
            slot_value = None

        if slot_value == None:
            dispatcher.utter_message("Unable to get budget so assuming budget to be 300 to 700 for 2 people")
            slot_value = "medium"

        #dispatcher.utter_message("ProcessBudget.run Final slot_value {0}".format(slot_value))
        #return(slot_value)
        return([SlotSet(SLOT_BUDGET, slot_value)])

class ActionProcessBudget(Action):
    def name(self):
        return 'action_process_budget'

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message(
                "ActionProcessBudget.run {0}".format(tracker.get_slot(SLOT_BUDGET)))
            return ProcessBudget().run(dispatcher, tracker, domain)
            #slot_value = ProcessBudget().run(dispatcher, tracker, domain)
            #return ([SlotSet(SLOT_BUDGET, slot_value)])
            #dispatcher.utter_message(
            #    "ActionProcessBudget.run {0}".format(tracker.get_slot(SLOT_BUDGET)))
        except Exception as e:
            dispatcher.utter_message("Please retry. Processing Error: {0}".format(str(e)))
            return([])

        #return([])
        #return(Utility().rewrite_all_slots(dispatcher, tracker, domain))


class SendEmail():
    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message("SendEmail.run")

            email_data = tracker.get_slot(SLOT_EMAIL_DATA)
            receiver_email_id = tracker.get_slot(SLOT_EMAIL)
            msg_subject = "{} Restaurant at {}".format(tracker.get_slot('cuisine'), tracker.get_slot('location'))

            msg_data = 'Subject: {}\n\n{}'.format(msg_subject, email_data)

            if email_data == None:
                dispatcher.utter_message("No information available to send")
                return([])
            if receiver_email_id == None:
                dispatcher.utter_message("Email id is not available")
                return([])

            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email_id, msg_data)
            server.close()
            dispatcher.utter_message("Email Sent to:{}".format(receiver_email_id))

        except Exception as e:
            dispatcher.utter_message("Could not send email: {0}".format(str(e)))
            return([])


class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        try:
            #dispatcher.utter_message("ActionSendEmail.run")
            return SendEmail().run(dispatcher, tracker, domain)
        except Exception as e:
            dispatcher.utter_message("Please retry. Processing Error: {0}".format(str(e)))
            return([])


class ValidateLocation():
    def run(self, dispatcher, tracker, domain):
        supported_loc = ['AGRA','AHMEDABAD','AJMER','ALIGARH','ALLAHABAD','AMRAVATI',
        'AMRITSAR','ASANSOL','AURANGABAD','BANGALORE','BAREILLY','BELGAUM','BHAVNAGAR',
        'BHIWANDI','BHOPAL','BHUBANESWAR','BIKANER','BOKARO STEEL CITY',
        'CHANDIGARH','CHENNAI','COIMBATORE','CUTTACK','DEHRADUN','DELHI','DHANBAD',
        'DURG-BHILAI','DURGAPUR','ERODE','FARIDABAD','FIROZABAD','GHAZIABAD','GOA',
        'GORAKHPUR','GULBARGA','GUNTUR','GURGAON','GUWAHATI','GWALIOR','HUBLI-DHARWAD',
        'HYDERABAD','INDORE','JABALPUR','JAIPUR','JALANDHAR','JAMMU','JAMNAGAR',
        'JAMSHEDPUR','JHANSI','JODHPUR','KAKINADA','KANNUR','KANPUR','KOCHI',
        'KOLHAPUR','KOLKATA','KOLLAM','KOTA','KOTTAYAM','KOZHIKODE','KURNOOL',
        'LUCKNOW','LUDHIANA','MADURAI','MALAPPURAM','MANGALORE','MATHURA','MEERUT',
        'MORADABAD','MUMBAI','MYSORE','NAGPUR','NANDED','NASHIK','NELLORE','NOIDA',
        'PALAKKAD','PATNA','PONDICHERRY','PUNE','RAIPUR','RAJAHMUNDRY','RAJKOT',
        'RANCHI','ROURKELA','SALEM','SANGLI','SILIGURI','SOLAPUR','SRINAGAR',
        'SULTANPUR','SURAT','THIRUVANANTHAPURAM','THRISSUR','TIRUCHIRAPPALLI',
        'TIRUNELVELI','TIRUPPUR','UJJAIN','VADODARA','VARANASI',
        'VASAI-VIRAR CITY','VIJAYAPURA','VIJAYAWADA','VISAKHAPATNAM','WARANGAL']

        loc = tracker.get_slot(SLOT_LOCATION)
        #dispatcher.utter_message("ValidateLocation.Run {0}".format(loc))
        if loc == None:
            return([])

        if loc.strip().upper() not in supported_loc:
            return [SlotSet(SLOT_LOCATION, UNSUPPORTED_LOCATION)]
        else:
            return [SlotSet(SLOT_LOCATION, loc.strip())]

class ActionValidateLocation(Action):
    def name(self):
       return 'action_validate_location'

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message(
                "ActionValidateLocation.run {0}".format(tracker.get_slot(SLOT_LOCATION)))
            return ValidateLocation().run(dispatcher, tracker, domain)
        except Exception as e:
            dispatcher.utter_message("Please retry. Processing Error: {0}".format(str(e)))
            return([])

        #all_slots = Utility().rewrite_all_slots(dispatcher, tracker, domain)
        #dispatcher.utter_message("ActionValidateLocation. All slots: {0}".format(all_slots))
        #return(all_slots)


class ProcessMultipleInput():
    def normalize_slots(self, dispatcher, tracker, domain):
        for slot in [SLOT_BUDGET, SLOT_CUISINE, SLOT_EMAIL, SLOT_LOCATION]:
            if tracker.get_slot(slot) != None:
                SlotSet(slot, str(tracker.get_slot(slot)).strip())

    def run(self, dispatcher, tracker, domain):
        values = "Loc:{0}; Cuisine:{1}; Budget:{2}".format(tracker.get_slot(SLOT_LOCATION),
            tracker.get_slot(SLOT_CUISINE), tracker.get_slot(SLOT_BUDGET))
        dispatcher.utter_message("ProcessMultipleInput.run {0}".format(values))

        slots=[]

        if tracker.get_slot(SLOT_LOCATION) != None:
            ValidateLocation().run(dispatcher, tracker, domain)
            slots.append(SlotSet(SLOT_LOCATION, tracker.get_slot(SLOT_LOCATION)))

        if tracker.get_slot(SLOT_CUISINE) != None:
            ProcessCuisine().run(dispatcher, tracker, domain)
            slots.append(SlotSet(SLOT_CUISINE, tracker.get_slot(SLOT_CUISINE)))

        if tracker.get_slot(SLOT_BUDGET) != None:
            ProcessBudget().run(dispatcher, tracker, domain)
            #slot_value = ProcessBudget().run(dispatcher, tracker, domain)
            #SlotSet(SLOT_BUDGET, slot_value)
            slots.append(SlotSet(SLOT_BUDGET, tracker.get_slot(SLOT_BUDGET)))

        return (slots)


class ActionProcessMultipleInput(Action):
    def name(self):
        return("action_multiple_input")

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message("ActionProcessMultipleInput.run")
            ProcessMultipleInput().normalize_slots(dispatcher, tracker, domain)
            return ProcessMultipleInput().run(dispatcher, tracker, domain)
        except Exception as e:
            dispatcher.utter_message("Please retry. Processing Error: {0}".format(str(e)))
            return([])


class ActionConfirmEmailPrompt(Action):
    def name(self):
        return('action_confirm_email_prompt')

    def run(self, dispatcher, tracker, domain):
        try:
            confirm_email_prompt = tracker.get_slot(SLOT_CONFIRM_EMAIL_PROMPT)
            dispatcher.utter_message(
                "ActionProcessEmailPrompt.run {0}".format(confirm_email_prompt))
            do_send_email = False
            if confirm_email_prompt != None:
                confirm_email_prompt = confirm_email_prompt.lower().strip()
                true_values = ['yes','y','true','yeah','ok']
                false_values = ['no','n','not','false']

                if confirm_email_prompt in true_values:
                    do_send_email = True
                elif confirm_email_prompt in false_values:
                    do_send_email = False

            return([SlotSet(SLOT_DO_SEND_EMAIL, do_send_email)])
        except Exception as e:
            dispatcher.utter_message("Please retry. Processing Error: {0}".format(str(e)))
            return([])


class ActionWipeData(Action):
    def name(self):
        return('action_wipe_data')

    def run(self, dispatcher, tracker, domain):
        try:
            values = "Loc:{0}; Cuisine:{1}; Budget:{2}".format(tracker.get_slot(SLOT_LOCATION),
                tracker.get_slot(SLOT_CUISINE), tracker.get_slot(SLOT_BUDGET))
            dispatcher.utter_message("ActionWipeData.run {0}".format(values))

            slots = [SlotSet(SLOT_LOCATION, None),
            SlotSet(SLOT_BUDGET, None),
            SlotSet(SLOT_CUISINE, None),
            SlotSet(SLOT_DO_SEND_EMAIL, None),
            SlotSet(SLOT_CONFIRM_EMAIL_PROMPT, False),
            SlotSet(SLOT_EMAIL, None),
            SlotSet(SLOT_EMAIL_DATA, None)]

            return(slots)

        except Exception as e:
            dispatcher.utter_message("Please retry. Processing Error: {0}".format(str(e)))
            return([])

class Utility():
    def rewrite_all_slots(self, dispatcher, tracker, domain):
        slots = []

        slot_list = [
            SLOT_BUDGET,
            SLOT_CONFIRM_EMAIL_PROMPT,
            SLOT_CUISINE,
            SLOT_DO_SEND_EMAIL,
            SLOT_EMAIL,
            SLOT_EMAIL_DATA,
            SLOT_LOCATION
            ]

        for slot_name in slot_list:
            slots.append(SlotSet(slot_name, tracker.get_slot(slot_name)))

        return(slots)