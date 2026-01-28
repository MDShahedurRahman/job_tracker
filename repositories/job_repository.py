import json
import os
from models.job_application import JobApplication


class JobRepository:
    FILE = "data/jobs.json"

    def load_all(self):
        if not os.path.exists(self.FILE):
            return []
        with open(self.FILE, "r") as f:
            data = json.load(f)
            return [JobApplication.from_dict(x) for x in data]

    def save_all(self, jobs):
        os.makedirs("data", exist_ok=True)
        with open(self.FILE, "w") as f:
            json.dump([j.to_dict() for j in jobs], f, indent=4)
