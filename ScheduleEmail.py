from crontab import CronTab
import getpass, os
import base64


def set_password():
    password = getpass.getpass('Enter your Email password for sending mails: ')
    encryptedData = base64.b64encode(password.encode('utf-8'))
    with open(os.path.dirname(os.path.abspath(__file__)) + '/password.txt', 'wb') as password:
        password.write(encryptedData)

if __name__ == '__main__':
    set_password()
    
    my_cron = CronTab(user='RutujaShinde')
    
    job = my_cron.new(command='python ' + os.path.dirname(os.path.abspath(__file__)) + '/SendMail.py')
    
    job.minute.every(1)
   
    my_cron.write()
