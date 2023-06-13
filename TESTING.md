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
