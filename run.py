from tours import app

with app.app_context():
    from tours import db
    db.create_all() 

# with app.app_context():
#     from tours.models import Admin
#     from tours import db
#     existing_admin = Admin.query.filter_by(email='admin@gmail.com').first()
#     if existing_admin is None:
#         new_admin = Admin(username='admin1', email='admin@gmail.com', password='admin123')
#         db.session.add(new_admin)
#         db.session.commit()
#     else:
#         print("Email already exists in the admin table. Please choose a different email.")


if __name__ == '__main__':
    app.run(debug=True)
