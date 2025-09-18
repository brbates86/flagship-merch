from flask import Flask, send_from_directory, request, jsonify
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

app = Flask(__name__)

# Serve static files
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

# Handle form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        company = request.form.get('company', '').strip()
        project_type = request.form.get('project_type', '').strip()
        budget = request.form.get('budget', '').strip()
        timeline = request.form.get('timeline', '').strip()
        quantity = request.form.get('quantity', '').strip()
        message = request.form.get('message', '').strip()
        
        # Validate required fields
        if not name or not email or not project_type or not message:
            return jsonify({'success': False, 'message': 'Please fill in all required fields.'})
        
        # For now, just return success (email functionality can be added later)
        print(f"Form submission from {name} ({email}) - {project_type}")
        print(f"Message: {message}")
        
        return jsonify({'success': True, 'message': 'Thank you! Your message has been received.'})
            
    except Exception as e:
        print(f"Error processing form: {str(e)}")
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'})

if __name__ == '__main__':
    print("Starting Flagship Merch server...")
    print("Website will be available at: http://localhost:8080")
    app.run(debug=True, host='127.0.0.1', port=8080)
