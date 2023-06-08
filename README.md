# booking_App
 
This an flight booking application 

to run this application 

run the following command in Terminal
   
>>pip install -r requirement.txt
   
now in Terminal
>> python
now in python shell 
>>from booking  import app,db

>>app.app_context().push()

>>db.create_all()

>> from booking.model import Admin

>>ad=Admin(name="Demo", email="demo@demo.com",password="demo")

>>exit()

now run the python application in terminal as
>> python test.py


now open http://127.0.0.1:5000/admin

 login with email=demo@demo.com and password=demo
 to have admin access
 
 
 now open http://127.0.0.1:5000 to have home page
 now  register urself and login to show tickets to purchas and purchased 




