import sys

if len(sys.argv) != 3:
    raise ValueError("Zla liczba argumentow")

input_file = sys.argv[1]
output_file = sys.argv [2]

def is_email(text):
    return text.count("@") == 1

def clean_email(text):
    return text.strip().lower()
emails = set()
with open(input_file) as file_in:
    for line in file_in:
        if is_email(line):
            emails.add(clean_email(line))

with open(output_file, "w",) as file_in:
    out_f.write("\n".join(sorted(emails)))

