
import datetime
import base64, os


def send_mail(Message):
    import smtplib
    fadd = 'srutuja497@gmail.com'  # sender's email address
    tadd = 'srutuja497@gmail.com'  # receiver's email address
    msg = Message  # Message to be sent!
    username = 'srutuja497@gmail.com'  # Your username(email ID)
    with open(os.path.dirname(os.path.abspath(__file__)) + '/password.txt', 'rb') as password:
        encryptedData = password.read()
        password = base64.b64decode(encryptedData)  # Your encrypted password for above email ID
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password.decode('utf-8'))
    server.sendmail(fadd, tadd, msg)
    server.close()


with open(os.path.dirname(os.path.abspath(__file__)) + '/Schedules.txt', 'r') as outFile:
    result = outFile.read().split('\n')
    for results in result:
        try:
            currentDateTime = results.split(' ')
            currentDate = currentDateTime[0].split('-')
            currentTime = currentDateTime[1].split(':')
            Message = currentDateTime[2:]
            date = datetime.date(int(currentDate[2]), int(currentDate[1]), int(currentDate[0])).strftime("%Y-%m-%d")
            time = datetime.time(int(currentTime[0]), int(currentTime[1])).strftime("%H:%M")
            res = date + ' ' + time
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            # print(res, now)
            if res == now:
                message = ' '.join(Message)
                send_mail(message)
        except IndexError:
            pass
