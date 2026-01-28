from repositories.job_repository import JobRepository
from models.job_application import JobApplication
from utils.date_utils import today, days_until


class JobService:
    def __init__(self):
        self.repo = JobRepository()
        self.jobs = self.repo.load_all()

    def add_job(self, company, title, status):
        job_id = len(self.jobs) + 1
        job = JobApplication(job_id, company, title, status, today())
        self.jobs.append(job)
        self.repo.save_all(self.jobs)

    def update_status(self, job_id, status, interview_date=None):
        for j in self.jobs:
            if j.job_id == job_id:
                j.status = status
                j.interview_date = interview_date
        self.repo.save_all(self.jobs)

    def delete_job(self, job_id):
        self.jobs = [j for j in self.jobs if j.job_id != job_id]
        self.repo.save_all(self.jobs)

    def list_jobs(self):
        return self.jobs

    def filter_by_company(self, company):
        return [j for j in self.jobs if j.company.lower() == company.lower()]
