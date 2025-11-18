from tts import speak
import webbrowser
import os
import datetime

# Core command handler
def handle_text(command, speak_response=False):
    command = command.lower()
    response = "Sorry, I did not understand."

    try:
        # --- System Control Commands ---
        if "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            response = "Opening YouTube."
        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            response = "Opening Google."
        elif "open whatsapp" in command:
            os.startfile("C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            response = "Opening WhatsApp."
        elif "open word" in command or "microsoft word" in command:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
            response = "Opening Microsoft Word."
        elif "open chrome" in command:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            response = "Opening Chrome browser."

        # --- Date / Time ---
        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            response = f"The time is {now}."
        elif "date" in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            response = f"Today's date is {today}."

        # --- Simple responses ---
        elif "hello" in command:
            response = "Hello, I am Jarvis. How can I assist you?"
        elif "how are you" in command:
            response = "I’m running smoothly, thank you!"
        elif "shutdown" in command or "exit" in command:
            response = "Shutting down. Goodbye!"
            if speak_response:
                speak(response)
            exit()

        # --- AI-like fallback ---
        elif "what is" in command or "who is" in command or "define" in command:
            import wikipedia
            try:
                summary = wikipedia.summary(command.replace("what is", "").replace("who is", ""), sentences=2)
                response = summary
            except:
                response = "I could not find information about that."

    except Exception as e:
        response = f"Error: {str(e)}"

    if speak_response:
        speak(response)
    return response, True
