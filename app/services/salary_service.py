class SalaryService:
    def __init__(self, repo):
        self.repo = repo

    def list_salaries(self):
        return [sal.to_dict() for sal in self.repo.get_all()]
