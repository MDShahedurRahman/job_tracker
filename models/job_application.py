class JobApplication:
    def __init__(self, job_id, company, title, status, applied_date, interview_date=None):
        self.job_id = job_id
        self.company = company
        self.title = title
        self.status = status
        self.applied_date = applied_date
        self.interview_date = interview_date
