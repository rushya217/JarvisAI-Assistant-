import speech_recognition as sr
import pyttsx3

# Text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)   # Speed of speech
engine.setProperty("volume", 1)   # Volume (0.0 to 1.0)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Change index for male/female voice

def speak(text):
    """Convert text to speech"""
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    """Convert speech to text"""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        speak("Network error. Please check your internet connection.")
        return ""
