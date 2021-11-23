import re
phone_no_regex= r"[\+\d]?(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

with open("potential-contacts.txt" ,"r") as f:
    file_content = f.read()

phone_no_type = re.findall(phone_no_regex,file_content)
print(len(phone_no_type))
phone_no_type.sort()

all_phone_no = []
for phone_no in phone_no_type:
    if phone_no not in all_phone_no:
        all_phone_no.append(phone_no.replace("(","").replace(")","-").replace(".","-"))


with open("phone_numbers.txt","w") as file:
    for email in all_phone_no:
        file.writelines(f"{email}\n")
    print("phone-done")
print(all_phone_no)
print(len(all_phone_no))


email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
all_emails = re.findall(email_regex , file_content)

all_emails.sort()
emails = []
for email in all_emails:
    if email not in emails:
        emails.append(email)

with open("emails.txt","w") as file:
    for email in emails:
        file.writelines(f"{email}\n")
    print("emails-done")
        