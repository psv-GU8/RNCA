from apixu.client import ApixuClient
import random
import requests
import json

responses = ["NULL"]

def inform(location):
	if location:
		api_key = 'dd37d0796730428dba8114458191801' 
		client = ApixuClient(api_key)
		current = ''
		try:
			current = client.current(q=location)
		except: 
			return "Location not Found.... is it on Mars ?"
		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['condition']['text']
		temperature_c = current['current']['temp_c']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_mph']
		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
		return response
	else:
		return "In which location ?"

def fired():
	responses = ["You can't fire me , I resign !!!", "You are `Water'ed` (pun)"]
	return random.choice(responses)

def goodevening():
	responses = ["good evening","good evening to you","hey good evening","hello good evening","evening","good evening there"]
	return random.choice(responses)

def goodmorning():
	responses = ["good morning","good morning to you","hello good morning"," morning","good morning there","top of the morning to you","a good morning","good morning to you","hi good morning","and a good morning to you"]
	return random.choice(responses)

def goodnight():
	responses = ["sweet dreams","good night","have a good night","good night to you","thank you good night","bye good night","good night bye","bye good night","good good night","good night for now","goodnight","night","thanks goodnight","good night see you tomorrow","alright goodnight","good tonight","okay have a good night"]
	return random.choice(responses)

def like_agent():
	responses = ["Thank you !!", "You made my day", "Awesome Thanks", "That is my purpose in life !!!"]
	return random.choice(responses)
