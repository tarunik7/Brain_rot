import joblib
import numpy as np

model = joblib.load("brainrot_model.pkl")

print("🧠 BrainRot – Social Media Addiction Detector\n")

screen_time = float(input("Daily screen time (in hours): "))
checks_per_hour = int(input("Phone checks per hour: "))
mood_swings = int(input("Mood swings without phone? (1=Yes, 0=No): "))
sleeps_less = int(input("Has sleep reduced? (1=Yes, 0=No): "))
anxiety_level = int(input("Anxiety level (1–5): "))

features = np.array([[screen_time, checks_per_hour, mood_swings, sleeps_less, anxiety_level]])
result = model.predict(features)

if result[0] == 1:
    print("\n🔴 You might be ADDICTED to social media. Time to detox 🧠📵")
else:
    print("\n🟢 You’re in control. Keep it that way! 🚀💪")
