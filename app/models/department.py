class Department:
    def __init__(self, DepartmentID, DepartmentName, Location):
        self.DepartmentID = DepartmentID
        self.DepartmentName = DepartmentName
        self.Location = Location

    def to_dict(self):
        return {
            "DepartmentID": self.DepartmentID,
            "DepartmentName": self.DepartmentName,
            "Location": self.Location
        }
