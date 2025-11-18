import speech_recognition as aj
#import pyttsx3
#import pywhatkit
import datetime
import wikipedia
import webbrowser
import platform
#import smtplib
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")


listener = aj.Recognizer()




#def talk(text):
 #   machine.say(text)
  #  machine.runAndWait()

@app.route("/init", methods=["GET"])
def init():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        response = "Good Morning! I am Jarvis. How may I help you?"
    elif hour >= 12 and hour < 18:
        response = "Good Afternoon! I am Jarvis. How may I help you?"
    else:
        response = "Good Evening! I am Jarvis. How may I help you?"
    return jsonify({"response": response})





    
#def sendEmail(to,content):
#    server=smtplib.SMTP('smtp.gmail.com',587)
#   server.ehlo()
#    server.starttls()
#    server.login("emasil.com","password")
#    server.sendmail("email.com",to,content)
#    server.close()



@app.route("/play_jarvis", methods=["POST"])
def play_jarvis():
    
    data = request.get_json()
    instruction = data.get("command", "").lower()
    url=None
    if "wikipedia" in instruction:
        instruction=instruction.replace("wikipedia"," ")
        content=wikipedia.summary(instruction,1)
        response="According to wikipedia "+ content
        #talk(response)
    elif "play" in instruction:
        song =instruction.replace("play","")
        response="playing" + song
        #talk(response)
        url = f"https://www.youtube.com/results?search_query={song}"

    elif "time" in instruction:
        time=datetime.datetime.now().strftime('%H:%M:%S')
        response="current time is "+time
        #talk(response)

    elif "date" in instruction:
        date=datetime.datetime.now().strftime('%d /%m %Y')
        response="Today's date " + date
        #talk(response)

    elif "how " in instruction:
        response="I am fine , how about you"
        #talk(response)

    elif "what is your name" in instruction:
        response="I am jarvis, what can i do for you"
        #talk(response)

    elif "who is " in instruction:
        person=instruction.replace("who is","")
        info =wikipedia.summary(person,1)
        response=info
        #print(info)
        #talk(info)
    elif "what is" in instruction:
        thing =instruction.replace("what is","")
        info=wikipedia.summary(thing,1)
        response=info
        #talk(info)
    elif "hello" in instruction:
        response="Hey , nice to meet you "
        #talk(response)
    elif "open youtube" in instruction:
        response="opening youtube"
        #talk(response)
        url = "https://www.youtube.com"
    elif "open google" in instruction:
        response="opening google"
        #talk(response)
        url = "https://www.google.com"
        #elif "email to ajay" in instruction:
        #    try:
        #        talk("What should i say")
        #        content=input_instr()
        #        to="sharmaj2529@gmail.com"
        #        sendEmail(to,content)
        #        talk("email has been sent")
        #    except Exception as e:
        #        talk("sorry ... i am not able to send this mail")
        
    else:
        response="please repeat"
        #talk(response)
        
        #print(instruction)
    return jsonify({"response": response, "url":url})
        

if __name__ == "__main__":
    with app.app_context():
        print("Jarvis Flask Backend is running...")
        
        app.run(host="0.0.0.0", port=5000, debug=True)

