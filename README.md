# Treats Sweet Shop
Treat Sweet Shop is a e-Commerce website that I build Using the Django Full Stack Frameworl for my fifth and final project at Code Institute.
Treats Sweet shop is a online sweet store where users can purchase sweets from a wide variety, there is alos a secion on the website that allows users to leave review of their experience shoppping at Treats. I have also include a blog section where that admin can post blog and then registered users are able to comment underneath said blogs.
  
![Am i responsive image](readme-docs/images/amiresponsive.jpg)  

[Click Here To Visit Live Site](https://treats-sweet-shop.herokuapp.com/)  

## Table Of Contents:
1. [UX Design](#ux-design)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Database Diagram](#database-diagram)

2. [Marketing](#marketing)

3. [Features](#features)
    * [Navigation](#Navigation-bar)
    * [footer](#footer)
    * [Home Page](#home-page)
    * [Products Page](#products-page)
    * [Product Detail Page](#product-detail-page)
    * [Shopping Cart Page](#shopping-cart-page)
    * [Checkout Page](#checkout-page)
    * [Blog Page](#blog-page)
    * [Blog Detail Page](#blog-detail-page)
    * [Reviews Page](#reviews-page)
    * [Add Review Page](#add-review-page)
    * [Edit Review Page](#Edit-review-page)
    * [Add Product Page](#add-product-page)

4. [Future Features](#future-features)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgements](#acknowledgements)


### User Stories
Below are the user stories that were added to the Github project, They can be found [here](https://github.com/kpsdev1/Treats-Sweet-Shop/issues) in the issue section of the repository.

**EPIC | Navigation**
- As a User I can easily navigate around the site so that I can view different pages and sections on the site.


**EPIC - Registration & Login / Logout**
- As a User I can Sign-in/ Sign-out so that I can access features when signed in and sign-out so that no one can access my account.
- As a User I can Register an account so that I can use the full functionality of the site.
- As a User I can register with my social media account so that I can sign up faster.

**EPIC - CRUD Functionality**
- As a User I can view a list of products so that I click on one to see the product details.
- As a Superuser I can add a new product so that I can sell them on the site.
- As a Superuser I can edit a product so that I can make changes to a product.
- As a Superuser I can delete a product from the site.
- As a User I can add a product to my shopping cart so that I can purchase it.
- As a User I can Update my shopping cart so that I can change what's in my cart before checking out.
- As a User I can remove a product from my cart so that can remove it an purchase the other items in my cart.
- As a User I can Leave a review so that share my experience of shopping here.
- As a User I can edit my review so that I can I can change it.
- As a User I can Delete my review so that I can remove it.

### Wireframes
Below are the wireframes for the site that I created using balsamiq.
Please note the finished product differed a bit from the wireframes.

<details>
    <summary>Home Page</summary>  

![Wireframe of home page](readme-docs/wireframes/home-wireframe.jpg)  
</details>

<details>
    <summary>Products Page</summary>  

![Wireframe of Products page](readme-docs/wireframes/products-wireframe.jpg)  
</details>

<details>
    <summary>Blog Page</summary>  

![Wireframe of Blog page](readme-docs/wireframes/blog-wireframe.jpg)  
</details>

<details>
    <summary>Blog Details Page</summary>  

![Wireframe of Blog Details page](readme-docs/wireframes/blog-details-wireframe.jpg)  
</details>

<details>
    <summary>Reviews Page</summary>  

![Wireframe of Reviews page](readme-docs/wireframes/reviews-wireframe.jpg)  
</details>

<details>
    <summary>Login Page</summary>  

![Wireframe of Login page](readme-docs/wireframes/login-wireframe.jpg)  
</details>

<details>
    <summary>Register Page</summary>  

![Wireframe of Register page](readme-docs/wireframes/register-wireframe.jpg)  
</details>




### Agile Methodology
Github projects was used to track the development of this website using the agile approach, the project can be found [here](https://github.com/users/kpsdev1/projects/6).

### Typography
- The font that was used for the logo was **Ysabeau**.
- **Montserrat** font was used for the body.

### Colour Scheme
For this site I decide to keep the main color scheme very simple, with the text being black or grey. The logo and the login/ logout page headings in green. I did also have some buttons like the delete, cancel, edit and post buttons red, orange and blue but the main color scheme of the site was black, white, grey.
  
![Colour scheme image](readme-docs/images/colors.jpg)  


### DataBase Diagram
Below is the database diagram that I created using LucidCharts.

![Database Schema image](readme-docs/images/database_schema.jpg)  
- - -


## Marketing
Treats Sweet Shop is a e-commerce website that sells directly to consumers all over the world. It is a B2C focused webite, and the idea of the site is to be able to bring affordable sweets to people all over the world. We have tried to create an easy shopping expierence for the users so that they are able to navigate and purchase products quickly and with ease.


#### Social Media Marketing
As the budget is limited with this business we decided to use cheap cheap organic marketing to start with and maybe in the future when business takes off we will look into some paid advertising. With all this in mind we decided to start with creating a Facebook Business page as Facebook is one of the biggest social media sites and one of the best for promoting a business. By creating a Facebook business page we then could post regular content of what we offer to keep the audience engaged. We have also decided on our Facebook page to do monthly Sweet hamper giveaways where the users just need to follow our page and share the post, this in turn is also cheap way that we can advertise our business. The Facebook page can be found [here](https://www.facebook.com/profile.php?id=100094215246991). (please note Facebook may have removed this page as they tend to remove inactive pages so i have included a screenshot below)


![Facebook Page](readme-docs/images/facebook.jpg)  

#### Email Marketing
We also plan to send out a monthly news letter that details what products we have to offer adn any new products that we may have on the site, as the site is still growing we will be constantly adding more and more products. In order to collect emails for our monthly mailing list we have added a suscribe inbupt field at the bottom of page in the footer where the user can enter there email address and then click suscribe, which will then sign them up to our monthly news letter. We used mailchimp to collect our mailing list.

#### Search Engine Optimization
For the this project I completed research on which SEO keywords to use both short-tail(which are more broad generic and pouular searhch terms ) and long-tail(which are keywords that are more specific, niche, and targeted terms that have a lower search volume and competition) in order to improve the search engine ranking so that our site will be more visible to people online.

#### Sitemap.xml
To help search engines crawl through our website a sitemap was created with alist of all the important Urls and Data on the site. We used XML sitemaps.com to create our sitemap.The website can be found [here](https://www.xml-sitemaps.com/)

#### Robots.txt
A robots.txt file was created to tell search engines where not to crawl on the site.

## Features

### Navigation Bar
- The Navigation bar sits at the very top of each page, The logo is at the right hand side and the navigation links are then to the left of the center of the page with the search, card and login/ register to the right hand side.
- When logged in the links for **Login** and the **Registeration** change to **My Profile** and logout, if the user is a superuser then they will also have a **Add Product** link.
- The Navbar background is a light grey which is colored using the the bootstrap **bg-info** class, the logo is green and the links are black in colour.
- The active page (page that the user is currently on) is displayed in bold text, this makes it stand out much more and is clear to the user which page they are on.
- When on medium to small screens the navigation menu changes to burger menu which shows all the nav links when clicked on.

![Nav bar Image](readme-docs/images/nav.jpg)  

### Footer
- The footer is found at the bottom of every page and responsive for tablet and mobile too.
- There are icon links to the business Instagram and Facebook page(please note these may have been removed byy facebook when you are reading this as they tend to remove fake pages).
- Beneath this is an input box where the user enter their email address, which will allow them to suscribe to the shops newsletter
- The background is also light grey like the Navigation bar.

![footer](readme-docs/images/footer.jpg)
- - -

### Home Page
- The home page has 2 large images that both take up 50% of the screen width on large devices and 100% on small and medium screens.
- The image on the left is a image that i created using illustrator that syas **Treat Yourself** and then underneather the text there nis a button that says **Shop Now**, which once clicked will bring users to the all products page.
- The image on the right is a picture of different sweets on a table.

![HomePage](readme-docs/images/home.png) 
- - -  


### Products Page
- At the top of the Products page, right below the Nav bar there is a H1 heading that says **Products** which is underlined and centered.
- Below this are the Product cards which are displayed in the bootstrap card format, they are displayed 4 across on x-large screens, 3 cross on large screens, 2 on small and medium and 1 accross on x-small screens which makes the page fully resonsive to all devices.
- On the right hand side above the products is a sort filter, where the user can sort by price, low to high or high to low and also can search alphabetically from A-Z or from Z-A.
- Each product displays a picture of the product, the name of it, the price and the category it is in, if the user clicks on the picture it will bring them to the product detail page where they can purchase a product.

![Products](readme-docs/images/products.png) 
- - -


### Product Details Page
- On the products detail you will see the product image on the left and on mobile and small devices this will be the full width bar some padding.
- On the right of this you will have the product name, the price, a description, the category and if the user is an admin you will also see a delete and edit button. 
- Then you will see a quantity selector that can be increased or decrease by the **+** or **-** signs. Below the quantity sign there is a back button that will bring you **Back** to products when clicked and there is also an **Add to cart** button that will add the product to your cart so you can purchase.


![Product details](readme-docs/images/product-details.png) 
- - -

### Shopping Cart Page
- When a user adds a product to thir cart it is deisplayed in the shopping cart page, the user can add multiple products to their cart
- At the top you will see a H2 heading saying **shopping cart** with a horizontial line above and below it.
- Then you will see 4 table headings which will say **Product Info**, **Price**, **Qty**, **Subtotal**.
- In the **Product Info** column you will see a small picture of the product and the product name, in the **Price** colument you will see the price for each product. In the **Qty** you will see the quantity which you can change with the selector and click update, There is also a button to remove a product here. Then in the **Subtotal** column you will see the subtotal price for each item.
- Below the products that are in the shopping cartt towards the right you will see the **Cart Total** and below this the **Delivery** which when added together will give you the **Grand Total**, beneath the grand total in red it will tell you how much more you need to spend to get free deleivery if you havent already surpased it.
- Then  we have a **back** button which will bring the user back to the **Products** page and a **Secure Checkout** button which will bring the user to the secure checkout.

![Shopping cart](readme-docs/images/cart.png) 
- - -

### Checkout Page
- On the check out page at the top you will see a H2 heading that is centered and says **Checkout** with a horizontal line above and below it.
- Beneath this is the order summary which will show a **small picture of the items**, the **name of the product**, the **quantiity**, **the price**, the **delivery** and the **grand total**.
- Then there is the form where the user will have to fill out the form with their **name**, **email**, phone and **address details**. There is also a buton to check that will save the info you have enterd to your profile.
- Then there is the payment input where a user can enter their card details which will then be processed through **Stripe payments** when they click the **complete oorder** button below it.
- Beside the **complete oorder** button there is a **Back** button which will bring the user back to their cart, underneath the buttons in red writing you will see text saying how mcuh your card will be charged.

![Checkout page](readme-docs/images/checkout.png) 

### Blog Page
- On the blog page you will see a link that says **Please log in to read the blogs** and when clicked will bring the user to the sign in page,k where they can sign in or register, only users who are signed in can read each blog post(this link will not be visible if the user is signed in).
- Beneath this you will see the blog post in bootstrap card format which will show a picture, the title of the blog post, the date it was posted on and a blue **Read** button. If the user is not signed in when they click the read button it will bring them to the sign in page.
- If the user is an admin, then above the blog posts on the left side there will be a blue button that says **Add Post** which when clicked will bring the admin to a form where they can enter a new blog post.

![Blog page](readme-docs/images/blog.png) 

### Post Detail page
- At the top of the Post details you will have the Post title displayed using a h2 heading tag, directly below this will then be the image of the blog post sand then below that will be thePost body which will display the main text of a post. Everything is in the centered bar on small and extra small devices where they take up nearly the full width of the screen.
- Below the Post body there is a comment section that will show any comments posted by users(users need to signed in to view the blog post and to also comment)
- Under the comment section there is a **Post A comment** box where a user can enter their comment and when they click post it will be displayed in the comment section. The user will also see a delete and edit button at the top right of their posted comments, if they click the delete button a bootstrap modal will appear asking them to confirm the deletion. If the user clicks the edit button they will be taken to another page that has a comment box with their posted comment in there for them to edit.
- If the user is an admin right below the image on the right side there will be an edit and delete button, if they click the delete button a bootstrap modal will appear asking them to confirm the deletion and if they click the edit button they will be taken to a prefilled form where they can edit the post.

![Post Detail page](readme-docs/images/post-detail.png) 


**Delete Comment Modal**
![Delete Comment modal](readme-docs/images/delete-comment.jpg) 


**Edit Comment Page**
![Edit comment page](readme-docs/images/edit-comment.png) 


**Delete Post Modal**
![Delete Post modal](readme-docs/images/delete-post.jpg) 


**Edit Post Page**
![Edit Post page](readme-docs/images/edit-post.png) 
- - -

### Reviews Page
- At the top of the review page int the center is H1 heading that says **Cutomer Reviews**.
- If the users is signed in then there is a green **Add A Review** button to the right just above the most recent review.
- Then below this are the reviews the revies are each in a light grey colored box, at the top right of the box is the review title then oppiste this at the left hand side is the review stars which can be from 1 - 5.
- Below the title is the username of the person who posted the review and then underneath this is the body of the review, where the user can write a fully detailed review of the site.
- Then at the bottom write of the review you will see the date and thim of which it was psoted on.
- At the bottom left there is a edit and delete button that is visible to the user who psoted the review, the delete button is orange and when click brings up a bootstrap modal asking the user if they want to confirm the deletion. Then beside this is blue edit button which allows the user to edit their review.

![Review Page](readme-docs/images/reviews.png) 
- - -

### Add Review Page
- At the top of the page is a centered H2 heading that says **Write a Review** with a horizontal line above and below it.
- Then there is the form below it with the field of **Title**, **Body**, and the **Rating** which is a drop down whith choices from 1 - 5.
- At the bottom right there is a yellow **Cancel** button that when clciked will bring the user back to the review page, beside this there is a green**Submit** button that once clciked will submit the form and bring the user back to the reviews page where they will see their freshly posted review.

![Add Review Page](readme-docs/images/add-review.png) 


### Edit Review Page
- This is exactly like the **Add Review** page only the H2 heading at the top says **Edit Your Review** and has the form already prpoulated with their previous review so that they can edit it.

![Edit Review Page](readme-docs/images/edit-review.png) 
- - -

### Add Product Page
- This page is only availabe to admins so that they can add a product to the site, on the topn of the page is a H2 heading that is centered and says **Add a Product** with a horizontal line above and below it.
- Below this we have the form with the first input **category** being a drop down, there there is the other inputs **Sku**, **Name**, **Type**, **Description**, **Price**, **Image Url** and **Image**.
- Then below the form on the right is a yellow **Cancel** button that when clicked will bring the admin back tot the products page, beside it is a green **Add Product** button that will add the product to the porducts page once clicked and as logn as the form is filled out.

![Add Product Page](readme-docs/images/add-product.png) 
- - -


## Future Features


## Technologies Used
- [Balsamiq](https://en.wikipedia.org/wiki/Balsamiq) was used to create the wireframes.
- [LucidChart](https://www.lucidchart.com/pages/) was used to design the database schema.
- [HTML](https://en.wikipedia.org/wiki/HTML) was used for the mark up.
- [CSS](https://en.wikipedia.org/wiki/CSS)  was used to style the site.
- [Django](https://www.djangoproject.com/) was the framework that was used.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), django is a python framework.
- [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)) was also used to style the site.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for interactiveness.
- [Gitpod](https://www.gitpod.io/about) was used to create this site and then push everything to github.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) is used to host this site.
- [Github](https://en.wikipedia.org/wiki/GitHub) was used to store the code.
- [Git](https://en.wikipedia.org/wiki/Git) was used for version control.
- [AWS](https://aws.amazon.com/) was used to store the images and static files.
- [ElephantSQL](https://www.elephantsql.com/) was used to store the database.
- - -

## Testing
The testing section can be found [here](TESTING.md).

## Deployment
This website is deployed to Heroku from a github repository, the following steps were taken:

#### Creating Respository on Github
- First make sure you are signed into [Github](https://github.com/) and go to code institutes template, which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Then click on **use this template** and select **Create a new repository** from the drop down. Enter the name for the repository and click **Create repository from template**.
- Once the repository was created, I clicked the green **gitpod** button to create a workspace in gitpod so that I could write the code for the site.

#### Creating app on Heroku
- After creating the repository on github, head over to [heroku](https://www.heroku.com/) and sign in.
- On the home page, click **New** and **Create new app** from the drop down.
- Give the app a name(this must be unique) and select a **region** I chose **Europe** as I am in Europe, Then click **Create app**.

#### Create a database On ElephantSQL
- Log into the [ElephantSQL](https://www.elephantsql.com/) website and click **Create new Instance**
- Enter a **Name** and keep the plan as **Tiny Turtle Free**, then **tags** field can be left blank, Select a region closest to you, I selected **EU-West-1(Ireland)** as I'm in Ireland. Then click **Review** and afterwards click **create instance**.
- On The Dashboard click on your database instance name.
- You will see the details for your database instance, in the url section click on the copy icon to copy the database url.
- Head over to gitpod and create a **Database URL** enviroment variable in your env.py file and set it equal to the copied url.

#### Deploying to Heroku.
- Head back over to [heroku](https://www.heroku.com/) and click on your **app** and then go to the **Settings tab**
- On the **settings page** scroll down to the **config vars** and enter your key and value pairs.
- Then scroll to the top and go to the **deploy tab** and go down to the **Deployment method** section and select **Github** and then sign into your account.
- Below that in the **search for a repository to connect to** search box enter the name of your repository that you created on **github** and click **connect**
- Once it has connected scroll down to the **Manual Deploy** and click **Deploy branch** when it has deployed you will see a **view app** button below and this will bring you to your newly deployed app.
- Please note that when deploying manually you will have to deploy after each change you make to your repository.
- - -

## Credits

## Acknowledgements