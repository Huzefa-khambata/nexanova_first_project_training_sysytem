from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nexanova.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating the database object
db = SQLAlchemy(app)

# Home Page
@app.route('/')
def home_page():
    return render_template('index.html')

# Add Trainer Page
@app.route('/add-trainer')
def add_trainer_page():
    return render_template('add_trainer.html')

# View Trainers Page
@app.route('/view-trainers')
def view_trainers_page():
    return render_template('view_trainers.html')

# Add Subject Page
@app.route('/add-subject')
def add_subject_page():
    return render_template('add_subject.html')

# View Subjects Page
@app.route('/view-subjects')
def view_subjects_page():
    return render_template('view_subjects.html')


# Define the Trainer model
class Trainer(db.Model):
    empid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    subject_id = db.Column(db.Integer, nullable=False)

# Define the Subject model
class Subject(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(50), nullable=False)

# Create database tables (after defining all models)
with app.app_context():
    db.create_all()

# Home Route
@app.route('/')
def home():
    return "Welcome to NexaNova Training System!"

# API to Add Trainer
@app.route('/trainer', methods=['POST'])
def add_trainer():
    data = request.get_json()
    new_trainer = Trainer(
        empid=data['empid'],
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        subject_id=data['subject_id']
    )
    db.session.add(new_trainer)
    db.session.commit()
    return jsonify({"message": "Trainer added successfully!"}), 201

# API to Get All Trainers
@app.route('/trainer', methods=['GET'])
def get_trainers():
    trainers = Trainer.query.all()
    result = []
    for trainer in trainers:
        trainer_data = {
            'empid': trainer.empid,
            'name': trainer.name,
            'email': trainer.email,
            'phone': trainer.phone,
            'subject_id': trainer.subject_id
        }
        result.append(trainer_data)
    return jsonify(result), 200

# API to Add Subject
@app.route('/subject', methods=['POST'])
def add_subject():
    data = request.get_json()

    # Input validation
    if not data or 'subject_id' not in data or 'subject_name' not in data:
        return jsonify({"error": "Missing subject_id or subject_name"}), 400

    # Check for duplicate subject_id
    existing_subject = Subject.query.get(data['subject_id'])
    if existing_subject:
        return jsonify({"error": "Subject ID already exists"}), 409

    # Create and add new subject
    new_subject = Subject(
        subject_id=data['subject_id'],
        subject_name=data['subject_name']
    )
    db.session.add(new_subject)
    db.session.commit()

    return jsonify({"message": "Subject added successfully!"}), 201

# API to Get All Subjects
@app.route('/subject', methods=['GET'])
def get_subjects():
    subjects = Subject.query.all()
    result = []
    for subject in subjects:
        subject_data = {
            'subject_id': subject.subject_id,
            'subject_name': subject.subject_name
        }
        result.append(subject_data)
    return jsonify(result), 200

@app.route('/trainer', methods=['DELETE'])
def delete_trainer():
    data = request.get_json()

    if not data or 'empid' not in data:
        return jsonify({"error": "Missing empid"}), 400

    trainer = Trainer.query.get(data['empid'])
    if not trainer:
        return jsonify({"error": "Trainer not found"}), 404

    db.session.delete(trainer)
    db.session.commit()

    return jsonify({"message": "Trainer deleted successfully!"}), 200

@app.route('/trainer/<int:empid>', methods=['GET'])
def get_trainer_by_id(empid):
    trainer = Trainer.query.get(empid)
    
    if not trainer:
        return jsonify({"error": "Trainer not found"}), 404

    trainer_data = {
        'empid': trainer.empid,
        'name': trainer.name,
        'email': trainer.email,
        'phone': trainer.phone,
        'subject_id': trainer.subject_id
    }
    
    return jsonify(trainer_data), 200


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

