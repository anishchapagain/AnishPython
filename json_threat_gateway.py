import json

class JSONThreatProtection:
    def __init__(self, max_size=1024, max_depth=10, max_elements=50):
        self.max_size = max_size
        self.max_depth = max_depth
        self.max_elements = max_elements

    def check_size(self, data):
        # Check if data size exceeds max_size
        data_size = len(json.dumps(data).encode('utf-8'))
        if data_size > self.max_size:
            raise ValueError(f"Payload size({data_size}) exceeds allowed limit({self.max_size}).")

    def check_depth(self, data, depth=0):
        # Recursively check for max depth
        if depth > self.max_depth:
            raise ValueError(f"JSON nesting depth({depth}) exceeds allowed limit({self.max_depth}).")
        
        if isinstance(data, dict):
            for value in data.values():
                self.check_depth(value, depth + 1)
        elif isinstance(data, list):
            for item in data:
                self.check_depth(item, depth + 1)

    def check_elements(self, data):
        # Check the total number of elements in the JSON structure
        element_count = self.count_elements(data)
        if element_count > self.max_elements:
            raise ValueError(f"Number of JSON elements({element_count}) exceeds allowed limit({self.max_elements}).")

    def count_elements(self, data):
        # Helper function to count elements recursively
        if isinstance(data, dict):
            count = len(data)
            for value in data.values():
                count += self.count_elements(value)
            return count
        elif isinstance(data, list):
            count = len(data)
            for item in data:
                count += self.count_elements(item)
            return count
        else:
            return 0

    def validate_json(self, data):
        # Perform all checks
        self.check_size(data)
        self.check_depth(data)
        self.check_elements(data)
        print("JSON passed all threat protection checks.")

# Sample usage
json_threat_protection = JSONThreatProtection(max_size=500, max_depth=3, max_elements=20)

# Example JSON payload to validate
sample_json = {
    "user": {
        "id": 123,
        "name": "Alice",
        "attributes": {
            "age": 30,
            "country": "US",
            "preferences": {
                "language": "en",
                "currency": "USD"
            }
        }
    }
}

try:
    json_threat_protection.validate_json(sample_json)
except ValueError as e:
    print("JSON Threat Detected:", e)
