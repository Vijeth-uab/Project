from flask import Flask, jsonify, request, session
from flask_session import Session
from flask import session

from flask_cors import CORS
import sqlite3
import secrets
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SECRET_KEY'] = secrets.token_hex(16)  # Replace with a strong secret key
app.config['SESSION_TYPE'] = 'filesystem' 
Session(app)

DATABASE = 'todo.db'
Coupons_db = 'coupons.db'
conn_coupons = sqlite3.connect(Coupons_db)

app.secret_key = secrets.token_hex(16)

def create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    phonenumber TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS coupons (
                    cid INTEGER PRIMARY KEY AUTOINCREMENT,
                    couponName VARCHAR(30) NOT NULL,
                    couponDescription VARCHAR(200) NOT NULL,
                    couponImage VARCHAR(200) NOT NULL,
                    couponType VARCHAR(30) NOT NULL,
                    couponExpiry DATE NOT NULL,
                    uid INTEGER,
                    CONSTRAINT fk_credentials
                    FOREIGN KEY (uid)
                    REFERENCES users(id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS tradedcoupons (
                    transactionID INTEGER PRIMARY KEY AUTOINCREMENT,
                    couponID INTEGER,
                    userID INTEGER,
                    FOREIGN KEY (couponID) REFERENCES coupons (cid),
                    FOREIGN KEY (userID) REFERENCES users (id)
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    user_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )''')
    conn.commit()
    conn.close()


@app.route('/api/debugSession')
def debug_session():
    return jsonify(session)


@app.route('/api/addCoupons', methods=['POST'])
def add_coupons():
    # Retrieve the 'user_id' from the session
    print('g',session)
    # user_id = session.get('user_id')
    # if not user_id:
    #     return jsonify({'error': 'User not logged in'}), 401
 
    data = request.json
    coupon_data = {
        'userId': 2,
        'couponName': data.get('couponName'),
        'couponDescription': data.get('couponDescription'),
        'couponType': data.get('couponType'),
        'couponImage': data.get('couponImage'),
        'couponExpiry': data.get('couponExpiry'),
    }

    with conn_coupons:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO coupons (uid, couponName, couponDescription, couponType, couponImage, couponExpiry) VALUES (?, ?, ?, ?, ?, ?)", (coupon_data['userId'], coupon_data['couponName'], coupon_data['couponDescription'], coupon_data['couponType'], coupon_data['couponImage'], coupon_data['couponExpiry']))
        conn.commit()
        return jsonify({'message': 'Coupon added successfully'}), 201

@app.route('/api/getCoupons', methods=['GET'])
def get_coupons():
    try:
        # Fetch all coupons from the 'coupons' table using raw SQL query
        query = """
            SELECT * FROM coupons
        """
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        result = c.execute(query).fetchall()

        # Serialize the coupons to a list of dictionaries
        serialized_coupons = []
        for row in result:
            serialized_coupon = {
                'cid': row[0],
                'couponName': row[1],
                'couponDescription': row[2],
                'couponImage': row[3],
                'couponType': row[4],
                'couponExpiry': row[5],
                # 'couponExpiry': row[5].strftime('%Y-%m-%d')
            }
            serialized_coupons.append(serialized_coupon)

        return jsonify(serialized_coupons), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/getMyCoupons/<int:uid>', methods=['GET'])
def get_my_coupons(uid):
    try:
        # Fetch all coupons from the 'coupons' table using raw SQL query
        query = """
            SELECT c.cid AS couponID, c.couponName, c.couponDescription, c.couponType,
            c.couponImage, c.couponExpiry, u.id AS userID, u.firstname, u.lastname, u.phonenumber, u.email
            FROM coupons AS c
            JOIN users AS u ON c.uid = u.id
            WHERE c.uid = ?
        """, (uid,).fetchall()
      
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        result = c.execute(query).fetchall()

        # Serialize the coupons to a list of dictionaries
        serialized_coupons = []
        for row in result:
            serialized_coupon = {
                'couponID': row[0],
                'couponName': row[1],
                'couponDescription': row[2],
                'couponType': row[3],
                'couponImage': row[4],
                'couponExpiry': row[5].strftime('%Y-%m-%d'),
                'userID': row[6],
                'firstname': row[7],
                'lastname': row[8],
                'phonenumber': row[9],
                'email': row[10],
            }
            serialized_coupons.append(serialized_coupon)

        return jsonify(serialized_coupons), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/getCouponsById/<int:coupon_id>', methods=['GET'])
def get_coupon_by_id(coupon_id):
    try:
        # Fetch a specific coupon from the 'coupons' table by its coupon ID
        query = """
            SELECT * FROM coupons WHERE cid = ?
        """
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        result = c.execute(query, (coupon_id,)).fetchone()

        if result:
            # Serialize the coupon data to a dictionary
            serialized_coupon = {
                'cid': result[0],
                'couponName': result[1],
                'couponDescription': result[2],
                'couponType': result[3],
                'couponImage': result[4],
                'couponExpiry': result[5].strftime('%Y-%m-%d')
            }
            return jsonify(serialized_coupon), 200
        else:
            return jsonify({'error': 'Coupon not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/deleteCoupon/<int:coupon_id>', methods=['DELETE'])
def delete_coupon(coupon_id):
    try:
        # Check if the user is logged in
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'User not logged in'}), 401

        # Check if the coupon exists and belongs to the logged-in user
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT uid FROM coupons WHERE cid = ?', (coupon_id,))
        coupon_owner = c.fetchone()

        if not coupon_owner:
            conn.close()
            return jsonify({'error': 'Coupon not found'}), 404

        if coupon_owner[0] != user_id:
            conn.close()
            return jsonify({'error': 'Unauthorized to delete this coupon'}), 403

        # Delete the coupon from the 'coupons' table
        c.execute('DELETE FROM coupons WHERE cid = ?', (coupon_id,))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Coupon deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    phonenumber = data.get('phonenumber')
    email = data.get('email')
    password = data.get('password')
    confirmpassword = data.get('confirmpassword')

    print(firstname,lastname,phonenumber,email,password,confirmpassword)
    # Basic validation for required fields
    if not firstname or not lastname or not phonenumber or not email or not password or not confirmpassword:
        return jsonify({'error': 'All fields are required'}), 400

    # Check if the password and confirm password match
    if password != confirmpassword:
        return jsonify({'error': 'Passwords do not match'}), 400

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Check if the user already exists
    c.execute('SELECT id FROM users WHERE email = ?', (email,))
    user = c.fetchone()
    if user:
        conn.close()
        return jsonify({'error': 'User with this email already exists'}), 400

    # Create the user
    c.execute('INSERT INTO users (firstname, lastname, phonenumber, email, password) VALUES (?, ?, ?, ?, ?)', (firstname, lastname, phonenumber, email, password))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Check if the user exists and the password is correct
    c.execute('SELECT id FROM users WHERE email = ? AND password = ?', (email, password))
    user = c.fetchone()
    conn.close()

    if not user:
        return jsonify({'error': 'Invalid email or password'}), 401

    # Store the 'user_id' in the session
    session['user_id'] = user[0]

    return jsonify({'message': 'Login successful', 'user_id': user[0]}), 200


@app.route('/api/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        user_id = request.args.get('user_id')  # Get user_id from query parameter
        if not user_id:
            return jsonify({'error': 'User ID is required as a query parameter'}), 400

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        c.execute('SELECT * FROM tasks WHERE user_id = ?', (user_id,))
        tasks = [{'id': row[0], 'task': row[1]} for row in c.fetchall()]
        conn.close()
        return jsonify(tasks)

    elif request.method == 'POST':
        data = request.json
        task = data.get('task')
        user_id = data.get('user_id')

        if not task or not user_id:
            return jsonify({'error': 'Invalid data'}), 400

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('INSERT INTO tasks (task, user_id) VALUES (?, ?)', (task, user_id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Task added successfully'}), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
def task_detail(task_id):
    if request.method == 'PUT':
        data = request.json
        new_task = data.get('task')
        if new_task:
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            c.execute('UPDATE tasks SET task = ? WHERE id = ?', (new_task, task_id))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Task updated successfully'}), 200
        else:
            return jsonify({'error': 'Invalid data'}), 400

    elif request.method == 'DELETE':
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Task deleted successfully'}), 200

@app.route('/api/getTradedCoupons/<int:userID>', methods=['GET'])
def get_traded_coupons(userID):
    try:
        # Fetch all coupons from the 'coupons' table using raw SQL query
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        result = c.execute("""
            SELECT tc.transactionID, c.cid AS couponID, c.couponName, c.couponDescription, c.couponType,
            c.couponImage, c.couponExpiry, u.id AS userID, u.firstname, u.lastname, u.phonenumber, u.email
            FROM tradedcoupons AS tc
            JOIN coupons AS c ON tc.couponID = c.cid
            JOIN users AS u ON tc.userID = u.id
            WHERE tc.userID = ?
        """, (userID,)).fetchall()


        # Serialize the coupons to a list of dictionaries
        serialized_coupons = []
        for row in result:
            serialized_coupon = {
                'transactionID': row[0],
                'couponID': row[1],
                'couponName': row[2],
                'couponDescription': row[3],
                'couponType': row[4],
                'couponImage': row[5],
                'couponExpiry': row[6].strftime('%Y-%m-%d'),
                'userID': row[7],
                'firstname': row[8],
                'lastname': row[9],
                'phonenumber': row[10],
                'email': row[11],
            }
            serialized_coupons.append(serialized_coupon)

        return jsonify(serialized_coupons), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# @app.route('/api/sendEmail', methods=['POST'])
# def send_email():
#     data = request.json
#     recipient_email = data.get('email')
#     sender_email = 'bheemprashanthreddy4@gmail.com'  # Replace with the recipient email address

#     msg = EmailMessage()
#     msg.set_content(data.get('message'))
#     msg['Subject'] = 'Contact Form Submission'
#     msg['From'] = sender_email
#     msg['To'] = recipient_email
#     SMTP_HOST = 'smtp.gmail.com'
#     SMTP_PORT = 587  
#     SMTP_USERNAME = 'bheemprashanthreddy4@gmail.com' #keep the sender gmail address
#     SMTP_PASSWORD = 'Prashanth@48' #keep the sender gmail password
#     try:
#         with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
#             server.starttls()
#             server.login(SMTP_USERNAME, SMTP_PASSWORD)
#             server.send_message(msg)
#         return jsonify({'message': 'Email sent successfully'}), 200
#     except Exception as e:
#         print(e)
#         return jsonify({'error': 'Failed to send email'}), 500
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587  # Replace with the appropriate SMTP port for your server
SMTP_USERNAME = 'avinashthatavarthi123@gmail.com'
SMTP_PASSWORD = 'ARROgance800@#$'


@app.route('/api/sendEmail', methods=['POST'])
def send_email():
    # Parse data from the request (assuming it's a JSON request)
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = SMTP_USERNAME
    msg['To'] = email
    msg['Subject'] = 'Contact Form Submission'

    body = f"Hello {name},\n\nThank you for contacting us. Your message has been received:\n\n{message}"
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, email, msg.as_string())
        server.quit()

        response_data = {
            'success': True,
            'message': 'Email sent successfully'
        }

    except Exception as e:
        response_data = {
            'success': False,
            'message': f'Error sending email: {str(e)}'
        }

    # Set the CORS headers in the response
    response = jsonify(response_data)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
