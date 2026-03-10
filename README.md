# 🛡️ Scam Checker: AI-Powered Fraud Prevention

An AI-first web application designed to protect vulnerable populations (such as the elderly) from phishing texts, malicious emails, and digital scams. Users can upload screenshots of suspicious messages, and the app uses multimodal AI to analyze the image, categorize the threat, and provide a highly empathetic, jargon-free safety verdict.

## 🚀 The Problem It Solves
Elderly individuals are prime targets for digital fraud, often receiving texts like *"Your package is delayed, click here"* or *"Your bank account is locked."* This application serves as a safe, accessible digital safety net, allowing users or their caregivers to verify a message's authenticity before clicking any dangerous links.

## 💻 Tech Stack
This project utilizes a modern, decoupled monorepo architecture:

**Frontend (UI)**
* **React.js & Vite:** Lightning-fast, component-driven UI.
* **Custom CSS:** Designed for accessibility (high-contrast colors, large touch targets, clear visual feedback).

**Backend (API & AI)**
* **Python & FastAPI:** High-performance, asynchronous REST API.
* **Google Gemini 2.5 Flash API:** Multimodal generative AI (`google-genai` SDK) prompted to act as a cybersecurity expert returning strict JSON outputs.
* **Pillow (PIL):** In-memory image processing for AI ingestion.

**Database (Storage)**
* **PostgreSQL:** Cloud-hosted relational database for securely logging scan results.
* **SQLAlchemy:** Python ORM for programmatic database schema management and queries.

## 📂 Project Structure
```text
Scam-Checker/
├── main.py                     # FastAPI entry point & API routes
├── database.py                 # PostgreSQL connection & SQLAlchemy engine
├── models.py                   # Database table schemas
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (Git-ignored)
└── scam-checker-frontend/      # React UI App
    ├── src/
    │   ├── App.jsx             # Main React component & API logic
    │   └── App.css             # Accessible styling
    ├── package.json            # Node dependencies
    └── vite.config.js          # Vite configuration
```

## 🛠️ Getting Started (Local Development)

### 1. Clone the Repository

```bash
git clone [https://github.com/muhlikVision/Scam-Checker.git](https://github.com/muhlikVision/Scam-Checker.git)
cd Scam-Checker
```

### 2. Set Up the Backend

Create a `.env` file in the root directory and add your API keys:

```env
GEMINI_API_KEY=your_google_gemini_key_here
DATABASE_URL=postgresql://user:password@hostname/dbname
```

Install dependencies and start the FastAPI server:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
*The backend will be running at `http://localhost:8000`*

### 3. Set Up the Frontend

Open a new terminal window and navigate to the frontend folder:

```bash
cd scam-checker-frontend
npm install
npm run dev
```
*The frontend will be running at `http://localhost:5173`*

## 🔮 Future Enhancements

* **Caregiver Dashboard:** A dedicated view for family members to log in and monitor the types of scams targeting their loved ones based on PostgreSQL database logs.
* **Text Input Fallback:** Allow users to paste raw text instead of just screenshots.
* **Auth Integration:** Implement JWT or OAuth for secure user profiles.

## 📸 App Interface & Features

**Accessible, High-Contrast User Interface**

<img width="756" height="677" alt="image" src="https://github.com/user-attachments/assets/2a955fc9-a118-4459-b4e3-58eba7b0ed32" />

**AI-Powered Scam Detection**

<img width="691" height="779" alt="image" src="https://github.com/user-attachments/assets/01ca9dfb-4133-4e29-ae4d-873848de4c82" />

**Documented FastAPI Backend**

<img width="1289" height="928" alt="image" src="https://github.com/user-attachments/assets/ad7b963e-2c04-45b8-b332-821e4ea2882f" />
