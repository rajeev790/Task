import csv
import re

def is_valid_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def clean_csv(input_file, output_file):
    seen_ids = set()
    cleaned_data = []

    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['user_id'] not in seen_ids and is_valid_email(row['email']):
                seen_ids.add(row['user_id'])
                cleaned_data.append(row)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=cleaned_data[0].keys())
        writer.writeheader()
        writer.writerows(cleaned_data)

if __name__ == "__main__":
    clean_csv('input.csv', 'cleaned_output.csv')
