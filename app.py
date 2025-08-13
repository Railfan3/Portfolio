from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

# Mock database for contact form submissions
contacts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if name and email and message:
            contacts.append({
                'name': name,
                'email': email,
                'message': message,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            flash('Thank you! Your message has been sent successfully.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in all fields.', 'error')
    
    return render_template('contact.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True)