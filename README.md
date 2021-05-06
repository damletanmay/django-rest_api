# Django-Rest-Api


Django-Rest-Api Is an RESTful API which has certain features like adding data, viewing data, etc.

It can be used for a system across any platform. It doesn't contain any pages or UI because it's just an API.


There are 3 Models in this app.
1. Advisor - To hold Advisors' name & img_url.
2. User - To hold username, password & email of an user.
3. Booking - To hold the bookings of any user.


## Hosting

The Website is Hosted [Here](https://django-rest-api-222.herokuapp.com/)



## Coding & Requirements

1. Back-End In - ```Python```
2. Integration  - ``` Django```
3. Modules/Frameworks - ```Django rest framework, django heroku module```
4. Hosting - ```Heroku, PostgresDB```


Comments are added wherever necessary so that the code can be easily understood.

## Test Cases 

### 1 | i. To add advisors to the DB

path  - https://django-rest-api-222.herokuapp.com/api/admin/advisor/

Request Type - POST

content -type = application / JSON

data format :
```
{

"name": "Tanmay Damle",

"img_url": "https://pbs.twimg.com/profile_images/1305702550977429504/VMhFKZni.jpg"

} 
 ```
Output in Postman:

![i](https://github.com/damletanmay/django-rest_api/blob/master/test%20cases/i.png)



### 1 | ii. To register for being an user
		
path  - https://django-rest-api-222.herokuapp.com/api/user/register/
		
Request Type - POST

content -type = application / JSON

request data: 

```
{

"username": "Tanmay_Damle",

"email":"tanmay@samplemail.com",

"password": "password123"

}
```
Output in Postman:

![ii](https://github.com/damletanmay/django-rest_api/blob/master/test%20cases/ii.png)


### 2. To login as a user.
	
path  - https://django-rest-api-222.herokuapp.com/api/user/login/

Request Type - POST

content -type = application / JSON

request data:
```
{

"email":"tanmay@samplemail.com",

"password": "password123"

}
```

Output in Postman:

![2](https://github.com/damletanmay/django-rest_api/blob/master/test%20cases/2.png)


### 3.To view all advisors.

path  - https://django-rest-api-222.herokuapp.com/api/user/<user-id>/advisor/

Request Type - GET

content -type = application / JSON

data format = None

Login required, from any user account.

Output in Postman:

![3](https://github.com/damletanmay/django-rest_api/blob/master/test%20cases/3.png)


### 4. To book a call.

path  - https://django-rest-api-222.herokuapp.com/api/user/<user-id>/advisor/<advisor-id>/

Request Type - POST

content -type = application / JSON

request data : 
```
{

  "time":"15-05-2021,2:30 PM"

}	
```		
Output in Postman:

![4](https://github.com/damletanmay/django-rest_api/blob/master/test%20cases/4.png)
		
### 5. To view all bookings of an user.

path  - https://django-rest-api-222.herokuapp.com/api/user/<user-id>/advisor/booking/

Request Type - GET

request data: None

Output in Postman:

![5](https://github.com/damletanmay/django-rest_api/blob/master/test%20cases/5.png)
