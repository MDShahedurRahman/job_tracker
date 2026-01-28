class JobApplication:
    def __init__(self, job_id, company, title, status, applied_date, interview_date=None):
        self.job_id = job_id
        self.company = company
        self.title = title
        self.status = status
        self.applied_date = applied_date
        self.interview_date = interview_date

    def to_dict(self):
        return {
            "id": self.job_id,
            "company": self.company,
            "title": self.title,
            "status": self.status,
            "applied_date": self.applied_date,
            "interview_date": self.interview_date
        }

    @staticmethod
    def from_dict(data):
        return JobApplication(
            data["id"],
            data["company"],
            data["title"],
            data["status"],
            data["applied_date"],
            data.get("interview_date")
        )
