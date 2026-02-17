import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("this is a text to specch feature, it was coded with the help of copilot")
engine.runAndWait()


# this is how we can use pyttsx3 module to convert text to speech in python
