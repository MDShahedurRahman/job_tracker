from services.job_service import JobService
from views.job_view import JobView


class JobController:
    def __init__(self):
        self.service = JobService()
        self.view = JobView()
