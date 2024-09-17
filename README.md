# Green Couture Website

Green Couture is an ecommerce platform specializing in the sale of high-end luxury goods with a focus on sustainability. The store offers pre-owned designer fashion items, including clothing, accessories, and footwear from renowned luxury brands. Green Couture emphasizes eco-consciousness by promoting circular fashion, allowing customers to purchase gently used, high-quality luxury items at more accessible prices while contributing to reducing waste and extending the life cycle of premium products.

## Table Of Contents 

. [Business Model](#business-model)
. [User Experience](#user-experience)
. [Wireframes] (#wireframes)
. [Features](#features)
. [Database] (#database-schema)
. [Technologies Used](#technologies-used)
. [Testing](#testing)
. [Deployment](#deployment)
. [Credits](#credits)

# Business Model 
## Overview

GreenCouture is committed to delivering high-quality, sustainable fashion that not only meets the style needs of our customers but also aligns with our core values of environmental responsibility and ethical practices. Our business model focuses on integrating sustainability into every aspect of our operations, from product sourcing to customer engagement.

## Key Strategies

### 1. Sustainable Product Offerings
- **Eco-Friendly Materials**: We prioritize the use of organic and recycled materials in our products to minimize environmental impact.
   - **Ethical Manufacturing**: Our products are sourced from manufacturers who adhere to fair labor practices and environmental regulations.

### 2. Customer-Centric Approach
   - **Personalized User Profiles**: We offer customized shopping experiences by maintaining detailed user profiles, including default delivery information and order history.
   - **Responsive Customer Support**: Our contact page ensures that customer inquiries and issues are handled promptly and professionally.

### 3. Community Engagement
   - **Educational Content**: We provide FAQs and informative content about sustainable practices and fashion to educate our customers and raise awareness.
   - **Newsletter Subscriptions**: Our subscription model keeps customers informed about new arrivals, promotions, and sustainability initiatives.

### 4. Efficient Operations
   - **Streamlined Order Management**: Our system efficiently handles orders, updates totals, and calculates delivery costs, ensuring a smooth purchasing experience for our customers.
   - **Data-Driven Decisions**: We leverage data from customer interactions, order histories, and feedback to continually refine our products and services.

### 5. **Innovative Technology Integration**
   - **Advanced E-commerce Platform**: We utilize a robust e-commerce platform to provide a seamless shopping experience, including real-time updates on stock, pricing, and delivery options.
   - **Secure Payment Systems**: We integrate secure payment gateways to ensure safe and reliable transactions for our customers.



# User Experience
## User goals are:
 - View products.
 - Create account with my details.
 - Purchase products with credit card.
 - Sign up to newletter to be informed about latest offers.

## This reaches the user goals by:
 - Providing a product page.
 - Allowing the user to create a profile.
 - Having a payment system.
 - Allowing user to enter email to receieve newsletter

## User stories:
 - As a site user, I want to browse and filter through pre-owned luxury items so I can easily find the products that 
    meet my preferences.
 - As a site user, I want to be able to create an account, so that my details can be saved.
 - As a site user, I want to be able to enter my credit card details, so that I can make a purchase.
 - As a site user, I want to receieve emails, so I am up to date with all of the latest offers.


### Colors 
- The website uses 3 main colours. The footer and the nav are both dark grey with green icons and buttons. 
The main body of each page is a lightgray to contrast with the darker shade in the nav and footer. I chose green as this colour represents sustainablity, which is a main priority at Green Couture.


### Font 
- I decided to use the 'Barlow Condensed' font from [GoogleFonts](https://fonts.google.com/) throughout all pages of the website, because it is plain while also being captivating for the viewer. 

### Icons 
- The icons are found in both the nav and footer, located at the bottom of every page. They are taken from [Fontawesome](https://fontawesome.com/), and are all utilised as classes in the i tag, therefore easily targeted and customised. Once an icon clicked, the link will bring you to the desired website.

# Features
### Navbar
- The website incorpates a responsive navbar depending on the screen size in use. The navbar features a dropdown menu with links to the profile page, a search bar and also a link to your basket. When viewing the site on a mobile, a burger icon is on the top left hand corner, and the other buttons are placed on the right hand side.

- If the site user clicks on the search icon, and search bar will toggle beneath so the user can make search queries to find a desired item. 

### Footer 
- At the bottom of each page there is a footer. It is styled in the same color as the navbar the keep consistency within the site(#fc9003). Here, you can find links the social media sites like Youtube, Facebook and Twitter.

### Home Page
- The home page of the site showcases an image of some items in stock on the website. The main heading reads 'Pre-loved luxury goods' and beneaht that, lies a button that links the user to the product page.

### Product Page 
- The product page is where users can browse and find their desired products. At the top of the page, the amount of results can be found along with a sort by box, which allowes the user to arrange the order of products depending on price, rating etc. 

### Product Detail Page
- Once a user clicks on a product, they are brought to the product detail page. This page gives a full breakdown and description of the product. Once a user clicks the 'Add To Bag' button, a pop up will be displayed on the top right corner of the page, notifying the user that the product has been added to their bag. Once the user confirms this by clicking the button they will be brought to the checkout page.

### Checkout Page
- The checkout page is populated with emtpy fields. The user can then enter their full name and email, followed by their delivery address and credit card details. Once the user is ready they can click the complete order button, which will display a loading overlay, followed by success message notifying the user their purchase has been successfull.

# Database Schema

### Category
- **id**: Integer, Primary Key, Auto-increment
- **name**: CharField (max_length=254)
- **friendly_name**: CharField (max_length=254, null=True, blank=True)

### Product
- **id**: Integer, Primary Key, Auto-increment
- **category**: ForeignKey to `Category`, null=True, blank=True
- **sku**: CharField (max_length=254, null=True, blank=True)
- **name**: CharField (max_length=254)
- **size**: CharField (max_length=8, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('Xl', 'Extra Large')] + [('UK6', 'UK 6'), ('UK7', 'UK 7'), ('UK8', 'UK 8'), ('UK9', 'UK 9'), ('UK10', 'UK 10'), ('UK11', 'UK 11')] + [('One Size', 'One Size')], null=True, blank=True)
- **description**: TextField
- **price**: DecimalField (max_digits=6, decimal_places=2)
- **rating**: DecimalField (max_digits=6, decimal_places=2, null=True, blank=True)
- **image_url**: URLField (max_length=1024, null=True, blank=True)
- **image**: ImageField (null=True, blank=True)

### Order
- **id**: Integer, Primary Key, Auto-increment
- **order_number**: CharField (max_length=32, null=True, editable=False)
- **user_profile**: ForeignKey to `UserProfile`, null=True, blank=True
- **full_name**: CharField (max_length=50)
- **email**: EmailField (max_length=254)
- **phone_number**: CharField (max_length=20)
- **country**: CountryField
- **postcode**: CharField (max_length=20, null=True, blank=True)
- **town_or_city**: CharField (max_length=40)
- **street_address1**: CharField (max_length=80)
- **street_address2**: CharField (max_length=80, null=True, blank=True)
- **county**: CharField (max_length=80, null=True, blank=True)
- **date**: DateTimeField (auto_now_add=True)
- **delivery_cost**: DecimalField (max_digits=6, decimal_places=2, default=0)
- **order_total**: DecimalField (max_digits=10, decimal_places=2, default=0)
- **grand_total**: DecimalField (max_digits=10, decimal_places=2, default=0)
- **original_bag**: TextField
- **stripe_pid**: CharField (max_length=254, default='')

### OrderLineItem
- **id**: Integer, Primary Key, Auto-increment
- **order**: ForeignKey to `Order`
- **product**: ForeignKey to `Product`
- **quantity**: Integer (default=1)
- **lineitem_total**: DecimalField (max_digits=6, decimal_places=2, editable=False)

### Contact
- **id**: Integer, Primary Key, Auto-increment
- **title**: CharField (max_length=200)
- **name**: CharField (max_length=50)
- **email**: CharField (max_length=50)
- **content**: TextField
- **created_on**: DateTimeField (auto_now=True)

### Faq
- **id**: Integer, Primary Key, Auto-increment
- **question**: CharField (max_length=255)
- **answer**: TextField

### UserProfile
- **id**: Integer, Primary Key, Auto-increment
- **user**: OneToOneField to `User`
- **default_phone_number**: CharField (max_length=20, null=True, blank=True)
- **default_street_address1**: CharField (max_length=80, null=True, blank=True)
- **default_street_address2**: CharField (max_length=80, null=True, blank=True)
- **default_town_or_city**: CharField (max_length=40, null=True, blank=True)
- **default_county**: CharField (max_length=80, null=True, blank=True)
- **default_postcode**: CharField (max_length=20, null=True, blank=True)
- **default_country**: CountryField (null=True, blank=True)

### Subscribe
- **id**: Integer, Primary Key, Auto-increment
- **email**: EmailField (unique=True)
- **date_subscribed**: DateTimeField (auto_now_add=True)


# Technologies Used 
### HTML 
- HTML was used to write all of the content on each page.

### CSS 
- I used a CSS to style each page. You can all of the styling in the style.css file.

### Python 
- I used Python classes for all of the mdodels used. The FAQ section, newsletter signup, and contact form are all custom made. The product and order model were both taken from the walkthrough and modified. All of the views, forms, and url files are all written in Python code.


### Bootstrap
- I used Bootstrap styling to simply design some elements, for example, the layout of the home page. Any further, more specific styling was written in the style.css file.

### Django 
- I used Django, a python based framework to complete this project. Django provides a structure that makes the development process simple and clean.

## Librares 

### Google Fonts
- I used [GoogleFonts](https://fonts.google.com/) to import the 'Chivo Monu' font. 
### Fontawesome
- I used [Fontawesome](https://fontawesome.com/) for the font styling throughout.

## Platforms

### Github
- I used Github to store my code locally.

#### User Stories
- I used Github user stories to make sure that I was developing the site in the right direction. I added labels to all of my user stories. Each user story was either labelled with Must Have, Should Have, Could Have and Won't Have.
- I also created my own custom board in the Project section in order to keep track of my progress. The board includes three section. To do, In Progress, and Done. I would regualrly make changes to the board to remind myself of other features that needed to be created.

### Gitpod
- Gitpod was used as my IDE for the project development.

# Testing

### Validation 
- HTML has been validated with [W3C HTML5 Validator](https://validator.w3.org/). All pages were tested until the message below was visible.

- CSS has been validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). These were the results.

- Python has been validated with until no errors were found.[CI PYTHON LINTER](https://pep8ci.herokuapp.com/).

### Manual Testing 
- I used Devtools for the development of this website. I often would test different styles in the devtools environment, before writing them in my style.css file. 
- I used the 'Lighthouse' feature to ensure my project scored high in accessibilty on each page.

#### Desktop Testing
- The site was developed on a laptop and the majority of the testing was done on Google Chrome.
- The site was tested on other browsers.
- The site was sent to friends and family with different laptop sizes to get different looks.

### Mobile Testing
- I sent the site to myself and viewed it on a Iphone XR.
- I used Devtools to view the site on many different mobile screen sizes
- The site was also sent to numerous different mobile users to get feedback about its responsiveness.

### Automated Testing
- I decided to not use automatic testing in the production of this project. As you can see, there is nothing in the test.py files. Automatic testing can be more effective than manual testing in the long run, as you can test multiple test cases and find bugs that a human might miss during manual testing. As this website was relatively basic, I could find all of the bugs through manual testing and fix them easily.

# Deployment 
## Local Instructions
- Copy the repo here (https://ruairikeane-project4rua-15b816h0t6u.ws-eu114.gitpod.io/).
- Open up an IDE and paste the copied repo.
- Once opened, install all of the needed dependencies. (pip install -r requirements.txt)
- Create an .env file and add necessary environment variables like 'SECRET_KEY' and 'DATABASE_URL'.
- Run command (python manage.py migrate).
- Create a superuser (python manage.py createsuperuser).
- Run the server with (python3 manage.py runserver).
- The website should now be visible.

## Heroku 
- This project was deployed early on in the development stage with Heroku.
- For deployment, 'DEBUG' was set to 'False'.
- 'ALLOWED_HOSTS' was updated.
- A 'Procfile' was created for Heroku deploy.
- A 'requirements.txt' was added with all of the dependecies listed.
- Two config vars were added. The 'DATABASE_URL' and a 'SECRET_KEY'.
- A python buildpack was also added in the settings tab.


# Credits

## Boutique Ado Walkthrough Project
- I found the 'Boutique Ado'  walkthrough project extemely helpful. The site incorporated many similar features and systmens to my own project and took alot of inspiration of the neat aesthetics of an e-commerce fashion store. 

## Mentor Tutor
- I had three meeting with my Mentor Tutor throughout this process. After each session I had a clear idea of what was needed in order to develop the website further.

## Contact 
- Contact @ruairi.rk@icloud.com

