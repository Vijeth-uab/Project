from flask import Flask, jsonify, request ,render_template
from flask_cors import CORS
import sqlite3
import re 

app = Flask(__name__)
CORS(app)

Users_db = 'credentials.db'
Coupons_db = 'coupons.db'

conn_users = sqlite3.connect(Users_db)
conn_coupons = sqlite3.connect(Coupons_db)

# API for signup
# @app.route('/api/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method =='POST':
#         fname = request.form['fname']
#         lname = request.form['lname']
#         email = request.form['email']
#         password = request.form['pwd']
#         confirm_password = request.form['cpwd']

#         if password == confirm_password:
#             print("Password matches")
            

#             validation_errors = validate_password(password)
#         #     if not validation_errors:
#         #         print("Password is valid!")
#         #         with conn_users:
#         #             cur = conn_users.cursor()
#         #             cur.execute("SELECT * FROM credentials WHERE email = ?",(email,))
#         #             users = cur.fetchone()
#         #             if users:
#         #                  return render_template('signup.html',userStatus="User Already exists.") 
                        
#         #             else:
#         #                 cur.execute("INSERT INTO credentials(fname,lname,email,password) values (?,?,?,?)", (fname,lname,email,password))
#         #                 return render_template('signupSucc.html')
#         #     else:
#         #         print("Password is invalid. Errors:")
#         #         for error in validation_errors:
#         #             print(error)
#         #         return render_template('signup.html',pwdFailures=validation_errors)
#         # else:
#         #     print('Password did not match')
#         #     return render_template('signup.html',passwordError="Password is not matching")

#     # else:
#     #     return render_template('signup.html')

# Function to validate the password (used in signup API)
def validate_password(password):
    min_length = 8
    has_uppercase = re.compile(r'[A-Z]')
    has_lowercase = re.compile(r'[a-z]')
    has_number = re.compile(r'\d')

    errors = []

    if len(password) < min_length:
        errors.append("Password must be at least 8 characters long.")

    if not has_uppercase.search(password):
        errors.append("Password must contain at least one uppercase letter.")

    if not has_lowercase.search(password):
        errors.append("Password must contain at least one lowercase letter.")

    if not has_number.search(password):
        errors.append("Password must contain at least one number.")

    return errors


# API for login
# @app.route('/api/login', methods=['POST','GET'])
# def login():
    # if request.method =='POST':
    #     email = request.form['email']
    #     password = request.form['pwd']
    #     print('email',email)
    #     print('password',password)
    #     with conn_users:
    #             cur = conn_users.cursor()
    #             cur.execute("SELECT * FROM credentials WHERE email = ? AND password = ?",(email,password))
    #             users = cur.fetchall()
    #             if users:
    #                 cur.close()
    #                 return render_template('loginSucc.html')
    #             else:
    #                 cur.close()
    #                 return render_template('login.html',userStatus="Username or password missmatch")
    # else:
    #     return render_template('login.html')
    

# API for rendering all the coupons
@app.route('/api/getCoupons', methods=['POST','GET'])
def getCoupons():
    if request.method =='GET':
        with conn_coupons:
            cur = conn_coupons.cursor()
            cur.execute("SELECT * FROM coupons")
            coupons = cur.fetchall()
            return coupons    
            

# API for adding coupons to database
@app.route('/api/addCoupons', methods=['POST','GET'])
def addCoupons():
    if request.method =='POST':
        userId = request.form['userId']
        couponName = request.form['couponName']
        couponDescription = request.form['couponDescription']
        couponType = request.form['couponType']
        couponImage = request.form['couponImage']
        couponExpiry = request.form['couponExpiry']

        with conn_coupons:
            cur = conn_coupons.cursor()
            cur.execute("INSERT INTO coupons(userId,couponName,couponDescription,couponType,couponImage,couponExpiry) values (?,?,?,?,?,?)", (userId,couponName,couponDescription,couponType,couponImage,couponExpiry))
            coupons = cur.fetchall()
            return coupons


# API for searching coupons
@app.route('/api/couponSearch', methods=['POST','GET'])
def couponSearch():
    couponType = request.form['couponType']
    couponName = request.form['couponName']

    with conn_coupons:
        cur = conn_coupons.cursor()
        cur.execute("SELECT * FROM coupons WHERE couponType = ? OR couponName = ?",(couponType,couponName))
        searchedCoupons = cur.fetchall()
        return searchedCoupons



# API for deleting coupons
@app.route('/api/couponDelete/<int:cid>', methods=['POST','GET'])
def couponDelete(cid):
    with conn_coupons:
        cur = conn_coupons.cursor()
        cur.execute("DELETE FROM coupons WHERE cid = ?",(cid))
        cur.close()
        return "Coupon deleted"



# @app.route('/api/tasks', methods=['GET', 'POST'])
# def tasks():
#     if request.method == 'GET':
#         conn = sqlite3.connect(Users_db)
#         c = conn.cursor()
#         c.execute('SELECT * FROM tasks')
#         tasks = [{'id': row[0], 'task': row[1]} for row in c.fetchall()]
#         conn.close()
#         return jsonify(tasks)

#     elif request.method == 'POST':
#         data = request.json
#         task = data.get('task')
#         if task:
#             conn = sqlite3.connect(Users_db)
#             c = conn.cursor()
#             c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
#             conn.commit()
#             conn.close()
#             return jsonify({'message': 'Task added successfully'}), 201
#         else:
#             return jsonify({'error': 'Invalid data'}), 400

# @app.route('/api/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
# def task_detail(task_id):
#     if request.method == 'PUT':
#         data = request.json
#         new_task = data.get('task')
#         if new_task:
#             conn = sqlite3.connect(Users_db)
#             c = conn.cursor()
#             c.execute('UPDATE tasks SET task = ? WHERE id = ?', (new_task, task_id))
#             conn.commit()
#             conn.close()
#             return jsonify({'message': 'Task updated successfully'}), 200
#         else:
#             return jsonify({'error': 'Invalid data'}), 400

#     elif request.method == 'DELETE':
#         conn = sqlite3.connect(Users_db)
#         c = conn.cursor()
#         c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
#         conn.commit()
#         conn.close()
#         return jsonify({'message': 'Task deleted successfully'}), 200

if __name__ == '__main__':
    with conn_users:
        c = conn_users.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS credentials (
                        uid INTEGER PRIMARY KEY AUTOINCREMENT,
                        fname VARCHAR(30) NOT NULL,
                        lname VARCHAR(30) NOT NULL,
                        email VARCHAR(50) NOT NULL,
                        password VARCHAR(30) NOT NULL
                    )''')

    with conn_coupons:
        c = conn_coupons.cursor()
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
                            REFERENCES credentials(uid)
                    )''')
    app.run(debug=True)
