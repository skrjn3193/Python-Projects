import speech_recognition as sr
import pyautogui as p
r=sr.Recognizer()
r.energy_threshold=2800
while 1:
    with sr.Microphone() as source:
        print("Say Something")
        audio=r.listen(source,phrase_time_limit=5)
        try:
            speech=r.recognize_google(audio)
            if(speech=="hello"):
               print(p.moveTo(x=20,y=25,duration=3.0))
               p.scroll(clicks,x=2.0,y=4.0)
        except sr.UnknownValueError:
            print("could not understand your spech")
        except sr.RequestError:
            print("could not request result from google")


#py autogui
