# all our imports
import speech_recognition as sr
from time import sleep
from datetime import datetime
import webbrowser
import pyttsx3
import time
import requests

#create an instance of Recognizer class
r = sr.Recognizer()

#confs for pyttsx3
engine = pyttsx3.init()

#speak (text to speech)
def speak(text):
	engine.say(text)
	engine.runAndWait()

#recognize voice and return the text version of it
def recognize_voice():
	text = ''

	#create an instance of the Microphone class
	with sr.Microphone() as source:
	# adjust for ambient noise
		r.adjust_for_ambient_noise(source)
		voice = r.listen(source)

	#recognize
	try:
		text = r.recognize_google(voice)
	except sr.RequestError:
		speak("Sorry, the I can't access the Google API...")
	except sr.UnknownValueError:
		speak("Sorry, Unable to recognize your speech...")
	return text.lower()

#respond function
def reply(text_version):
	print("input: " + text_version)

	#response---------------------------------------------
	# name
	if "name" in text_version:
		speak("My name is pea nuts")

	# how are you?
	if "how are you" in text_version:
		speak("I am chilling")

	# date
	if "date" in text_version:
		date = datetime.now().strftime("%Y-%m-%d")
		speak("The date is " + date)

	# time
	if "time" in text_version:
		time = datetime.now().time().strftime("%H %M")
		speak("The time is " + time)

	#quote
	if "quote" in text_version:
		quotes = ["Shut yo skin tone chicken bone google chrome no home flip phone disowned ice cream cone garden gnome extra chromosome metronome dimmadome genome full blown monochrome student loan indiana jones overgrown flintstone x and y hormone post malone friend zone sylvester stallone hydrocortisone sierra leone autozone professionally seen silver patrone head ass tf up","Eat trash Get cash Slurp ass Die fast","The final stand is wherever I plant my feet. Not one step more. - Saint 14","Death is only the end if you assume the story is about you","When you watch the birds, they watch you too","Sleep like theres nobody watching","I physically cannot stop myself from saying 'bruh moment' whenever i react to anything. What was originally a rather humorous saying has evolved to now an impulsive, uncontrollable behavior that consumes me whenever i have to react to something. From 'holy crap' and omg to 'bruh' all that is said now is 'bruh moment'. 'bruh moment' this 'bruh moment'. my family died. bruh moment. im having the time of my life. bruh moment. i just wanted to be cool and say something original. bruh moment. little did i know the horrors that came from bruh moment. im doomed. bruh moment. this phrase has gotten the best of me. its over for me. bruh moment. bruh sound effect. b r u h m o m e n t. bruh.", "If you’re not dying you’re not living", "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.", "Real gangsta ass niggas dont have to flex nuts, cause real gangsta ass niggas know they got them  -Socrates", "When i raise this sword, so i wish that this poor sinner will receive eternal life.", "When there is no more room in hell, the dead will walk the earth", "Ask the rice for he knows all. But not right now hes busy", "Jeez louise i crave the cheese", "Tell me the name of god you fungal piece of shit", "Too dead to die", "Every second you’re not running, Im only getting closer", "Danger is my bread, and death; my butter", "When tyranny becomes law, resistance becomes duty", "Only dead fish go with the flow", "Cum is stored in the brain, and i have a headache", "If thou gaze long into an abyss, the abyss will also gaze into thee", "Forecast: making it rain", "If a man does not have the sauce,then he is lost. But the same man can be lost in the sauce", "live every day like its your last before you die from a a drive-by crossbow shot at 8:39 tomorrow", "Stand in the ashes of a trillion dead souls and ask the ghosts if honor really matters", "Be polite. Be courteous. Show professionalism and have a plan to kill everyone in the room", "my demons are chasing me and they’re doing the naruto run", "Money doesn’t change people, it unlocks characters which were jailed by poverty", "My crocs have holes so my swag can breathe", "aloha my broha", "Spend fiddies, pet kitties, suck tiddies", "when you’re in hell, only the devil can save you","the blood of the covenant is thicker than the water of the womb","how fleeting are all human passions compared with the massive continuity of ducks","Once you've read the dictionary, every other book you read is just a remix"]
		randQuo = random.randChoice(quotes)
		speak(randQuo)

	#sploch
	if "splotch" in text_version:
		speak("You ever just sploch on a homie")

	#fallacy
	if "fallacy" in text_version:
		speak("When your homie tells you that their minecraft playing cousin is a 12 year old chinese person, and they really aint - Vivian Ren")

	#robust
	if "robust" in text_version:
		speak("No more Mrs. Nice Quesnelle")

	#weather
	if "weather" in text_version:
		base_url = "https://api.openweathermap.org/data/2.5/weather?"
		city_name = "Oakville"
		api_key = "fe0c0c0b7ed26a50c489d78880ae5769"
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name
		response = requests.get(complete_url) 
		x = response.json()
		if x["cod"] != "404": 
			y = x["main"] 
			current_temperature = y["temp"] 
			current_pressure = y["pressure"] 
			current_humidiy = y["humidity"] 
			z = x["weather"] 
			weather_description = z[0]["description"]  

			tempCel = round(int(y["temp"]) - 273.13)
			#await ctx.send(f"Displaying weather for {city_name}:")
			#await ctx.send(f"Current temperature is: {tempCel}")
			#await ctx.send(f"Current weather is: {z[0]['description']}")
			speak(f"In Oakville, the current forecast is {z[0]['description']}, and the current temperature is {tempCel}")

	#utility-------------------------------------------------
	# search google
	if "search" in text_version:
		speak("What do you want me to search for?")
		keyword = recognize_voice()

		# if "keyword" is not empty
		if keyword != '':
		  url = "https://google.com/search?q=" + keyword

		  # webbrowser module to work with the webbrowser
		  speak("Here are the search results for " + keyword)
		  webbrowser.open(url)
		  sleep(3)

	# quit/exit
	if "quit" in text_version or "exit" in text_version:
		speak("Ok, I am gonna head out...")
		exit()

# wait a second for ambient noise

sleep(1)
while True:
	print("-Listening-")
	speak("Listening...")
	# listen for voice and convert it into text format
	text_version = recognize_voice()

	# give "text_version" to reply() 
	reply(text_version)