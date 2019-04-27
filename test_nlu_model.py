from rasa_nlu.model import Interpreter
import bot_intents as bi 
import bot_scrapper as bs

model_directory = "./models/nlu/default/stable"
interpreter = Interpreter.load(model_directory)

slots = {
	'location' : '',
}

def nextAction(intent,entities = '',slot_value = ''):
	if entities:
		if slot_value:
			slots[slot_value] = entities
	if intent == 'inform': return bi.inform(slots['location'])
	if intent == 'goodevening' : return bi.goodevening()
	if intent == 'goodmorning' : return bi.goodmorning()
	if intent == 'goodnight' : return bi.goodnight()
	if intent == 'like_agent' : return bi.like_agent()
	if intent == 'fired' : return bi.fired()


def invokeScrapping(text):
	_text =  text.replace(" ","+")
	query = 'https://www.google.com/search?q=' + _text
	response = bs.getResponse(query)
	print(response)


while True:
	raw_data = input(">> ")
	if not raw_data:
		print("**Silence**")
		continue
	data = interpreter.parse(raw_data)
	if data['intent']['name'] != None:
		intent = data['intent']['name']
		if data['entities']:
			entities = data['entities'][0]['value']
			print(entities)
			slot_value = data['entities'][0]['entity']
			print(nextAction(intent,entities,slot_value))
		else:
				print(nextAction(intent))
	else:
		invokeScrapping(data['text'])