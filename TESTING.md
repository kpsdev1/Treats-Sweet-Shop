## Table Of Contents:
1. [Validator Testing](#vadilidator-testing)
    * [Html](#html)
    * [CSS](#css)
    * [JavaScript](#javascript)
    * [Python](#python)
    * [Lighthouse](#lighthouse)

    
2. [Browser and Deivce Testing](#browser-and-device-testing)
3. [User Story Testing](#user-story-testing)
4. [Manual Testing](#manual-testing)
5. [Bugs](#bugs)



## Validator Testing

### HTML
All the site pages were run through the W3C validator to check for any issues and HTML syntax errors. The W3C validator can be found [here](https://validator.w3.org/). As you can see from the below screenshots there are no errors.

<details>
    <summary>Home Page</summary>  
    
![home validation ](readme-docs/images/validator-home.jpg)  
</details>
  
<details>
    <summary>Products Page</summary>  
    
![products validation](readme-docs/images/validator-products.jpg)  
</details>  

<details>
    <summary>Products Details Page</summary>  
    
![products details validation](readme-docs/images/validator-product-details.jpg)  
</details>  

<details>
    <summary>Add Products Page</summary>  
    
![add product validation](readme-docs/images/validator-add-product.jpg)  
</details>  

<details>
    <summary>Blog Page</summary>  
    
![blog validation](readme-docs/images/validator-blog.jpg)  
</details> 

<details>
    <summary>Blog Detail Page</summary>  
    
![blog detail validation](readme-docs/images/validator-blog-details.jpg)  
</details>

<details>
    <summary>Reviews Page</summary>  
    
![reviews validation](readme-docs/images/validator-reviews.jpg)  
</details> 

<details>
    <summary>Register Page</summary>  
    
![Register validation](readme-docs/images/validator-register.jpg)  
</details> 

<details>
    <summary>Login Page</summary>  
    
![Login validation](readme-docs/images/validator-login.jpg)  
</details> 

The **Add Post** and **Edit Post** pages threw errors in the Validator that were related to the Django **Summernote** widget that I used. From searching on slack, speaking to tutor support and also talking to my mentor I was told that this is common with summernote and as I had not written the summernote code, I could ignore these errors as long as my code validated and make a note of it in the readme. These errors do not affect the site functionality in any way. Below you can see a screenshot of the errors.

![summernote errors](readme-docs/images/summernote-errors.jpg)
- - -

### CSS
The CSS stylesheet was put through the W3C Jiqsaw validator to see if there was any errors. The W3C Jiqsaw validator can be found [here](https://jigsaw.w3.org/css-validator/).
As you can see from the below screenshot of the result there were no errors.

![Css Validation](readme-docs/images/css-validator.jpg)
- - -

### JavaScript
The Javascript file was put through Jshint code validator to see if there were any errors. Jshint can be found [here](https://jshint.com/).
- The first image is from the JavaScript file I wrote for the Quantity buttons, it throws no errors but 2 warnings, I spoke to tutor support about this and they are just warnings and can be ignored as they do not affect the code, from looking online it is because the event listener is inside the for loop, when putting the event listener outside the forloop the warnings do not show but the quantity buttons do not work correctly.
- The second JavaScript file is from Stripe and is the same one that is used in boutique ado, it gives one undefined variable, from searching on slack and speaking to tutor support, this is normal behaviour as it is comming form another script.

![JS Validation](readme-docs/images/js.jpg)

![JS Validation](readme-docs/images/stripe-js.jpg)

[Back to the top](#table-of-contents)
- - -


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

*Just to note, the settings.py file gave some **line too long** errors which are related to the default authorization, which I was told can be ignored in this file so I added the **Noqa** comment to them so that the linter would not read them, I also added the comment on a few lines through the project that did not make sense to breakup.*  
- - -  

### Lighthouse
Lighthouse in chrome dev tools was used to generate a report that tests the sites Performance, Accessibility, Best Practices and Seo.
Please note that I have noticed that the performace score on mobile can vary and this is due to render blocking resources from Stripe, JS and bootstrap, I could not figure out how to improve without affecting the site and the fix seems to be way beyond to scope of this course.

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


## Browser and Device Testing
- In order to make sure the site was fully responsive and compatible with different browsers and devices, I tested the site on multiple browsers and devices. 
- The browsers I tested the site on **Chrome**, **Edge** and **Firefox**, when using **Chrome** I was able to use the dev tools and test the site on many different device sizes  like **iPhones 5, 6, 7, 8, X, SE and 12 pro**, **iPad mini and air** , and **Samsung s9+ and s20 ultra**, the site worked as expected on all.
- I also tested the site on a number of real mobile and tables, the devices I tested on were **Samsung S8 and a53**, **iPad 7** and **iPhone 7 and 11**.
- From testing the site on multiple browsers and devices, along with different screen widths, I can confirm that the site is fully responsive and compatible with multiple browsers and devices as you will see from the screenshots below.

#### Browser Screenshots

<details>
    <summary>Chrome</summary>  

![chrome browser test](readme-docs/images/chrome.jpg)
</details>  

<details>
    <summary>Edge</summary>  

![edge browser test](readme-docs/images/edge.jpg)
</details>  

<details>
    <summary>Firefox</summary>  

![firefox browser test](readme-docs/images/firefox.jpg)
</details>

<details>
    <summary>Chrome Dev tools iPhone 5</summary>  

![Iphone 5 image](readme-docs/images/iphone5.jpg)
</details>  

<details>
    <summary>Chrome Dev tools iPhone 6, 7, 8</summary>  

![Iphone 6,7,8 image](readme-docs/images/iphone678.jpg)
</details>  

<details>
    <summary>Chrome Dev tools iPhone SE</summary>  

![Iphone SE image](readme-docs/images/iphonese.jpg)
</details>  

<details>
    <summary>Chrome Dev tools iPhone X</summary>  

![Iphone X image](readme-docs/images/iphonex.jpg)
</details>  

<details>
    <summary>Chrome Dev tools iPhone 12 Pro</summary>  

![Iphone 12 image](readme-docs/images/iphone12.jpg)
</details>  

<details>
    <summary>Chrome Dev tools iPad Mini</summary>  

![Ipad mini image](readme-docs/images/ipadmini.jpg)
</details>  

<details>
    <summary>Chrome Dev tools iPad air</summary>  

![Ipad Air image](readme-docs/images/ipadair.jpg)
</details>  

<details>
    <summary>Chrome Dev tools Samsung S9 </summary>  

![Samsung S9 image](readme-docs/images/samsungs9.jpg)
</details>  

<details>
    <summary>Chrome Dev tools Samsung S20 Ultra</summary>  

![Samsung S20 image](readme-docs/images/samsungs20.jpg)
</details>  



#### Real Device Screenshots

<details>
    <summary>Samsung a53</summary>  

![Samsung a53 image](readme-docs/images/a53.jpg)
</details>  

<details>
    <summary> iPhone 11</summary>  

![Iphone 11 image](readme-docs/images/iphone11.jpg)
</details>  

<details>
    <summary> iPad 7</summary>  

![Ipad 7 image](readme-docs/images/ipad7.png)
</details>  

<details>
    <summary> Samsung S8</summary>  

![Samsung S8 image](readme-docs/images/s8.jpg)
</details>  

<details>
    <summary> iPhone 7</summary>  

![iphone 7 image](readme-docs/images/iphone7.jpg)
</details>  

[Back to the top](#table-of-contents)
- - - 

## User Story Testing


#### Navigation
*As a User I can easily navigate around the site so that I can view different pages and sections on the site.*
- The Navigation is at the top of the page, it is easy to navigate and the current page link is bold which clearly indicates what page you are on.


#### Registration
*As a User I can Register an account so that I can use the full functionality of the site.*
- In the Navigation bar at the top of the page, if a User clicks on the Register link, they will be brought to the registeration page where they can sign up, once they sign up they will be able to access full functionality of the site.


#### Login / Logout
*As a User I can Sign-in/ Sign-out so that I can access features when signed in and sign-out so that no one can access my account.*
- When a User is not logged in the login link will be visible in the navigation bar, the same link will change to logout when the user is logged in.
- When the User enters their login credentials they will be able to access the full fuctionality of the site, when the user is logged out they will not have full access on the site and their account will be secure.

#### View Products
*As a User I can view a list of products so that I can click on one to see the product details.*
- The user is able to click the Products link in the nav bar and this will show a drop down bar where they can select all products or the sweet type they wish to view, which will then bring them to a products page where they can view all or the selected category products.
- If they wish to view a product and purchase they can click on the product image and this will bring them to the product details page where the user is able to order.

#### Add Products
*As a Superuser I can add a new product so that I can sell them on the site.*
- When an admin is logged in with a superuser account there will be an add product link in the navigation, when this is clicked it will bring them to the add product page where they can fill in the form and add another product.

#### Edit Products
*As a Superuser I can edit a product so that I can make changes to a product.*
- When an admin is logged in with a superuser account, on the product details page there will be a **edit** button, when the edit button is clicked it will bring the admin to a prefilled in form with all the orginal product details there so that they can edit it.

#### Delete Products
*As a Superuser I can delete a product from the site.*
- When an admin is logged in with a superuser account, on the product details page there will be a **delete** button, when the delete button is clicked the product will be removed from the site and the database.

#### Add product to cart
*As a User I can add a product to my shopping cart so that I can purchase it.*
- When the user is on the products details page they can click on the blue **Add to Cart** button this will then add the product to their shopping cart, they can also choose the quantity before clicking **Add to Cart**

#### Update Cart
*As a User I can Update my shopping cart so that I can change what's in my cart before checking out.*
- When the user is on the shopping cart page(they can click the shopping cart icon in the Nav bar to access it) they can change the quantity of the proudcts they have in their cart by using the quantity selector and then clicking the **update** button.

#### Remove from Cart
*As a User I can remove a product from my cart so that I can remove it and purchase the other items in my cart.*
- When the user is on the shopping cart page(they can click the shopping cart icon in the Nav bar to access it) under each item in their cart there will be a **remove** button, when they click the **remove** button this will remove the product.

#### Leave a Review
*As a User I can Leave a review so that I can share my experience of shopping here.*
- If the user is signed in they can go to the Reviews page where they will see a green **Add A Review** button which they can click and this will bring them to a form where they can fill in their review, once the review is posted then it will be visible on the reviews page.

#### Edit a Review
*As a User I can edit my review so that I can change it.*
- In the top right of a review that the user has written, there is an **edit** button that when clicked it will bring them to the prefilled form with their review so that they can edit it. A user can only edit a review they have posted.

#### Delete a Review
*As a User I can Delete my review so that I can remove it.*
- In the top right of a review that the user has written, there is an **Delete** button that when clicked it will bring up a bootstrap modal asking the user to confim their deletion, once comfirmed then the review will be removed. A user can only delete a review they have posted.

#### Publish Blog Post
*As a Site Owner I can Publish Blog posts so that customers can read them.*
- If an admin is signed in with a superuser account, then on the blogs page above the Posts at the right hand side will be an **Add Post** button. When the admin clicks this it will bring them to the Add post page where they can fill out a form and submit a blog post.

#### Edit/Delete Blog Post
*As a Site owner I can make changes to blog posts so that I have full control over them.*
- If an admin user is signed in, then on the Post details page below the image at the right-hand side there will be an **edit** button, when clicked this will bring the admin to a prepoulated form where they can edit the blog post.
- If an admin user is signed in, they will see a **delete** button beside the **edit** button. When the admin clicks this a delete modal will pop up asking them to confirm the deletion, on confimation the post will be deleted.

#### Mailing List
*As a Admin I can have a email newsletter signup so that I can collect emails to send information about upcoming deals.*
- At the bottom of each page in the footer there is a input box where a user can enter their email address and click suscribe to signup to the sites mailing list. Mailchimp is used to collect the emails for the mailing list.

#### Order Confirmation.
*As a Admin I would like to send an order confirmation when a product is purchased so that the user knows that the order went through.*
- When a user purchases a product a confirmation email is sent to their email so that they know the order completed sucessfully.

#### Verify Account
*As a Admin I want a verification email sent so that the user has to verify their account.*
- When a user signs up they have to verify their account through a verification email, this stops users from signing up with fake email addresses.

#### Rest Password
*As a User I can reset my password so that I can change it if I have forgotten it or want to change it.*
- If a user forgets their password, they can click the **Forgot Password** link on the login page and then they will be asked to enter their email, this will then send the user an email with instructions on how to reset their password(if their email exists in the database).

- - -

## Manual Testing

#### Navigation
| Feature               | Test Performed                                                     | Result  |
|-----------------------|--------------------------------------------------------------------|---------|
| Logo | Clicking on logo to see if it redirects to home page.                               | Pass    |
| Home | Clicking on Home link brings user to the home page.                                 | Pass    |
| Products | Clicking on the Products link, brings user to the product page.                      | Pass    |
| blog | Clicking on the blog link, brings user to the blog page.           | Pass    |
| Reviews | Clicking on the Reviews link, brings user to the reviews page.                      | Pass    |
| Search| Entering a product into the search box and clicking the icon displays a result for the product.     | Pass    |
| Register | When signed out clicking on the Register link, brings the user to the Registeration page.   | Pass    |
| Login | When signed out, clicking on the Login link, brings the user to the login page.    | Pass    |
| Logout | When signed in, clicking on the logout link, brings the user to the logout page.  | Pass    |
| Correct links display | When a user is signed in or out the correct links display for both.   | Pass    |
| Displays correctly on all pages | Made sure it displays correctly on all pages.               | Pass    |
| Current Page | Nav Link is bold for current page that a user is on.                        | Pass    |
| Responsiveness | Checked to make sure it changes to burger menu on smaller devices.         | Pass      |


#### Footer
| Feature               | Test Performed                                                     | Result  |
|-----------------------|--------------------------------------------------------------------|---------|
| External links | Clicking on social media links opens on a new page.                       | Pass    |
| Private Policy | Clicking on Private policy link opens on a new page with the private policy on it.   | Pass    |
| Subscribing | Entering an email into the Suscribe input box and clicking suscribe, signs the user up to the mailing list   | Pass    |
| Displays Correctly On All Pages | Made sure it displays correctly on all pages.            | Pass    |
| Responsiveness | Checked to make sure link icons display correctly on smaller devices.     | Pass    |


#### Home
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Images | Checked to make sure Images load correctly on large and small devices.            | Pass      |
| Shop Now Button | When clicked brings the user to the products page.                       | Pass      |



#### Products
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Product Cards   | Check to make sure product cards display correctly.                        | Pass      |
| Click on Image| Allow user to click the image part of the card which will then bring them to the product details page.    | Pass      |
| Sort Button | Sorts the Products to the selected choice in the drop down.         | Pass      |


#### Product Details Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Product Content   | Make sure the product content displays correctly.                         | Pass      |
| Edit Product   | When clicked brings the admin to the edit form, this is only visible to a superuser.            | Pass      |
| Delete Product   | When clicked this will delete the product from the site and database, this is only visible to a superuser.        | Pass      |
| Quantity Button  | Allows user to select how much of a porduct they want before adding to the cart. Also checked that 1 is the minimum.    | Pass      |
| Back Button   | When clicked brings the user back to the products page.         | Pass      |
| Add to Cart Button   | When clicked adds the product to cart and also the quantity of that product    | Pass      |


#### Add Product Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Admin Only  | Make sure only a site admin can access this page.                            | Pass      |
| Display Form  | Check to see if all input fields display correctly.                                  | Pass      |
| Submit Filled Out Form  | Fill out all the form and click the Add Product button at the bottom of the page. | Pass      |
| Leave Image Field Blank on Submission  | Check to make sure image place holder displays after submititng. | Pass      |
| Leave Input Fields Blank | Check to make sure form wont submit, and will display warnings. | Pass      |
| Add Product Button | On click it will submit the Product. | Pass      |
| Cancel Button | On click it will bring the user back to the Products list.                  | Pass      |
| Success Message | Success message is displayed at the top right of the screen when a user clicks Add Product.  | Pass      |


#### Edit Product Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Admin Only  | Make sure only a site admin can access this page.                            | Pass      |
| Display Form  | Check to see if all input fields display with the orginal product details.   | Pass      |
| Update Form  | Update the form and click the Update product button at the bottom of the page and check if the product has been updated. | Pass      |
| Update Product Button | On click it will Update the product, and bring the user to the products page where the updated product can be seen. | Pass      |
| Cancel Button | On click it will bring the user back to the Products list.                  | Pass      |
| Success Message | Success message is displayed at the top right of the screen when a user clicks Update Product. | Pass      |


#### Blog 
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Post Cards   | Check to make sure each post card display correctly.                        | Pass      |
| Read Button (when signed in)  | When clicked brings the user to the post details page.      | Pass      |
| Read Button (when signed out)  | When clicked brings the login page.     | Pass      |
| Add Post button  | Is only visible when a superuser is signed in and when clicked brings the admin to the Add post page.     | Pass      |


#### Add Post Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Admin Only  | Make sure only a site admin can access this page.                            | Pass      |
| Display Form  | Check to see if all input fields display correctly.                        | Pass      |
| Submit Filled Out Form  | Fill out all the form and click the Submit button at the bottom of the page. | Pass      |
| Leave an Input Field Blank | Check to make sure form wont submit, and will display warnings. | Pass      |
| Submit Button | On click it will submit the Post and bring the admin back to the blog page where they will see the post. | Pass      |
| Cancel Button | On click it will bring the admin back to the blog page.                  | Pass      |
| Success Message | Success message is displayed at the top right of the screen when a user clicks submit.  | Pass      |


#### Post Details Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Post Content   | Make sure the post content displays correctly.                         | Pass      |
| Edit Button   | When clicked brings the admin to the edit post form, this is only visible to a superuser.            | Pass      |
| Delete Button  | When clicked this will bring up a delete modal for the admin to confim the deletion, this is only visible to a superuser.        | Pass      |
| Comment Section  | Make sure all comments diplay correctly.   | Pass      |
| Edit Comment Button | This is only visible to the user who posted the comment and is in the top right of the comment, when clicked will bring a user to the edit comment page.  | Pass      |
| Delete Comment Button | This is only visible to the user who posted the comment and is in the top right of the comment, when clicked will bring up a bootstrap modal asking the user to confirm the deletion.  | Pass      |
| Post Comment   | When clicked posts the comment that a user has entered in the comment box, this will then be visible in the comment section.     | Pass      |


#### Edit Post Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Admin Only  | Make sure only a site admin can access this page.                            | Pass      |
| Display Form  | Check to see if all input fields display with the orginal post details.   | Pass      |
| Update Form  | Update the form and click the Submit button at the bottom of the page and check if the Post has been updated. | Pass      |
| Submit Button | On click it will update the post, and bring the user back to the posts detail page where the updated post can be seen. | Pass      |
| Cancel Button | On click it will bring the user back to the post details page.                  | Pass      |
| Success Message | Success message is displayed at the top right of the screen when a user clicks Submit . | Pass      |


#### Delete A Post Modal
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Yes Button | When the user clicks the yes button the Post will be deleted.                 | Pass      |
| Cancel Button | When th user clicks the cancel button, the delete modal will disappear and the user will be back on the post details page.     | Pass      |
| Clicking Outside The Modal | When the user clicks anywhere ouside the modal will disappear.    | Pass      |
| X  | When the user clicks on the X button at the top of the modal, the modal disappears.   | Pass      |
| Success Message | Success message is displayed at the top right of the screen when a user clicks yes on the delete modal.  | Pass      |


#### Reviews
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Reviews  | Check to make sure each review is displayed correctly with newest at the top.    | Pass      |
| Add a Review Button  | Is only visible when a user is signed in and when clicked brings the user to the Add review page.    | Pass      |
| Edit button  | This is only visible to the user who posted the review and is at the bottom right of the review, when clicked will bring a user to the edit review page.  | Pass      |
| Delete button  | This is only visible to the user who posted the review and is at the bottom right of the review, when clicked will bring up the bootstrap delete modal where it will ask the user to confirm the deletion.  | Pass      |


#### Edit Review Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Display Form  | Check to see if all input fields display with the orginal review details.   | Pass      |
| Update Form  | Update the form and click the Submit button at the bottom and check if the Review has been updated. | Pass      |
| Submit Button | On click it will update the review, and bring the user back to the Reviews page where the updated Review can be seen. | Pass      |
| Cancel Button | On click it will bring the user back to the Reviews page.                  | Pass      |
| Success Message | Success message is displayed at the top right of the screen when a user clicks Submit. | Pass      |


#### Delete A Review Modal
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Yes Button | When the user clicks the yes button the Review will be deleted.                 | Pass      |
| Cancel Button | When th user clicks the cancel button, the delete modal will disappear and the user will be back on the Reviews page.     | Pass      |
| Clicking Outside The Modal | When the user clicks anywhere ouside the modal will disappear.    | Pass      |
| X  | When the user clicks on the X button at the top of the modal, the modal disappears.   | Pass      |
| Success Message | Success message is displayed at the top right of the screen when a user clicks yes on the delete modal.  | Pass      |


#### Register Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Sign In link | Below the Signup heading, click Sign in link to see if it brings you to the login page        | Pass      |
| Submit Filled Out Form  | Fill out the form and click the Signup button to see if a new account is created and the user is sent a confirmation email. | Pass      |
| Leave Email Field Blank  | Fill out all the form except email field and hit the Sign Up button to see if warnings appear and does not Sign Up.| Pass      |
| Leave Email(again) Field Blank  | Fill out all the form except email again field and hit the Sign Up button to see if warnings appear and does not Sign Up.| Pass      |
| Leave Username Field Blank| Fill out the form and leave Username field blank, to see if it give a warning and does not Sign Up.| Pass      |
| Leave Password Field Blank| Fill out the form and leave Password field blank, to see if it give a warning and does not Sign Up.| Pass      |
| Leave Password (again) Field Blank| Fill out the form and leave Password (again) field blank, to see if it give a warning and does not submit.| Pass      |
| Signup With an Taken Username| Try to register an account that already has the taken username, and see if it fails and warns you that there is an account with that username. | Pass      |
| Signup Button | On click check will it submit the user details and and send them a confirmation email. | Pass      |
| Verify Your Email Address | When the user enters the correct details they will then see a page that tells them we have sent a verifcation email and to follow the steps in the email. | Pass      |


#### Login Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Sign Up Link | Under the Sign In heading , clicking Sign up to see if it brings you to the Register page     | Pass      |
| Leave Username Field Blank| Fill out Password Field and leave Username field blank, to see if it give a warning and does not Sign in.| Pass      |
| Leave Password Field Blank| Fill out the Username field and leave Password field blank, to see if it give a warning and does not submit.| Pass      |
| Sign In with Unregistered Account | Try to sign in with an account that is not registered, to see if it will fail. | Pass      |
| Change 1 Letter in Username or Password | Check will it tell the user that the username or password is incorrect. | Pass      |
| Sign In Button | On click, check will it log the user in if they have entered the right credentials and redirect them to the home page. | Pass      |
| Success Message | Success message is displayed at the top of the screen when a user enters the correct details and clicks Sign in. | Pass      |


#### Shopping Cart Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Show Products in Cart | Check to see if it displays your cart contents correctly.   | Pass      |
| Update Button| Under each product there is an update button, when the user changes the quantity with the quantity selector and clicks update it changes the subtotal for that product. | Pass      |
| Remove Button | Under each product there is an Remove button, that when clicked will remove the product from the cart.   | Pass      |
| Grand Total | Make sure the grand total updates to the total price.  | Pass      |
| Secure Checkout button | Clicking on the secure checkout button will bring the user to the checkout page.  | Pass      |
| Back Button | Clicking on the Back button will bring the user back to the products page. | Pass      |


#### Checkout Page
| Feature               | Test Performed                                                     | Result    |
|-----------------------|--------------------------------------------------------------------|-----------|
| Responsiveness | Checked Page on many different devices, browser and screen widths.        | Pass      |
| Show Order Summary | Above the form display a list of cart contents.  | Pass      |
| Display Form  | Check to see if all input fields display correctly.                        | Pass      |
| Submit Filled out Form  | Fill out all the form and click the Complete order button at the bottom of the page. | Pass      |
| Leave an Input Field Blank | Check to make sure form wont submit, and will display warnings. | Pass      |
| Allow Checkout as Guest | Check to make sure a user does not have to register to purchase items. | Pass      |
| Login / Create an Account | If user is checking out as a guest make sure there is a create account and login option at the bottom to save the information. | Pass      |
| Save Information to Profile | When a registered user is checking out they will have a checkbox at the bottom of the form that they can click to save the information to their profile. | Pass      |
| Prepoulate Delivery Information | If the user has delivery information filled out on their profile it will prepopulate the delivery information on the checkout page. | Pass      |
| Complete Order Button  | When the form is filled out correctly, the order is placed and it is able be seen in stripe and confimation email is also sent to user.     | Pass      |
| Back Button  | When clicked brings the user back to their shopping cart.   | Pass      |


## Bugs

### Fixed
- After creating the project I was getting alot of PEP8 errors, most of which were for **lines too long**. To fix this and conform to PEP8 standards I broke the lines up and made sure they did not go past 79 characters.
- One of the main issues I had was with the quantity selector, it would not update for each item in the shopping cart, only the first product in the list would allow you to update the quantity, this was because I was using **querySelector()** instead of the **querySelectorAll()** method and then having to loop through the items.
- I started to get a CORS issue with fontawesome icons and they started to display incorrectly, from searching online I found that if you add **CORS_ALLOWED_ORIGINS = []** and **CORS_ALLOWED_ORIGIN_REGEXES = []** to the settings file that this fixes the issue and the icons display correctly.

[Back to the top](#table-of-contents)