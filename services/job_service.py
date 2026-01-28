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
