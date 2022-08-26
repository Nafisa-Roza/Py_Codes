email = input("what is your email address?:  ")
user = email[:email.index("@")]
domain = email[email.index("@")+1 : ]
output = "Your username is {} & your domain name is {} ".format(user,domain)
print(output)