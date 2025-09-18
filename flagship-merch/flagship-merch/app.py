from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json

app = Flask(__name__, static_folder='.')

# Configuration - You'll need to set these environment variables
SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS', 'your-email@gmail.com')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', 'your-app-password')
OWNER_EMAIL = os.environ.get('OWNER_EMAIL', 'owner@flagshipmerch.com')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/about.html')
def about():
    return send_from_directory('.', 'about.html')

@app.route('/contact.html')
def contact():
    return send_from_directory('.', 'contact.html')

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

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
        
        # Create email content
        email_content = f"""
        New Contact Form Submission - Flagship Merch
        
        Contact Information:
        Name: {name}
        Email: {email}
        Phone: {phone if phone else 'Not provided'}
        Company: {company if company else 'Not provided'}
        
        Project Details:
        Project Type: {project_type}
        Budget: {budget if budget else 'Not specified'}
        Timeline: {timeline if timeline else 'Not specified'}
        Quantity: {quantity if quantity else 'Not specified'}
        
        Message:
        {message}
        
        Submitted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        # Send email
        success = send_email(
            to_email=OWNER_EMAIL,
            subject=f"New Contact Form Submission from {name}",
            body=email_content,
            reply_to=email
        )
        
        if success:
            return jsonify({'success': True, 'message': 'Message sent successfully!'})
        else:
            return jsonify({'success': False, 'message': 'Failed to send message. Please try again.'})
            
    except Exception as e:
        print(f"Error processing form: {str(e)}")
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'})

def send_email(to_email, subject, body, reply_to=None):
    """
    Send an email using SMTP
    """
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        if reply_to:
            msg['Reply-To'] = reply_to
        
        # Add body to email
        msg.attach(MIMEText(body, 'plain'))
        
        # Create SMTP session
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Enable TLS encryption
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Send email
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, to_email, text)
        server.quit()
        
        print(f"Email sent successfully to {to_email}")
        return True
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False

@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('home'))

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'success': False, 'message': 'Internal server error. Please try again later.'}), 500

if __name__ == '__main__':
    # Check if email configuration is set
    if EMAIL_ADDRESS == 'your-email@gmail.com' or EMAIL_PASSWORD == 'your-app-password':
        print("⚠️  WARNING: Email configuration not set!")
        print("Please set the following environment variables:")
        print("- EMAIL_ADDRESS: Your email address")
        print("- EMAIL_PASSWORD: Your email app password")
        print("- OWNER_EMAIL: The email address to receive form submissions")
        print("\nFor Gmail users:")
        print("1. Enable 2-factor authentication")
        print("2. Generate an app password")
        print("3. Use the app password as EMAIL_PASSWORD")
        print("\nExample:")
        print("export EMAIL_ADDRESS='your-email@gmail.com'")
        print("export EMAIL_PASSWORD='your-16-char-app-password'")
        print("export OWNER_EMAIL='owner@flagshipmerch.com'")
        print("\nStarting server anyway...")
    
    app.run(debug=True, host='127.0.0.1', port=8080)
