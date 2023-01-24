#Harrison Wendt
#30353351
#Created: 11/28/2022
#Last modified: 11/28/2022
#executive.py
from heap import MaxHeap
from patient import Patient
class Executive:
    def __init__(self,file_name):
        self.file_name = file_name
        self.hospital = MaxHeap()
        self.command = []

    
    def file_input(self):
        file_input = open(self.file_name,"r")
        for line in file_input:
            temp = line.strip().split(" ")
            self.command.append(temp)
    
    def run(self):
        for ele in self.command:
            com = ele[0]
            if com == "ARRIVE":
                temp_patient = Patient(ele[1],ele[2],ele[3],ele[4],ele[5])
                self.hospital.add(temp_patient)
            elif com == "NEXT":
                if self.hospital.return_length() >0 :
                    current_patient = self.hospital.return_next()
                    print("Next Patient:")
                    print(current_patient)
                    print()
                else:
                    print("There are no patients")
            elif com == "TREAT":
                try:
                    self.hospital.remove()
                except:
                    print("There are no patients to treat")
            elif com == "COUNT":
                count = self.hospital.return_length()
                if count == 1:
                    print(f'There is {count} patient waiting')
                    print()
                else:

                    print(f'There are {count} patients waiting')
                    print()

