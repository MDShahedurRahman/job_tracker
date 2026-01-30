class JobView:

    def menu(self):
        print("\n1. Add Job")
        print("2. View All Jobs")
        print("3. Update Status")
        print("4. Delete Job")
        print("5. Filter by Company")
        print("6. Filter by Status")
        print("7. Upcoming Interviews")
        print("8. Analytics Summary")
        print("0. Exit")
        return input("Choose: ")

    def get_job_input(self):
        return (
            input("Company: "),
            input("Title: "),
            input("Status (applied/interview/offer/rejected): ")
        )

    def display_jobs(self, jobs):
        print("\n--- Job Applications ---")
        for j in jobs:
            print(f"{j.job_id}. {j.company} | {j.title} | {j.status} | Applied: {j.applied_date} | Interview: {j.interview_date}")

    def get_update_input(self):
        job_id = int(input("Job ID: "))
        status = input("New Status: ")
        interview = input("Interview Date (YYYY-MM-DD or blank): ")
        return job_id, status, interview or None

    def get_job_id(self):
        return int(input("Job ID: "))

    def get_company(self):
        return input("Company: ")
