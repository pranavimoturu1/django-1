1. Install the requirements.txt by 
>> pip install -r requirements.txt

2. Create DB with the specified username and password, in terminal

3. Migrate the database by ,
>> python manage.py db init
>> python manage.py db migrate

orelse update some new models by,
python manage.py db upgrade

4. Then run the server by,
>>python manage.py runserver