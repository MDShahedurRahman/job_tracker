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

            elif choice == "2":
                self.view.display_jobs(self.service.list_jobs())

            elif choice == "3":
                job_id, status, interview = self.view.get_update_input()
                self.service.update_status(job_id, status, interview)

            elif choice == "4":
                job_id = self.view.get_job_id()
                self.service.delete_job(job_id)

            elif choice == "5":
                company = self.view.get_company()
                self.view.display_jobs(self.service.filter_by_company(company))

            elif choice == "6":
                status = self.view.get_status()
                self.view.display_jobs(self.service.filter_by_status(status))
