# e_commerce_app
[![Build Status](https://travis-ci.com/Web-Cookie/e_commerce_app.svg?branch=master)](https://travis-ci.com/Web-Cookie/e_commerce_app)

The live website can be viewed [here](https://e-commerce-s.herokuapp.com/)     
[Responsive mockup](http://ami.responsivedesign.is/?url=https://8000-b1cf53cc-2b25-469b-af3b-7158f95cb3fc.ws-eu03.gitpod.io/)

<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Home.PNG" alt="mockup" target="_blank" rel="noopener" width="850">

## Milestone 4 Project
This project is to demonstrate full stack development skills which in this case have enabled the creation of an e-commerce store for dirt bike products such as; clothing, protection, helmets, boots, etc. I have decided to create an online store because I plan on turning it into a real functioning business. Python and Django framework along with HTML and CSS have been used for its creation.

## UX and Design

#### Wireframe

Wireframing was done through [Balsamiq Wireframes](https://balsamiq.com/)
* [AllProducts]( https://github.com/Web-Cookie/e_commerce_app/blob/master/wireframes/allproducts.PNG)
* [Checkout]( https://github.com/Web-Cookie/e_commerce_app/blob/master/wireframes/checkout.png)
* [LandingPage]( https://github.com/Web-Cookie/e_commerce_app/blob/master/wireframes/landing_page.PNG)
* [MyProfile]( https://github.com/Web-Cookie/e_commerce_app/blob/master/wireframes/my_profile.PNG)
* [Registration]( https://github.com/Web-Cookie/e_commerce_app/blob/master/wireframes/registration.PNG)
* [SignIn]( https://github.com/Web-Cookie/e_commerce_app/blob/master/wireframes/signin.PNG)

#### Target Group
This online shop targets people who are into dirt bikes and who are looking for that type of equipment. The concept is to provide high quality protection products like body armor and helmets as this sport/hobby can be quite dangerous, hence, finest equipment is from paramount importance. Also, the shop enables nice UX with its simplicity and ease of access. Just with a couple of clicks a customer can place his or her order without being re-directed to extra links. An order can be placed even without creating an account which is a feature that I personally find very useful.


#### Features
E-commerce store provides the below features
#### Home Page - serves as the initial landing page for all users
- **Navigation bar (mobile top header)** - - occurs only on smaller screen such as smart devices and tablets
- **Search** - The search function enables user to search by a specific category or brand
- **logo**, that is clickable and redirects to the landing page 
- **Main-nav with quick links** to the main pages: 'All products', Clothing, 'Protection equipment', Special Offers'.
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Navigationbar.PNG" alt="mockup" target="_blank" rel="noopener" width="850">
The landing gives an overview of the nature of the online shop.
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Home.PNG" alt="mockup" target="_blank" rel="noopener" width="850">

#### All Products page
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Allproduts_s.PNG" alt="mockup" target="_blank" rel="noopener" width="850">
Provides all products available to customers. It enables filtering by price, category, and rating.

#### Clothing page
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Jerseys.PNG" alt="mockup" target="_blank" rel="noopener" width="850">
Re-directs users to all clothes and eyewear available

#### Protection Equipment 
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Protection_equipment.PNG" alt="mockup" target="_blank" rel="noopener" width="850">
Takes users to all protection products

#### Special Offers
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Special%20offers.PNG" alt="mockup" target="_blank" rel="noopener" width="850">
Shows deals, clearance, and specials

#### Login/Register page
- Allow new user to register for an account and allow existing users to login to their account.
- **Register** - Username, email, and password are required. Emails are checked in the database against already existing profiles. Emails and password must be entered twice for confirmation reasons 
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/SignUpp.PNG" alt="mockup" target="_blank" rel="noopener" width="850">
- **Message** - A verification email will be sent to user's email and after confirming clients will be able to log into his or her account with credidentials provided
- The login page only requires the user to input there username and password. There is a link to the register page so a user can create an account, and a password reset link if a user has forgotten or lost their password and remember checkbox to store logging details.
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Loginn.PNG" alt="mockup" target="_blank" rel="noopener" width="850">

#### Shopping bag page
- **Product Info** - Displays a summary of the products ordered along with an image and price
- **Update quantity** - User can amend the quantity of the chosen product by clicking the '-' or '+' to increasing or decreasing the quantity in bag
- **Remove** - Allows the user to remove a product from the bag
- **Keep shopping** - Redirects user to All products page
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Loginn.PNG" alt="mockup" target="_blank" rel="noopener" width="850">
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Loginn.PNG" alt="mockup" target="_blank" rel="noopener" width="850">

#### Checkout page
- **Order summary** - Gives a detailed overview of all products in the bag, displaying qty, price, image, and description of the product/s
- **Complete Order** - Allows the user to make a card payment.
- **Stripe** - Allows users to pay securely using Stripe payment
- **Adjust Bag** - Takes user back to shopping bag where he or she can make changes to the order
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Checkout%20page.PNG" alt="mockup" target="_blank" rel="noopener" width="850">

#### Checkout Success page
- **Thank You page** - User receives confirmation that the order has been placed, also an email is send to user’s account. The thank you page display an order number and details of the order
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Confirmation%20of%20payment.PNG" alt="mockup" target="_blank" rel="noopener" width="850">

#### Admin service managment
- Only available for superusers
* **Add | Edit | Delete a Product** superusers can add, edit, or delete products
<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/Add%20product.PNG" alt="mockup" target="_blank" rel="noopener" width="850">

### Features to Implement
Images 404 and 500 errors need to be implemented 

### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/) 
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) 

### Libraries and Frameworks
- [Django](https://www.djangoproject.com/) - Django framework for developing the project
- [Bootstrap](https://www.bootstrapcdn.com/) - used for layout and design and fonts
- [Google Fonts](https://fonts.google.com/) - to import fonts.
- [FontAwesome](https://fontawesome.com/) - to provide icons used across the project. 
- [JQuery](https://jquery.com/) - to initiate Bootstrap functions
- [Gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server to enable deployment to Heroku
- [Psycopg2](https://pypi.org/project/psycopg2/) - to enable the PostgreSQL database to function with Django
- [Stripe](https://stripe.com/ie) -to enable financial tranactions
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - to style Django forms

### Tools
- [GitPod](https://www.gitpod.io/) - has been used as an online IDE, the online version of visual studion
- [GitHub] Used for version control and hosting software development
- [PIP](https://pip.pypa.io/en/stable/installing/) - pip3 install for installing various functions
- [AWS S3 Bucket](https://aws.amazon.com/) -  Storage of static and media files
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for compatibility with AWS
- [Travis](https://travis-ci.org/) - For Testing
- [Balsamiq](https://balsamiq.com/) - for Wireframing

### Hosting
- [**Heroku**](https://www.heroku.com/) - Hosting platform where complete and fully funcional app was deployed

## Testing
### Validation
HTML:  https://validator.w3.org/ for HTML code

CSS:  https://jigsaw.w3.org/css-validator/ for CSS code

JavaScript:  https://jshint.com/ for Javascript code

[PEP8 Online]: http://pep8online.com/ for Python code

# Travis Integration Testing

The integration testing of my code has been done through Travis CI. Total of 13 tests have been implemented. Primarily, under products. 

tests_forms.py, tests_models.py, tests_views.py, tests_urls.py

You can run these by typing python3 manage.py test or go to the top of the ReadMe file and click on build passing button

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>


## Deployment
This project was developed through [GitPod](https://www.gitpod.io/) online IDE and using Git & GitHub for version control. It is hosted on the [Heroku](https://heroku.com/) platform. Static and media files are hosted by AWS S3 bakets
### Local Deployment
To be able to run this project, the following tools have to be installed:
- [GitPod](https://www.gitpod.io/) 
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) 
- [Python3](https://www.python.org/download/releases/3.0/)    

Also, account creation needs to the below apps
- [Stripe](https://stripe.com/en-ie) For payments 
- [AWS](https://aws.amazon.com/) for hosting the static and media files 
- [Gmail](https://mail.google.com/)to be able to send confirmation emails upon registering

#### Directions
The easiest is to open the terminal and do the following command:
git clone https://github.com/Web-Cookie/e_commerce_app

Create environment variables. Please keep in mind that this process may vary depending on the IDE you’re using    
    - Create .env 
    - Add .env to the .gitignore file in your project's root directory
    - In .env file set the following variables 
    
    import os  
   
    os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    
    os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    
    os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"     
     ```
       
    
Install all requirements from the requirements.txt 
In the terminal type pip3 install -r requirements.txt 
All of the below should be in your requirements.txt file

asgiref==3.3.1
boto3==1.16.60
botocore==1.19.60
dj-database-url==0.5.0
Django==3.1.4
django-allauth==0.44.0
django-countries==7.0
django-crispy-forms==1.10.0
django-storages==1.11.1
gunicorn==20.0.4
jmespath==0.10.0
oauthlib==3.1.0
Pillow==8.0.1
psycopg2-binary==2.8.6
PyJWT==1.7.1
python3-openid==3.2.0
pytz==2020.4
requests-oauthlib==1.3.0
s3transfer==0.3.4
sqlparse==0.4.1
stripe==2.55.1

In the terminal in your IDE migrate the models to crete a database using the following commands:    
python3 manage.py makemigrations`    
python3 manage.py migrate    
Load the data fixtures(**categories**, **products**) in that order into the database using the following command:    
python3 manage.py loaddata <fixture_name>        
A superuser has to be created in order to be able to access the admin control panel. In the terminal type python3 manage.py cretesuperuser.
The superuser access will enable you to add, edit or delete products, something that clients won’t have access to.
After all this steps, you can run server locally by typing in the terminal
python3 manage.py runserver
To access the admin control panel you can simply add /admin/ at the end of the url link



