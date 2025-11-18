from apps import open_whatsapp, open_youtube, open_word, open_excel, open_browser, open_notepad
from ai_module import ask_ai

def handle(command):
    command = command.lower()

    if "hello" in command:
        return "Hello! How can I help you today?"

    elif "your name" in command:
        return "I am JARVIS, your personal assistant."

    elif "time" in command:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%I:%M %p')}"

    elif "open whatsapp" in command:
        return open_whatsapp()

    elif "open youtube" in command:
        return open_youtube()

    elif "open word" in command or "microsoft word" in command:
        return open_word()

    elif "open excel" in command or "microsoft excel" in command:
        return open_excel()

    elif "open browser" in command or "open google" in command:
        return open_browser()

    elif "open notepad" in command:
        return open_notepad()

    elif "shut down" in command or "exit" in command or "quit" in command:
        return "Shutting down. Goodbye!"

    else:
        # AI fallback for general questions
        return ask_ai(command)
