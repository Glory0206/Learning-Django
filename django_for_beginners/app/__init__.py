import smtplib

try:
    server = smtplib.SMTP_SSL('smtp.naver.com', 465)
    server.ehlo()
    print("Connection successful!")
    server.quit()
except Exception as e:
    print(f"Error: {e}")
