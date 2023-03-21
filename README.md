# API

# About
Library that I use for this API project is 
1. corsheaders - Adding CORS headers allows your resources to be accessed on other domains. 
https://pypi.org/project/django-cors-headers/
2. django-rest-framework - building Web APIs.

# Potential improvements
the serializer for my relational fields in Django models was not with its name instead using id since I add a POST method function. So it can be improve by using SlugRelatedField or StringRelatedField
https://www.django-rest-framework.org/api-guide/relations/

# Production consideration
after testing, this API can go for production however it might not sustain since the Postgres database use is free tier.

# Assumptions
base on each model that this assignment provide:
1. name - it is simple CharField model 
2. mobile_number - since it require only digit, the most suitable model is IntegerField
3. email - django provide special model field for email, EmailField
4. city - since other driver might also have the same city with another driver, we can use Many-to-one fields, ForeignKey
5. district - since it is related to city, 1 city many district, we can use the same Many-to-one fields, ForeignKey
6. language - I assume for this project only have 3 language, Malay, English and Chinese (can add more language). Therefore I only provide CharField model with choices field between those language
7. an_aasigned_truck - I assume many driver can be assign to many truck. therefore I will use ManyToManyField for its model 

for it API endpoints: 
1. /domain/driver - since the assignment ask to return a list of available drivers, I filter the driver using exclude(truck=1), where I excluded 1 that was assigned to "no truck assigned"
                  - and since it also require me to allow filtering using a driver's email, mobile_number, langeuage and his truck's number_plate, I put buildin Django rest framework function Filtering
                  https://www.django-rest-framework.org/api-guide/filtering/
2. /domain/driver/id - since it require me to return a single driver, I use simple GET request with driver ID
3. /domain/driver/ - since it require me to create a single driver, I use simple POST request and save it
