from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("registration/login.html", boolean=False)

@auth.route('/logout')
def logout():
    return render_template("registration/logout.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if password1 != password2:
            flash('Password not Matching', category='error')
        elif len(password1) < 8:
            flash('Password must be greater than 8 charecters', category='error')
        else:
            flash('Account Created', category='success')
    return render_template("registration/signup.html")