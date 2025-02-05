from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import pyodbc
import os

app = Flask(__name__)

# Database Configuration for Microsoft SQL Server (Windows Authentication)
DB_SERVER = "localhost"  # Change if using a remote server
DB_NAME = "contact"      # Your database name
DB_DRIVER = "ODBC Driver 17 for SQL Server"

# Connection String (Windows Authentication)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc://{DB_SERVER}/{DB_NAME}?trusted_connection=yes&driver={DB_DRIVER}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# Contact Model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)

# Create database tables if not exists
with app.app_context():
    db.create_all()

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Get All Contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'phone': c.phone, 'email': c.email} for c in contacts])

# Add a New Contact
@app.route('/contacts', methods=['POST'])
def add_contact():
    try:
        data = request.json
        if not all(k in data for k in ['name', 'phone', 'email']):
            return jsonify({'error': 'Missing data'}), 400
        
        new_contact = Contact(name=data['name'], phone=data['phone'], email=data['email'])
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({'message': 'Contact added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Update an Existing Contact
@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if not contact:
        return jsonify({'error': 'Contact not found'}), 404

    data = request.json
    contact.name = data.get('name', contact.name)
    contact.phone = data.get('phone', contact.phone)
    contact.email = data.get('email', contact.email)
    
    db.session.commit()
    return jsonify({'message': 'Contact updated successfully'})

# Delete a Contact
@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if not contact:
        return jsonify({'error': 'Contact not found'}), 404

    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': 'Contact deleted successfully'})

# Search Contacts (by name, phone, or email)
@app.route('/contacts/search', methods=['GET'])
def search_contact():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'Missing search query'}), 400
    
    results = Contact.query.filter(
        (Contact.name.ilike(f'%{query}%')) | 
        (Contact.phone.ilike(f'%{query}%')) |
        (Contact.email.ilike(f'%{query}%'))
    ).all()
    
    return jsonify([{'id': c.id, 'name': c.name, 'phone': c.phone, 'email': c.email} for c in results])

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)

