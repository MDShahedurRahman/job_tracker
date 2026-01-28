from services.job_service import JobService
from views.job_view import JobView


class JobController:
    def __init__(self):
        self.service = JobService()
        self.view = JobView()

    def run(self):
        while True:
            choice = self.view.menu()

            if choice == "1":
                company, title, status = self.view.get_job_input()
                self.service.add_job(company, title, status)
