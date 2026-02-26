class DepartmentService:
    def __init__(self, repo):
        self.repo = repo

    def list_departments(self):
        return [dept.to_dict() for dept in self.repo.get_all()]
