class Employee:
    def __init__(self, EmployeeID, FirstName, LastName, Gender, DateOfBirth):
        self.EmployeeID = EmployeeID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Gender = Gender
        self.DateOfBirth = DateOfBirth

    def to_dict(self):
        return {
            "EmployeeID": self.EmployeeID,
            "FirstName": self.FirstName,
            "LastName": self.LastName,
            "Gender": self.Gender,
            "DateOfBirth": self.DateOfBirth
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            EmployeeID=data.get("EmployeeID"),
            FirstName=data.get("FirstName"),
            LastName=data.get("LastName"),
            Gender=data.get("Gender"),
            DateOfBirth=data.get("DateOfBirth"),
        )
