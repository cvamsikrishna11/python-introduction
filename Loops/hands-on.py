emails = ["vamsi@jjtech.com", "mark@tcs.com",
          "jespo@linkedin.com", "john@netflix.com"]
companies = set()

for email in emails:
    companies.add(email.split('@')[1].split(".")[0])
    #print(email.split('@')[1].split(".")[0])

print(companies)