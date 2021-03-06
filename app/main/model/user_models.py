from .. import db, flask_bcrypt
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
class Patient(db.Model):
    """ Patient Model for storing patient related details """
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password_hash = db.Column(db.String(100))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    diabetes_records = db.relationship("DiabetesRecord")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Patient '{}'>".format(self.username)

class Doctor(db.Model):
    """ Doctor Model to store doctor info """
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password_hash = db.Column(db.String(100))
    patients = db.relationship("Patient")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)

class InsuranceProfessional(db.Model):
    """ Insurance professional object for storing user related details """
    __tablename__ = "insurance_professionals"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)

class DiabetesRecord(db.Model):
    """ Diabetes object to store patient diabetes data """
    __tablename__ = "diabetes_history"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    times_pregnant = db.Column(db.Integer)
    glucose_concentration = db.Column(db.Integer)
    diastolic_blood_pressure = db.Column(db.Integer)
    triceps_skin_fold_thickness = db.Column(db.Integer)
    bmi = db.Column(db.Float)
    diabetes_pedigree_function = db.Column(db.Float)
    age = db.Column(db.Integer)
    prediction = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, nullable=False)

    def get_timestamp(self):
        return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

    def __repr__(self):
        return "<User '{}'>".format(self.username)

class CancerRecord(db.Model):
    """ Cancer object to store patient diabetes data """
    __tablename__ = "cancer_history"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    age = db.Column(db.Integer)
    bmi = db.Column(db.Float)
    glucose = db.Column(db.Float)
    insulin = db.Column(db.Float)
    homa = db.Column(db.Integer)
    leptin = db.Column(db.Float)
    adiponectin = db.Column(db.Integer)
    resistin = db.Column(db.Integer)
    mcp_1 = db.Column(db.Float)
    prediction = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, nullable=False)

    def get_timestamp(self):
        return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

    def __repr__(self):
        return "<User '{}'>".format(self.username)

class HeartDiseaseRecord(db.Model):
    """ Heart disease object to store patient diabetes data """
    __tablename__ = "heart_disease_history"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    chest_pain_type = db.Column(db.Integer)
    resting_blood_pressure = db.Column(db.Integer)
    cholesterol = db.Column(db.Integer)
    fasting_blood_sugar = db.Column(db.Float)
    resting_electrocardiographic = db.Column(db.Float)
    maximum_heart_rate = db.Column(db.Integer)
    exercise_induced_angina = db.Column(db.Integer)
    depression_induced_exercise = db.Column(db.Integer)
    peak_exercise = db.Column(db.Integer)
    number_major_vessels = db.Column(db.Integer)
    thal = db.Column(db.Integer)
    diagnosis_heart_disease = db.Column(db.Integer)
    prediction = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, nullable=False)

    def get_timestamp(self):
        return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

    def __repr__(self):
        return "<User '{}'>".format(self.username)