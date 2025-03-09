class student:
    def __init__(self,Name,Class,marks,Dob,BloodGroup,Password):
        self.Name = Name
        self.marks = marks
        self.Dob = Dob
        self.BloodGroup = BloodGroup
        self.Class = Class
        self.__Password = Password

    def __getpass(self):
        print(self.__Password)

Daksh = student("Daksh Singh",7,"2143256")

print(Daksh.Name)
Daksh.getpass()



