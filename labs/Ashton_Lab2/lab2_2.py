#lab2_2 - Ashton Hill
email="ashtann@costco.rewards.com"
user=email[0:email.find('@')]
company=email[(email.find('@')+1):email.rfind('.')]
print("Email address: "+email)
print("User name: "+user.lower())
print("Company name: "+company.upper())

