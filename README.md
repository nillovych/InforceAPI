After opening the project - write text below in your terminal: 
"python manage.py makemigrations RestrauntApp",
"python manage.py migrate"
Data will migrate into my Postgre database powered by Azure.

Then write "python manage.py runserver" to run the system.
Open the local host(link will appear in terminal).

To check work of authorizations use superuser: 
            {
                log: root 
                pass: 1234
            }

The user auth based by this url: /api/v1/token/
After, you can see poll by this url: /api/v1/token/polls/
You can see menu dict by this url: /menu
Restraunt dict by this url: /restraunt

You can try to add, change or delete Polls, Restraunts, Menus 
at admin-control panel by this url: /admin/
Using superuser account - root
or try account from groups user and restorators to check their
permissions(restorator: all operations with Menu and Restraunts;
            user: all operations with Choice and can view Menu):
            {
                log: rest1, pass: qwerty1234!
                log: user1, pass: qwerty1234!
            }
Thanks for your Attention!
