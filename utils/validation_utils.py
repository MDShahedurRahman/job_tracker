def validate_status(status):
    valid = ["applied", "interview", "offer", "rejected"]
    return status.lower() in valid
