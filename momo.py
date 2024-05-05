from Listen.ListenJs import Listen
import datetime
from Speak.SpeakOffline import Speak
from Commands.commands_control import commandControl

listening = False

def assistant():

    global listening

    while True:
        if not listening:
            bnText = Listen()
            query = bnText.lower()

            if "hey momo" in query:
                Speak("I'm here! What can I do for you?")
                listening = True

        else:
            bnText = Listen()
            query = bnText.lower()

            if "thanks momo" in query:
                Speak("You're welcome! Bye.")
                listening = False
            else:
                res = commandControl(query)
                if res is not None:
                    Speak(res)

    
if __name__ == "__main__":
    assistant()
