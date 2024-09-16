# Green Couture Website

Green Couture is an ecommerce platform specializing in the sale of high-end luxury goods with a focus on sustainability. The store offers pre-owned designer fashion items, including clothing, accessories, and footwear from renowned luxury brands. Green Couture emphasizes eco-consciousness by promoting circular fashion, allowing customers to purchase gently used, high-quality luxury items at more accessible prices while contributing to reducing waste and extending the life cycle of premium products.

## Table Of Contents 
1. [User Experience](#user-experience)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)


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


