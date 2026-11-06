import json

class LogParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def filter_errors(self):
        error_logs = []
        # फाइल को रीड करना (File I/O)
        with open(self.file_name, 'r') as file:
            for line in file:
                # सिर्फ ERROR वाली लाइनें फिल्टर करना
                if "ERROR" in line:
                    error_logs.append({"log": line.strip()})
        
        # JSON रिपोर्ट में बदलना
        return json.dumps(error_logs)

# 1. एक नकली लॉग फाइल बनाना (Testing के लिए)
with open("system.log", "w") as f:
    f.write("INFO: System started successfully.\n")
    f.write("ERROR: Database connection failed at 10:15 AM.\n")
    f.write("INFO: User logged in.\n")
    f.write("ERROR: API Timeout occurred.\n")

# 2. कोड को रन करके देखना
parser = LogParser("system.log")
json_report = parser.filter_errors()

print("--- Generated JSON Report ---")
print(json_report)
