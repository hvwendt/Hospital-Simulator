#Harrison Wendt
#30353351
#Created: 11/28/2022
#Last modified: 11/28/2022
#patient.py
class Patient:
    def __init__(self,f_name,l_name,age,illness,severity):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.illness = illness
        self.severity = severity

    
    def __str__(self):
       
        return f'\tName: {self.l_name}, {self.f_name}\n\t Age: {self.age}\n\t Suffers from: {self.illness}\n\t Illness severity: {self.severity}'

    def __eq__(self, other):
        return self.severity == other


    def __lt__(self, other):
        return self.severity < other
    
    
    def __gt__(self, other):
        return self.severity > other
