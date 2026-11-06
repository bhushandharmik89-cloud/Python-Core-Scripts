class ReportHandler:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def generate_summary(self):
        total_salary = 0
        employee_count = 0
        
        with open(self.csv_file, 'r') as file:
            next(file) # हेडर लाइन को छोड़ने के लिए
            for line in file:
                name, role, salary = line.strip().split(",")
                total_salary += int(salary)
                employee_count += 1
                
        print("--- CONSOLE SUMMARY REPORT ---")
        print(f"Total Employees Processed: {employee_count}")
        print(f"Total Salary Payout: INR {total_salary}")
        print(f"Average Salary: INR {total_salary // employee_count}")

# 1. एक नकली CSV फाइल बनाना (Testing के लिए)
with open("employees.csv", "w") as f:
    f.write("Name,Role,Salary\n")
    f.write("Bhushan,Developer,70000\n")
    f.write("Amit,Designer,50000\n")
    f.write("Nitin,Manager,90000\n")

# 2. कोड को रन करके देखना
handler = ReportHandler("employees.csv")
handler.generate_summary()
