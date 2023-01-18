

"""
(venv) omkar@pansy:~/PycharmProjects/timepass$ git push -u origin main
Username for 'https://github.com': omkarmusale0910
Password for 'https://omkarmusale0910@github.com':
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/omkarmusale0910/TP.git
"""


a=int(input("enter the base"))
b=int(input("enter the power upto."))
l=[0]
for i in range(b+1):
    l.append((pow(a,i)))
for x in l:
    print(x,end=" ")