📌 Interview Application Tracker

An Interview Application Tracker is a web-based application built using Flask that helps users track their job applications, interview status, and important dates in one place.

This project is designed for beginners to understand how a full-stack Flask project works with authentication, database integration, and basic frontend styling.

🚀 Features

✅ User Registration & Login

🔐 Authentication using Flask-Login

📝 Add job applications

📊 Track application status (Applied, Interview, Selected, Rejected)

📅 Store interview dates

👤 User-specific data (each user sees only their applications)

🎨 Simple UI using HTML & CSS

🗄 Database integration using SQLAlchemy (SQLite/MySQL)

🛠 Tech Stack

Backend

Python

Flask

Flask-Login

Flask-SQLAlchemy

Frontend

HTML

CSS

JavaScript (basic)

Database

SQLite (default)

MySQL (optional)

📂 Project Structure
interview application taracker/
│
├── app.py                  # Main Flask application
├── models.py               # Database models
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignored files
│
├── templates/              # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/                 # Static files
│   ├── css/
│   └── js/
│
└── venv/                   # Virtual environment (ignored in git)

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone <your-repository-url>
cd interview-application-tracker

2️⃣ Create virtual environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python app.py


Open browser and visit:

http://127.0.0.1:5000/

🔑 Environment Variables (Optional)

Create a .env file if needed:

SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///users.db

🧪 Default Workflow

Register a new user

Login to your account

Add job applications

Track interview status & dates

Manage all applications from dashboard

❌ Files to Ignore (Important)

Your .gitignore should include:

venv/
__pycache__/
.env
*.db

🎯 Future Improvements

🔄 Update & delete applications

📧 Email reminders for interviews

📈 Analytics dashboard

🌐 Deployment on Render / Vercel

🎨 Better UI & responsiveness

👨‍💻 Author

Riya Rathod
Beginner Python & Flask Developer
📍 India

📜 License

This project is for learning and educational purposes.

