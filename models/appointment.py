from datetime import datetime
class Appointment():
    def __init__(self, appointmentID, doctor, patient, date):
        self.appointmentID = appointmentID
        self.doctor = doctor
        self.patient = patient
        self.date = date if date is not None else datetime.now()

    def showInfo(self):
        print(f"AppointmentID: {self.appointmentID}\nDoctor: {self.doctor}\nPatient: {self.patient}\nDate: {self.date}")
