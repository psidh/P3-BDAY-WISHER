import smtplib

my_email = "ulast3017@gmail.com"
password = "Qwerty@123#"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email, to_addrs="user1last12@yahoo.com", msg="hi")
connection.close()



