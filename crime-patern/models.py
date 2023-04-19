from flask import Flask
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from app import app
from flask_migrate import Migrate
import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crime'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

date = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

class Location(db.Model):
     __tablename__ = "locations"
     id = db.Column(db.Integer, primary_key=True, autoincrement= True)
     name = db.Column(db.String(255), nullable = False) 
     
     date_created = db.Column(db.DateTime(), default=date)
     status = db.Column(db.Boolean, default=True)
     
    #  user = db.relationship('users', backref=backref('locations'))
    #  crime = db.relationship('crime', backref=backref('locations'))
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    fullname = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), nullable = False, unique=True)
    phoneNumber = db.Column(db.String(20),nullable =False )
    password = db.Column(db.String(30), nullable = False)
    is_admin = db.Column(db.Boolean, default=False)
    is_staff = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    # crime = db.relationship('crime', backref=backref('users'))
    date_created = db.Column(db.DateTime(), default=date)
    date_updated = db.Column(db.DateTime(), default=date)
    
    
        
    def __repr__(self):
        return f"<{self.id}>"

    # @classmethod
    # def find_by_email(cls, email):
    #     return cls.query.filter_by(email=email).first()

    # @classmethod
    # def find_all(cls):
    #     return cls.query.all()

    # @classmethod
    # def find_by_id(cls, id):
    #     return cls.query.filter_by(id=id).first()
    
    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()
    
    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()

#workout class model

class CrimeType(db.Model):
    __tablename__ = "crimeTypes"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(255), nullable = False) 
    date_created = db.Column(db.DateTime(), default=date)
    date_updated = db.Column(db.DateTime(), default=date)
    status = db.Column(db.Boolean, default=False)
    # crime = db.relationship('crime', backref=backref('crimeTypes'))
    
    
class Crime(db.Model):
    __tablename__ = "crime"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    crimeType_id = db.Column(db.Integer, db.ForeignKey('crimeTypes.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    description = db.Column(db.String(255), nullable = False)
    date_occured =  db.Column(db.DateTime(), default=date)
    #post = db.relationship('posts', backref=backref('users'))
    date_created = db.Column(db.DateTime(), default=date)
    date_updated = db.Column(db.DateTime(), default=date)
    status = db.Column(db.Boolean, default=True)
    
with app.app_context():
    db.create_all()

# if __name__ == '__main__':
#     app.run()