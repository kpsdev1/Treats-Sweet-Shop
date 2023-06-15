## Table Of Contents:
1. [Validator Testing](#vadilidator-testing)
    * [Html](#html)
    * [CSS](#css)
    * [JavaScript](#javascript)
    * [Python](#python)
    * [Lighthouse](#lighthouse)
    * [GTmetrix](#gtmetrix)
    
2. [Browser and Deivce Testing](#browser-and-device-testing)
3. [User Story Testing](#user-story-testing)
4. [Manual Testing](#manual-testing)
5. [Bugs](#bugs)



## Validator Testing


### Python
- I tested the project using the PEP8 validator in gitpod, this I had installed from my previous project, but it can be installed by running **pip3 install pycodestyle** then searching for **Python**, Select **Linter** and then select **pycodestyle**. The PEP8 errors would then be underlined in red and also listed in the **Problems tab**. This returned no errors.
- I also tested the site on **Code Institutes pep8 online** website. Which can be found [here](https://pep8ci.herokuapp.com/). As you can see from the below screenshots, no errors were found.

##### Home App
<details>
    <summary>admin.py</summary>  
    
![image of Python testing home admin.py file](readme-docs/images/home-admin.jpg)  
</details>

<details>
    <summary>models.py</summary>  
    
![image of Python testing home models.py file](readme-docs/images/home-models.jpg)  
</details>

<details>
    <summary>urls.py</summary>  
    
![image of Python testing home urls.py file](readme-docs/images/home-urls.jpg)  
</details>

<details>
    <summary>views.py</summary>  
    
![image of Python testing home views.py file](readme-docs/images/home-views.jpg)  
</details>
  

##### Review App
<details>
    <summary>admin.py</summary>  
    
![image of Python testing review admin.py file](readme-docs/images/review-admin.jpg)  
</details>

<details>
    <summary>form.py</summary>  
    
![image of Python testing review form.py file](readme-docs/images/review-forms.jpg)  
</details>

<details>
    <summary>models.py</summary>  
    
![image of Python testing review models.py file](readme-docs/images/review-models.jpg)  
</details>

<details>
    <summary>urls.py</summary>  
    
![image of Python testing review urls.py file](readme-docs/images/review-urls.jpg)  
</details>

<details>
    <summary>views.py</summary>  
    
![image of Python testing review views.py file](readme-docs/images/review-views.jpg)  
</details>

  
##### Profiles App
<details>
    <summary>admin.py</summary>  
    
![image of Python testing profiles admin.py file](readme-docs/images/profile-admin.jpg)  
</details>

<details>
    <summary>form.py</summary>  
    
![image of Python testing profiles form.py file](readme-docs/images/profile-forms.jpg)  
</details>

<details>
    <summary>models.py</summary>  
    
![image of Python testing profiles models.py file](readme-docs/images/profile-models.jpg)  
</details>

<details>
    <summary>urls.py</summary>  
    
![image of Python testing profiles urls.py file](readme-docs/images/profile-urls.jpg)  
</details>

<details>
    <summary>views.py</summary>  
    
![image of Python testing profiles views.py file](readme-docs/images/profile-views.jpg)  
</details>


##### Products App
<details>
    <summary>admin.py</summary>  
    
![image of Python testing products admin.py file](readme-docs/images/products-admin.jpg)  
</details>

<details>
    <summary>form.py</summary>  
    
![image of Python testing products form.py file](readme-docs/images/products-forms.jpg)  
</details>

<details>
    <summary>models.py</summary>  
    
![image of Python testing products models.py file](readme-docs/images/products-models.jpg)  
</details>

<details>
    <summary>urls.py</summary>  
    
![image of Python testing products urls.py file](readme-docs/images/products-urls.jpg)  
</details>

<details>
    <summary>views.py</summary>  
    
![image of Python testing products views.py file](readme-docs/images/products-views.jpg)  
</details>
  

##### Checkout App
<details>
    <summary>admin.py</summary>  
    
![image of Python testing checkout admin.py file](readme-docs/images/checkout-admin.jpg)  
</details>

<details>
    <summary>form.py</summary>  
    
![image of Python testing checkout form.py file](readme-docs/images/checkout-forms.jpg)  
</details>

<details>
    <summary>models.py</summary>  
    
![image of Python testing checkout models.py file](readme-docs/images/checkout-models.jpg)  
</details>

<details>
    <summary>signals.py</summary>  
    
![image of Python testing checkout signals.py file](readme-docs/images/checkout-signals.jpg)  
</details>

<details>
    <summary>urls.py</summary>  
    
![image of Python testing checkout urls.py file](readme-docs/images/checkout-urls.jpg)  
</details>

<details>
    <summary>views.py</summary>  
    
![image of Python testing checkout views.py file](readme-docs/images/checkout-views.jpg)  
</details>

<details>
    <summary>webhook.py</summary>  
    
![image of Python testing checkout webhook.py file](readme-docs/images/checkout-webhook.jpg)  
</details>

<details>
    <summary>webhook_handler.py</summary>  
    
![image of Python testing checkout webhook.py file](readme-docs/images/checkout-webhook-handler.jpg)  
</details>
  

##### Cart App
<details>
    <summary>admin.py</summary>  
    
![image of Python testing cart admin.py file](readme-docs/images/cart-admin.jpg)  
</details>

<details>
    <summary>contexts.py</summary>  
    
![image of Python testing cart contexts.py file](readme-docs/images/cart-contexts.jpg)  
</details>

<details>
    <summary>models.py</summary>  
    
![image of Python testing cart models.py file](readme-docs/images/cart-models.jpg)  
</details>

<details>
    <summary>urls.py</summary>  
    
![image of Python testing cart urls.py file](readme-docs/images/cart-urls.jpg)  
</details>

<details>
    <summary>views.py</summary>  
    
![image of Python testing cart views.py file](readme-docs/images/cart-views.jpg)  
</details>
  

##### Blog App
<details>
    <summary>admin.py</summary>  
    
![image of Python testing blog admin.py file](readme-docs/images/blog-admin.jpg)  
</details>

<details>
    <summary>form.py</summary>  
    
![image of Python testing blog form.py file](readme-docs/images/blog-forms.jpg)  
</details>

<details>
    <summary>models.py</summary>  
    
![image of Python testing blog models.py file](readme-docs/images/blog-models.jpg)  
</details>

<details>
    <summary>urls.py</summary>  
    
![image of Python testing blog urls.py file](readme-docs/images/blog-urls.jpg)  
</details>

<details>
    <summary>views.py</summary>  
    
![image of Python testing blog views.py file](readme-docs/images/blog-views.jpg)  
</details>

*Just to note, the settings.py file gave some **line too long** errors which are related to the default authorization, which I was told can be ignored in this file so I added the **Noqa** comment to them so that the linter would not read them, I also added the comment on a few lines through the project that did not make sense to breakup*  
- - -  

### Lighthouse
Lighthouse in chrome dev tools was used to generate a report that tests the sites Performance, Accessibility, Best Practices and Seo.

<details>
    <summary>Home</summary>  
    
![Home lighthouse test](readme-docs/images/lighthouse-home.jpg)  
</details>

<details>
    <summary>Products</summary>  
    
![products lighthouse test](readme-docs/images/lighthouse-products.jpg)  
</details>

<details>
    <summary>Blog</summary>  
    
![blog lighthouse test](readme-docs/images/lighthouse-blog.jpg)  
</details>

<details>
    <summary>Blog Details</summary>  
    
![blog betails lighthouse test](readme-docs/images/lighthouse-blog-details.jpg)  
</details>

<details>
    <summary>Reviews</summary>  
    
![reviews lighthouse test](readme-docs/images/lighthouse-reviews.jpg)  
</details>

<details>
    <summary>Register</summary>  
    
![register lighthouse test](readme-docs/images/lighthouse-register.jpg)  
</details>

<details>
    <summary>Sign In</summary>  
    
![sign in lighthouse test](readme-docs/images/lighthouse-signin.jpg)  
</details>


## User Story Testing


#### Navigation
*As a User I can easily navigate around the site so that I can view different pages and sections on the site.*
- The Navigation at the top of the page is easy to navigate and the current page link is bold which clearly indicates what page you are on.


#### Registration
*As a User I can Register an account so that I can use the full functionality of the site.*
- In the Navigation bar at the top of the page, if a User clicks on the Register link, they will be brought to the registeration page wehere they can sign up, once they sign up they will be able to access full functionality of the site.


#### Login / Logout
*As a User I can Sign-in/ Sign-out so that I can access features when signed in and sign-out so that no one can access my account.*
- When a User is not logged in the login link will be visible in at the in the navigation bar, the same link will change to logut when the user is logged in.
- When the User enters their login credentials they will be able to access the full fuctionality of the site, when the user is logged out they will not have full access on the site and their account will be secure.

#### View Products
*As a User I can view a list of products so that I click on one to see the product details.*
- The user is able to click the Products link in the nav bar and this will show a drop down bar where they can select all products or the sweet type they wish to view, which will then bring them to a products page where they can view all or the selected category products.
- If they wish to view a product and purchase they can click on the product image and this will bring them to the product details page where the user is able to order.

#### Add Products
*As a Superuser I can add a new product so that I can sell them on the site.*
- When an admin is logged in with a superuser account there will be an add product link in the naviagation, when this is clicked it will bring them to the add product page where they can fill in the form and add another product.

#### Edit Products
*As a Superuser I can edit a product so that I can make changes to a product.*
- When an admin is logged in with a superuser account, on the product details page there will be a **edit** button, when the edit button is clikcked it will bring the admin to a prefilled in form with all the orginal product details there so that they can edit it.

#### Delete Products
*As a Superuser I can delete a product from the site.*
- When an admin is logged in with a superuser account, on the product details page there will be a **delete** button, when the delete button is clicked the product will be removed from the site and the database.

#### Add product to cart
*As a User I can add a product to my shopping cart so that I can purchase it.*
- When the user is on the products details page they can click on the blue **Add to Cart** button this will then add the product to their shopping cart, they can also choose the quantity before clicking **Add to Cart**

#### Update Cart
*As a User I can Update my shopping cart so that I can change what's in my cart before checking out.*
- When the user is on the shopping cart page(they can click the shopping cart icon in the Nav bar to access it) they can change the quantity of the porudcts they have in their cart by using the quantity selector and then clicking the update button.

#### Remove from Cart
*As a User I can remove a product from my cart so that can remove it an purchase the other items in my cart.*
- When the user is on the shopping cart page(they can click the shopping cart icon in the Nav bar to access it) under each item in there cart there will be a remove button, when they click the remove button this will remove the product.

#### Leave a Review
*As a User I can Leave a review so that share my experience of shopping here.*
- If the user is signed in they can go to the Reviews page where they they will see a green **Add A Review** button which they can click and this will bring them to a form where they can fillin their review, once the review is posted then it will be visible on the reviews page.

#### Edit a Review
*As a User I can edit my review so that I can I can change it.*
- In the top right of a review that the user has left there is an **edit** button that when clicked it will bring them to pre filled form with their review so that they can edit it. A user can only edit a review they have posted.

#### Delete a Review
*As a User I can Delete my review so that I can remove it.*
- In the top right of a review that the user has left there is an **Delete** button that when clicked it will bring up a bootstrap modal asking thuser to confim their deletion, oce comfirmed then the review will be removed . A user can only delete a review they have posted.