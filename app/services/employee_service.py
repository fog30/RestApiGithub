class EmployeeService:
    def __init__(self, repo):
        self.repo = repo

    def list_employees(self):
        return [emp.to_dict() for emp in self.repo.get_all()]

    def get_employee(self, employee_id):
        emp = self.repo.get_by_id(employee_id)
        return emp.to_dict() if emp else None

    def create_employee(self, data):
        employee = self.repo.create(data)
        return employee.to_dict()

    def update_employee(self, employee_id, data):
        emp = self.repo.update(employee_id, data)
        return emp.to_dict() if emp else None

    def delete_employee(self, employee_id):
        return self.repo.delete(employee_id)
