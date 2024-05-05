from Listen.ListenJs import Listen
from Speak.SpeakOffline import Speak
from Commands.commands_control import commandControl

listening = False

def assistant():

    global listening

    while True:
        if not listening:
            bnText = Listen()
            query = bnText.lower()
            
            if "momo" in query:
                query = query.replace("momo", "").strip()
                res = commandControl(query)
                if res is not None:
                    Speak(res)
    
if __name__ == "__main__":
    assistant()
