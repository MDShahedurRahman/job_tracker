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
