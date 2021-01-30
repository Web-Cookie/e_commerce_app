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