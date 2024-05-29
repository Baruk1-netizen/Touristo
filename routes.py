from functools import wraps
from flask import render_template, redirect, request, session
from tours.models import User, Accommodation, Package, Contact, Admin
from tours import app, db
from datetime import datetime


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        passsword = User.query.filter_by(password=password).first()

        if user and passsword:
            session['logged_in'] = True
            return redirect('/main')
            # return {'status': 'success', 'message': 'Logged in successfully'}

        else:
            return render_template('login.html', error='Invalid email or password')
            # return {'status': 'fail', 'message': 'Invalid email or password'}
    return render_template('login.html')


@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        # print(username, email, password, confirmPassword)

        if password != confirmPassword:
            return render_template('signUp.html', error='Passwords do not match')
            # return {'status': 'fail', 'message': 'Passwords do not match'}

        existing_user = User.query.filter_by(email=email).first()
        # print(existing_user)

        if existing_user:
            return render_template('signUp.html', error='Email already exists. Please choose a different email.')
            # return {'status': 'fail', 'message': 'Email already exists. Please choose a different email'}

        # hashed_password = generate_password_hash(password)

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return render_template('login.html', message='Account created successfully')
        # return redirect('/')
        # return {'status': 'success', 'message': 'Registered successfully'}

    else:
        return render_template('signUp.html')


@app.route('/main')
@login_required
def index():
    return render_template('html/index.html')


@app.route('/animals')
@login_required
def animals():
    return render_template('/html/discover/animals.html')


@app.route('/citymalls')
@login_required
def citymalls():
    return render_template('/html/discover/citymalls.html')


@app.route('/hotels')
@login_required
def hotels():
    return render_template('/html/discover/hotels.html')


@app.route('/interactive map')
@login_required
def map():
    return render_template('/html/discover/map.html')


@app.route('/accommodation', methods=['GET', 'POST'])
@login_required
def accommodation():
    if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            checkinDate_str = request.form.get('checkinDate')
            checkoutDate_str = request.form.get('checkoutDate')
            guests = request.form.get('guests')
            room = request.form.get('room')
            hotel = request.form.get('hotel')

            # Convert date strings to datetime objects
            checkinDate = datetime.strptime(checkinDate_str, '%Y-%m-%d')
            checkoutDate = datetime.strptime(checkoutDate_str, '%Y-%m-%d')

            accommodation = Accommodation(name=name, email=email, checkinDate=checkinDate, checkoutDate=checkoutDate, guests=guests, room=room, hotel=hotel)
            db.session.add(accommodation)
            db.session.commit()
            return render_template('/html/services/accommodation.html', message='Accommodation booked successfully', hotel=hotel)
    return render_template('/html/services/accommodation.html')


@app.route('/packages', methods=['GET', 'POST'])
@login_required
def packages():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        checkinDate_str = request.form.get('checkin')
        checkoutDate_str = request.form.get('checkout')
        guests = request.form.get('guests')
        pkgType = request.form.get('room')

        # Convert date strings to datetime objects
        checkinDate = datetime.strptime(checkinDate_str, '%Y-%m-%d')
        checkoutDate = datetime.strptime(checkoutDate_str, '%Y-%m-%d')

        package = Package(name=name, email=email, checkinDate=checkinDate, checkoutDate=checkoutDate, guests=guests, pkgType=pkgType)
        db.session.add(package)
        db.session.commit()
        return render_template('/html/services/packages.html', message='Package booked successfully')
    return render_template('/html/services/packages.html')


@app.route('/transportation')
@login_required
def transportation():
    return render_template('/html/services/transportation.html')


@app.route('/about')
@login_required
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
@login_required
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        contact = Contact(name=name, email=email, message=message)
        db.session.add(contact)
        db.session.commit()
        return render_template('contact.html', message='Message sent successfully')
    return render_template('contact.html')

@app.route('/admin', methods=['GET', 'POST'])
def adminLogin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        admin = Admin.query.filter_by(email=email).first()
        passsword = Admin.query.filter_by(password=password).first()

        if admin == email and passsword == password:
            session['logged_in'] = True
            return redirect('/admin/page')
            # return {'status': 'success', 'message': 'Logged in successfully'}

        else:
            return render_template('adminLogin.html', error='Invalid email or password')
            # return {'status': 'fail', 'message': 'Invalid email or password'}
    return render_template('adminLogin.html')

@app.route('/admin/page', methods=['GET', 'POST'])
def admin():
    context = {}
    users = User.query.all()
    packages = Package.query.all()
    accommodations = Accommodation.query.all()
    contacts = Contact.query.all()
    
    # Create a list of dictionaries containing package information
    package_list = []
    for pkg in packages:
        package_info = {
            'name': pkg.name,
            'email': pkg.email,
            'checkinDate': pkg.checkinDate,
            'checkoutDate': pkg.checkoutDate,
            'guests': pkg.guests,
            'pkgType': pkg.pkgType
        }
        package_list.append(package_info)
        
    # Create a list of dictionaries containing accommodation information
    accommodation_list = []
    for acc in accommodations:
        accommodation_info = {
            'name': acc.name,
            'email': acc.email,
            'checkinDate': acc.checkinDate,
            'checkoutDate': acc.checkoutDate,
            'guests': acc.guests,
            'room': acc.room,
            'hotel': acc.hotel
        }
        accommodation_list.append(accommodation_info)
        
    # Create a list of dictionaries containing contact information
    contact_list = []
    for cont in contacts:
        contact_info = {
            'name': cont.name,
            'email': cont.email,
            'message': cont.message,
        }
        contact_list.append(contact_info)
    
    # Create a dictionary of user information
    users_dict = {user.username: user.email for user in users}
    
    # Add both user, package, accommodation, and contact information to the context
    context['users'] = users_dict
    context['packages'] = package_list
    context['accommodations'] = accommodation_list
    context['contacts'] = contact_list
    
    return render_template('admin.html', **context)

@app.route('/admin/search', methods=['POST'])
def search():
    if request.method == 'POST':
        username = request.form.get('username')
        
        user = User.query.filter_by(username=username).first()
        search = {}
        if user:
            search = {
                'username': user.username,
                'email': user.email
            }
        print(search)
        return render_template('admin.html', search=search)
    # return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)
