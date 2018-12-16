from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    v_password = request.form['v_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    v_password_error = ''
    email_error = ''

    at_counter = 0
    dot_counter = 0

    if username != '':
        for char in username:
            if ' ' in char:
                username_error = "You can not have space in your 'Username'."
        if len(username) < 3 or len(username) > 20:
            username_error = "Username should have 3 to 20 charactors."
    else:
        username_error = "You can not leave 'Username' as a blank."

    if password != '':
        for char in password:
            if ' ' in char:
                password_error = "You can not have space in your 'Password'."
        if len(password) < 3 or len(password) > 20:
            password_error = "Password should have 3 to 20 charactors."
    else:
        password_error = "You can not leave 'Password' as a blank."

    if v_password != '':
        if v_password != password:
            v_password_error = "Your passwords do not match."
    else:
        v_password_error = "You can not leave 'Verify Password' as a blank."

    if email != '':
        for char in email:
            if char == "@":
                at_counter += 1
            if char == ".":
                dot_counter += 1
        if at_counter == 0 or dot_counter == 0:
            email_error = "Please provide correct email."
        if at_counter > 1 or dot_counter > 1 or " " in email:
            email_error = "Please provide correct email."
        if len(email) < 3 or len(email) > 20:
            email_error = "'Email' must have 3-20 characters"

    if not username_error and not password_error and not v_password_error and not email_error:
        return redirect("/welcome?username={0}".format(username))

    return render_template ("signup.html", username_value = username, email_value = email, username_error = username_error, 
    password_error = password_error, v_password_error = v_password_error, email_error = email_error)

@app.route("/welcome", methods=['GET'])
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", username = username)

app.run()