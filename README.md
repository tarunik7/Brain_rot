# 🧠 BrainRot: Social Media Addiction Detector

> _“We shape our tools, and thereafter our tools shape us.”_ — Marshall McLuhan  

Hi, I'm Taruni — and I built a small project called **BrainRot**: a **Social Media Addiction Detector**.  
It was created with a simple yet important goal: **to make an impact on people**. The ideology behind it is to quietly bring attention to a growing modern issue, letting users **become aware of their habits and the results of their activity**.  

---

## 📌 Why This Matters

In a world where our screen time often outlasts our sleep time, it's easy to lose track of how subtly yet profoundly social media shapes our mental health.  
Just like you’d check your heart rate after a jog, why not check your digital habits once in a while?  

**BrainRot** lets you do exactly that — **without judgment, just gentle awareness**.

---

## 🚀 Project Overview

**BrainRot** is a simple yet impactful project that:

- Takes in personal digital behavior data  
- Uses a trained **Random Forest Classifier**  
- Predicts whether a person might be addicted to social media  
- Provides a friendly, motivating message encouraging self-awareness  

It comes with both a **Streamlit web app** and a **command-line interface** for flexibility.

---

## 📂 Project Structure

📦 BrainRot/
├── app.py # Streamlit web app
├── predict.py # Command-line predictor script
├── train.py # Model training script
├── brainrot_model.pkl # Saved trained ML model
├── synthetic_dataset.csv # Synthetic data for training
├── requirements.txt # Dependencies list
└── README.md # This documentation


---

## 📊 How It Works

**Inputs:**
- 📱 Daily Screen Time (in hours)
- 🔄 Phone Checks per Hour
- 😵 Mood Swings without Social Media (Yes/No)
- 😴 Sleep Reduction (Yes/No)
- 😰 Anxiety Level (1–5)

**Outputs:**
- 🚨 “You might be addicted”  
- ✅ “You’re in control”

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

git clone https://github.com/tarunik7/Brain_rot
cd brainrot

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Train the Model (Optional)
If you'd like to retrain the model with the synthetic dataset:
python train.py

4️⃣ Run the Web App
streamlit run app.py

5️⃣ Or Use the CLI Tool
python predict.py



🌱 Life Analogy: Why Build This?
Think of it like a speedometer for your digital life.
You wouldn't drive a car without a dashboard — yet many of us scroll endlessly without knowing how fast we're going or when to stop.
BrainRot acts as that dashboard for your digital habits.

🧠 Final Thought
We often underestimate small, daily habits — but they quietly shape our lives. BrainRot isn’t about guilt-tripping users, it’s about empowering people to reflect and reclaim control over their time.
