class Salary:
    def __init__(self, SalaryID, EmployeeID, BasicSalary, Bonus, Allowances):
        self.SalaryID = SalaryID
        self.EmployeeID = EmployeeID
        self.BasicSalary = BasicSalary
        self.Bonus = Bonus
        self.Allowances = Allowances

    def to_dict(self):
        return {
            "SalaryID": self.SalaryID,
            "EmployeeID": self.EmployeeID,
            "BasicSalary": self.BasicSalary,
            "Bonus": self.Bonus,
            "Allowances": self.Allowances
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            SalaryID=data.get("SalaryID"),
            EmployeeID=data.get("EmployeeID"),
            BasicSalary=data.get("BasicSalary"),
            Bonus=data.get("Bonus"),
            Allowances=data.get("Allowances"),
        )
