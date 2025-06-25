🔗 Live App: [AI Yoga Recommendor](https://app-gemini-yoga-recomendor.streamlit.app/)



# streamlit-gemini-yoga-recomendation
# 🧘‍♀️ AI Yoga Recommender App

A personalized yoga routine generator and AI-powered assistant built using **Streamlit**, **Gemini Pro/Flash (Google Generative AI)**, and **Python**.

---

## 🌟 Features

- ✅ Personalized yoga plans based on age, goal, and fitness level  
- 💬 Gemini AI integration to answer yoga-related questions  
- 🔐 Secure API key management using `.env`  
- ⚡ Fast, responsive web interface via Streamlit  
- 🌐 Ready for local use or cloud deployment  

---

## 🛠️ Tech Stack

| Tool                | Purpose                           |
|---------------------|------------------------------------|
| Streamlit           | Frontend user interface            |
| google-generativeai | Gemini model integration           |
| dotenv              | Secure API key loading             |
| Python              | Core backend logic                 |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/satyam3824/streamlit-gemini-yoga-recomendation.git
cd yoga-recommender-app

2. Create Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate      # macOS/Linux  
venv\Scripts\activate         # Windows
3. Install Requirements

bash
Copy code
pip install -r requirements.txt

4. Add Gemini API Key
Create a file named .env in the root folder:

ini
Copy code
GEMINI_API_KEY=your-real-gemini-api-key
🗝️ Get your API key from: https://makersuite.google.com/app/apikey

▶️ Run the App
bash
Copy code
streamlit run app.py
