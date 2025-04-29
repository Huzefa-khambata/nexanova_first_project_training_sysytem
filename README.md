# NexaNova Training System

A full-stack web application built with **Flask** that manages trainers and subjects in a training institute.

## 🔧 Features

- Add, view, and delete trainers
- Add and view subjects
- RESTful APIs for CRUD operations
- Basic HTML frontend with dynamic form submission
- Connected to SQLite database

## 🖼️ Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **API Testing**: Postman / Fetch API
- **Version Control**: Git + GitHub

## 📂 Project Structure

nexanova-training-system/ │ ├── app.py # Main Flask backend ├── templates/ # HTML frontend files │ ├── index.html │ ├── add_trainer.html │ ├── view_trainers.html │ ├── add_subject.html │ └── view_subjects.html ├── static/ # CSS files │ └── styles.css ├── nexanova.db # SQLite database file └── README.md



## 📌 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/nexanova_first_project_training_sysytem.git

2. Navigate to the project directory:

cd nexanova_first_project_training_sysytem

3. Install dependencies (optional if using only built-in packages):

pip install flask flask_sqlalchemy

4. Run the Flask server:

python app.py

5. Open your browser at:

http://localhost:5000

📬 API Endpoints (Sample)

Method	Endpoint	Description
POST	/trainer	Add a new trainer
GET	/trainer	Get all trainers
GET	/trainer/<empid>	Get a specific trainer
DELETE	/trainer	Delete a trainer
POST	/subject	Add a new subject
GET	/subject	Get all subjects


👤 Author
Huzefa Khambata
Built as a beginner full-stack project for learning Flask and frontend integration.

🌟 Future Improvements
Add authentication (login/logout)

Add trainer-subject mapping UI

Improve CSS design and responsiveness
