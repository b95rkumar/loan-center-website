from flask import Flask, render_template, request, render_template_string
from regex import escape
import smtplib
from email.mime.text import MIMEText

app = Flask (__name__)

@app.route('/')
def hello_loan ():
  return render_template ('home.html')
"""
@app.route('/')
def form():
    return '''
        <form action="/submit" method="post">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" required><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br>
            <label for="message">Message:</label><br>
            <textarea id="message" name="message" required></textarea><br>
            <input type="submit" value="Submit">
        </form>
    '''
"""
@app.route('/contact')
def hello_contact ():
  return render_template ('contact-form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Do something with the form data, such as saving it to a database
    # Sanitize inputs to prevent XSS
    safe_name = escape(name)
    safe_email = email
    safe_message = escape(message)
    subject = "Attention - New enquirty came!!!"
    sender = "loancenteras@gmail.com"
    receiver = "b95rkumar@gmail.com"
    final_message = safe_name +" \n with email id " + safe_email+ " \n has sent message \n" + safe_message
    msg = MIMEText(final_message)
#    msg = safe_message
    msg['Subject'] = subject
#    msg['From'] = sender
    
#    message = f"""
#    Subject: New enquiry from custoemr
#    From: {safe_email}
#    {safe_message}
#    """
    try:
#        with smtplib.SMTP("sandbox.smtp.mailtrap.io", 587) as server:
#            server.starttls()
#            server.login("f2959531319015", "9a0af9a27333b7")
#            server.sendmail(sender, receiver, safe_message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, "change here xxxx")
            smtp_server.sendmail(sender, receiver, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    # Continue processing or storing data
    return render_template_string('''
        <h1>Thank You!</h1>
        <h2>Mail sent successfully with below information!</h2>
        <p>Your name: {{ name }}</p>
        <p>Your email: {{ email }}</p>
        <p>Your message: {{ message }}</p>
    ''', name=safe_name, email=safe_email, message=safe_message)



if __name__ == '__main__':  
  app.run(host='0.0.0.0', debug=True)
  