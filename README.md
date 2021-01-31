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
- [GitHub](https://github.com/) Used for version control and hosting software development
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

<img src="https://github.com/Web-Cookie/e_commerce_app/blob/master/media/requirements.png" alt="mockup" target="_blank" rel="noopener" width="850">

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

### Heroku Deployment

Create requirements.txt file which will contain all of the dependencies
In terminal: pip3 freeze > requirements.txt
Create a Procfile to tell Heroku how to run the app in terminal:
web: gunicorn e_commerce_s.wsgi-*:application
Push to Github
Go to Heroku and create a new app, assign a name and chose region which is closes to your location
Go to Resource tab in herokum, then to Add-ons and look for Heroku Postgres select Hobby Dev — Free and click Provision button to add it to your project
Go to settings and Reveal Config Vars

| KEY            | VALUE         |
|----------------|---------------|
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |
| AWS_SECRET_ACCESS_KEY | `<your aws secret access key>`  |
| DATABASE_URL| `<your postgres database url>`  |
| EMAIL_HOST_PASS | `<your email password(generated by Gmail)>` |
| EMAIL_HOST_USER| `<your email address>`  |
| HEROKU_POSTGRESQL_ONYX_URL| `<your postgress>`  |
| STRIPE_PUBLIC_KEY| `<your stripe public key>`  |
| STRIPE_SECRET_KEY| `<your stripe secret key>`  |
| STRIPE_WH_SECRET| `<your stripe wh key>`  |
| USE_AWS | `True`  |


Go to setting.py and temporary comment out the current database settings code and paste below code

```bash 
  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
  ```

This is a temporary settings changes and for security reasons **DO NOT COMMIT TO GITHUB** 
Next, you have to migrate the database models to the Postgress database.
In terminal:
python3 manage.py makemigrations
python3 manage.py migrate
Load the fixture data for categories and products. Please keep in mind that categories should be loaded first as products are very much reliant on categories 
python3 manage.py loaddata <fixture_name>
Create a superuser. In terminal python3 manage.py createsuperuser
Go back to settings.py and delete the postgress database and uncomment the database setting. Add your Heroku app URL to ALLOWED_HOSTS in the settings.py file. 
You can connect Heroku to GitHub to automatically deploy each time you push to GitHub.    
To do so, from the Heroku dashboard follow the steps:
-  **Deploy** section -> **Deployment method** -> select **GitHub**
-  link the Heroku app to your GitHub repository for this project
- click **Enable Automatic Deploys** in the Automatic Deployment section
- Run `git push` command in the terminal, that would now push your code to both Github and Heroku, and perform the deployment.     

However, this did not work for me for some reason, so alternative way is in terminal:

heroku login –i
git push heroku master


##### Hosting the static files on AWS
To have your static and media files hosted you have to go to [AWS S3 Bucket](https://aws.amazon.com/) and create an account. You can read more about how to host static files to AWS S3 Bucket lease read [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)


 ##### Sending real email 
In order to send real emails for the app, you have to go Gmail account and set up the email which will be used for sending app’s emails and set it up in EMAIL_HOST_USER variable along with the password. This variable has to be set in Heroku as well

## Credits
This final challenge felt very difficult but rewarding at the same time. I have to admit that even re-watching 4-10 times the embedded videos I was still getting lost every now and then. Following Code Institute videos gave me a strong insight and feeling of the ability to complete a project from A-Z, using both declarative and imperative languages. I’ve diligently taken notes on all videos in order to re-create a similar project or refer to them for knowledge. There is no need to mention that without Code Institute material even an experienced developer might not satisfy the requirements of the project    Milestone 4 is focused not only on a simple website with minor to none logic, but indeed quite the opposite. It emphasizes a deep back end for a fully functional online store. 

Special shout outs to my mentor Guido! He has been very patient and never gave up on me, also very flexible as I am working during the day. 
Special thanks to slack community and Code institute tutors and of course the course videos. The project is fully based on Boutique Ado videos and it is for educational purposes only. 




