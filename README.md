# 🌦️ Simple Weather CLI App (Python)

A lightweight Python command-line tool that shows **real-time weather data** for any city using the [OpenWeatherMap API](https://openweathermap.org/api).

---

## 📌 Features
- 🏙️ Get current temperature and weather condition by city name  
- 🔐 Uses a `.env` file to securely store your API key  
- ⚙️ Built with Python and `requests` library  

---

## 📦 Requirements
- Python 3.7+  
- Internet connection  
- OpenWeatherMap API key  

---

## 🚀 Setup

```bash
git clone https://github.com/MohammedAthiq/Simple-Weather-app.git
cd Simple-Weather-app

# (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

### 🔐 Add your API Key

Create a `.env` file in the root directory and add this line:

```env
API_KEY=your_openweather_api_key
```

---

## 🧪 Example

```bash
$ python app.py
Enter city name bruh: Tokyo
Temperature in Tokyo: 25.63°C
Weather Condition: broken clouds
```

---

✅ That’s it! Get weather info from anywhere in the world right in your terminal.

---

## 💾 Save & Push

```bash
git add README.md
git commit -m "Add clean README"
git push
```