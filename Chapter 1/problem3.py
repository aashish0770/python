# problem3.py
# Install the external module with pip and try using it
import pyttsx3

engine = pyttsx3.init()

engine.say(
    "Hi there! I am Aashish Timalsina and I am learning Python programming language."
)
engine.runAndWait()
