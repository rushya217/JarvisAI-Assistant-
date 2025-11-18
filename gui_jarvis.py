# from controller import handle
# from speech_module import speak, listen
# import tkinter as tk

# def ask_voice():
#     user_input = listen()
#     if user_input:
#         response = handle(user_input)
#         speak(response)
#         if "shutting down" in response.lower():
#             root.destroy()

# root = tk.Tk()
# root.title("J.A.R.V.I.S. - Voice Assistant")
# root.geometry("400x300")
# root.configure(bg="black")

# tk.Label(root, text="J.A.R.V.I.S", font=("Consolas", 24, "bold"), bg="black", fg="#00FFFF").pack(pady=20)
# tk.Button(root, text="🎤 Speak", command=ask_voice, font=("Consolas", 14), bg="#00FFFF", fg="black").pack(pady=20)

# speak("Hello, I am Jarvis. How can I help you?")
# root.mainloop()


import tkinter as tk
import threading
import time
import math
import requests
from datetime import datetime
from assistant import handle_text
from stt import listen
from tts import speak

# ============ CONFIG ============
WEATHER_API_KEY = "your_openweathermap_api_key"
CITY_NAME = "Nagpur"  # change to your city
# ================================

def get_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={WEATHER_API_KEY}&units=metric"
        data = requests.get(url).json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].capitalize()
        return f"{temp}°C, {desc}"
    except:
        return "Weather Unavailable"

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.R.V.I.S. - Futuristic Assistant")
        self.root.geometry("700x500")
        self.root.configure(bg="black")

        # ========== Header ==========
        tk.Label(root, text="J.A.R.V.I.S", font=("Consolas", 28, "bold"),
                 fg="#00FFFF", bg="black").pack(pady=10)

        # ========== Info Bar ==========
        self.info_label = tk.Label(root, text="", font=("Consolas", 14),
                                   fg="cyan", bg="black")
        self.info_label.pack()

        # ========== Text Area ==========
        self.text_area = tk.Text(root, wrap="word", height=12, width=70,
                                 bg="#0A0A0A", fg="#00FFCC", font=("Consolas", 12))
        self.text_area.pack(pady=15)

        # ========== Dynamic Wave Canvas ==========
        self.canvas = tk.Canvas(root, width=500, height=100, bg="black", highlightthickness=0)
        self.canvas.pack()
        self.wave_phase = 0
        self.animate_wave()

        # ========== Speak Button ==========
        tk.Button(root, text="🎤 Speak", font=("Consolas", 14),
                  bg="#00FFFF", fg="black", command=self.start_listening).pack(pady=10)

        # ========== Update Info (Time + Weather) ==========
        self.update_info()

    def update_info(self):
        now = datetime.now().strftime("%H:%M:%S  |  %A, %d %b %Y")
        weather = get_weather()
        self.info_label.config(text=f"{now}   |   🌦 {weather}")
        self.root.after(60000, self.update_info)  # Update every 60s

    def animate_wave(self):
        self.canvas.delete("wave")
        for x in range(0, 500, 10):
            y = 50 + 30 * math.sin((x / 40) + self.wave_phase)
            self.canvas.create_oval(x, y, x + 5, y + 5, fill="#00FFFF", outline="", tags="wave")
        self.wave_phase += 0.2
        self.root.after(50, self.animate_wave)

    def start_listening(self):
        threading.Thread(target=self._listen_and_process, daemon=True).start()

    def _listen_and_process(self):
        speak("Listening...")
        text = listen()
        if not text:
            self.text_area.insert(tk.END, "❌ Could not understand. Try again.\n")
            return
        self.text_area.insert(tk.END, f"🧠 You: {text}\n", "user")
        resp, was_command = handle_text(text, speak_response=True)
        self.text_area.insert(tk.END, f"🤖 Jarvis: {resp}\n\n", "jarvis")

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisGUI(root)
    root.mainloop()
