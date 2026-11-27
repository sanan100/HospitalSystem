from models.doctor import Doctor
from models.patient import Patient
from models.hospital import Hospital

def main():
    while True:
        print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Show All Doctors")
        print("4. Show All Patients")
        print("5. Create Appointment")
        print("6. Show All Appointments")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                # Add Doctor
                pass

            elif choice == 2:
                # Add Patient
                pass

            elif choice == 3:
                # Show All Doctors
                pass

            elif choice == 4:
                # Show All Patients
                pass

            elif choice == 5:
                # Create Appointment
                pass

            elif choice == 6:
                # Show All Appointments
                pass

            elif choice == 0:
                print("Exiting Hospital System...")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")

