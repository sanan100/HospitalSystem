from models.appointment import Appointment
from models.doctor import Doctor
from models.patient import Patient
class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.appointments = []

    def addDoctor(self, doctor):
        self.doctor = doctor
        self.doctors.append(doctor)
        print("succefly added")
    def addPatient(self, patient):
        self.patient = patient
        self.patients.append(patient)
        print("succefly added")

    def showDoctors(self):
        for i in self.doctors:
            print(i)

    def showPatients(self):
        for i in self.patients:
            print(i)

    def createAppointment(self, doctorID, patientID, date):
        appointment = Appointment(doctorID, patientID, date)
        self.appointments.append(appointment)
        print("succefly created appointment")
    def showAppointments(self):
        for i in self.appointments:
         print(i)
