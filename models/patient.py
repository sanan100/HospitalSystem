from models.person import Person

class Patient(Person):
    def __init__(self, name, surname, age, phone, patientID, bloodGroup):
        super().__init__(name, surname, age, phone)
        self.patientID = patientID # public
        self._bloodGroup = bloodGroup # protected 
        self.__medicalHistory = [] # private

    def showInfo(self):
        super().showInfo()
        print(f"patientID: {self.patientID}\nBloodGroup: {self._bloodGroup}\nmedicalHistory: {self.__medicalHistory}")

    def getMedicalHistory(self):
        print(self.__medicalHistory)

    def updateMedicalHistory(self,medicine):
        if type(medicine) == list:
            self.__medicalHistory += medicine
            print("succesfly added")
        else:
            print("please data write in list")
        
