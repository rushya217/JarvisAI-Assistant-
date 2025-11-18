import os
import webbrowser

def open_whatsapp():
    # Opens WhatsApp Desktop (if installed)
    try:
        os.startfile("C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
        return "Opening WhatsApp"
    except Exception:
        return "WhatsApp is not installed."

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube"

def open_word():
    try:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
        return "Opening Microsoft Word"
    except Exception:
        return "Microsoft Word is not installed."

def open_excel():
    try:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
        return "Opening Microsoft Excel"
    except Exception:
        return "Microsoft Excel is not installed."

def open_browser():
    webbrowser.open("https://www.google.com")
    return "Opening browser"

def open_notepad():
    os.system("notepad")
    return "Opening Notepad"
