import sys
import os

def extract_logs(log_file, date):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{date}.txt")

    found = False  # Track if any logs are found

    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f, open(output_file, 'w', encoding='utf-8') as out:
        for line in f:
            if line.startswith(date):
                out.write(line)
                found = True

    if not found:
        print(f"No logs found for {date}. Check if the date format matches your log file.")

    print(f"Logs for {date} saved in {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    date_to_search = sys.argv[1]
    log_file_path = "/Users/mylappy/tech-campus-recruitment-2025/logs_2024 2.log"  

    extract_logs(log_file_path, date_to_search)
