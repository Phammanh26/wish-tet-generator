from datetime import datetime

def log_results(data_string, path, file_name = "default.txt"):
    with open(f"{path}/{file_name}", 'a+') as f:
        current_dateTime = datetime.now()
        f.write(f"---------START: {current_dateTime}----------\n")
        f.write(data_string)
        f.write(f"\n--------END:{current_dateTime}----------\n")