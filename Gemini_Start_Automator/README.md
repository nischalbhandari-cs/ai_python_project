# AI Task Automator (First AI Project)

Welcome to my first AI-integrated Python project! This tool connects to the Google Gemini 2.0 API 
to take a raw list of tasks and transform them into an organized, prioritized plan.

## 🎓 Learning Journey
As a Computer Science student, I built this project to move beyond basic algorithms and explore real-world API integration.

I collaborated with Google Gemini to:
- Debug connection logic  
- Handle API limits and responses  
- Structure this project professionally  

This is my first AI project, and I learned a lot while building it.

---

## How to Setup & Run

To protect private credentials, the `.env` file is not included in this repository.

### Step 1: Create `.env` file
Create a `.env` file in your project folder and add:

GEMINI_API_KEY=your_actual_key_here  
API_PASSWORD=your_security_password  

---

### Step 2: Create tasks file
Create a file named `tasks.txt` and add your tasks:

Example:
Complete assignment  
Go to gym  
Study algorithms  

---

### Step 3: Run the program
python main.py

---

## ⚠️ Note
The `.env`, `tasks.txt`, and `main.py` should be in the same folder.

---

## 🧠 Code Breakdown: Keywords used in the program

dotenv (load_dotenv)  
A Python library used to load environment variables from a `.env` file.  
It keeps sensitive data like API keys secure.

os.getenv  
Used to retrieve values (like API keys) from environment variables.

genai.configure  
Configures the API by providing your API key so the system can authenticate your requests.

GenerativeModel  
Represents the AI model being used.  
In this project: gemini-2.0-flash (fast and efficient model)

generate_content  
The function that sends your input to the AI and receives a response.

try...except (Error Handling)  
Prevents the program from crashing.  
If something goes wrong (file missing or API error), it shows a message instead.

if __name__ == "__main__":  
The entry point of the program.  
Ensures the script runs only when executed directly.

---

## Final Note
- This is a beginner project created for learning purposes  
- Some parts were developed with the help of AI tools like Google Gemini  

---

## Created By
Nischal Bhandari  
(nischalbhandari-cs)
