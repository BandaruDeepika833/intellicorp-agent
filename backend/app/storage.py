import json
import os

class Storage:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)

    def save(self, user_id, company, plan):
        filename = f"{self.base_dir}/{user_id}_{company}.json"
        with open(filename, "w") as f:
            json.dump(plan, f, indent=4)

    def load(self, user_id, company):
        filename = f"{self.base_dir}/{user_id}_{company}.json"
        if not os.path.exists(filename):
            return {"error": "Plan not found"}
        with open(filename) as f:
            return json.load(f)
