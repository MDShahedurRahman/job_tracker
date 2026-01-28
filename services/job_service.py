from repositories.job_repository import JobRepository
from models.job_application import JobApplication
from utils.date_utils import today, days_until


class JobService:
    def __init__(self):
        self.repo = JobRepository()
        self.jobs = self.repo.load_all()
