import os

class CameraResourceManager:
    def __init__(self, max_capacity=10):
        self.max_capacity = max_capacity
        self.used_capacity = 0

    def allocate_existing(self, hours):
        self.used_capacity = hours

    def allocation_decision(self, requested_hours, priority_level):
        remaining = self.max_capacity - self.used_capacity

        if requested_hours <= remaining:
            return "APPROVED"
        elif priority_level == "HIGH" and requested_hours <= self.max_capacity:
            return "CONDITIONALLY APPROVED"
        else:
            return "REJECTED"


# ---- Jenkins Execution Entry Point ----
if __name__ == "__main__":

    req_hours_env = os.getenv("REQ_HOURS")
    used_hours_env = os.getenv("USED_HOURS")
    priority_env = os.getenv("PRIORITY_LEVEL")

    # IF Jenkins parameters are missing → defaults
    if req_hours_env is None or used_hours_env is None or priority_env is None:
        req_hours = 2
        used_hours = 5
        priority = "LOW"
    else:
        # ELSE Jenkins parameters are present → use them
        req_hours = eval(req_hours_env)
        used_hours = eval(used_hours_env)
        priority = priority_env.upper()

    manager = CameraResourceManager()
    manager.allocate_existing(used_hours)

    result = manager.allocation_decision(req_hours, priority)

    print("Requested Hours:", req_hours)
    print("Used Hours:", used_hours)
    print("Priority Level:", priority)
    print("Final Decision:", result)
