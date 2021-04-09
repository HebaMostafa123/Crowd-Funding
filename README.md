

[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)[![forthebadge](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://forthebadge.com)[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)

![Django - Full Stack Python](https://www.fullstackpython.com/img/logos/django.png)



# Crowd-Funding

Crowdfunding is the practice of funding a project or venture by raising small amounts of money from a large number of people, typically via the Internet. This is a web platform implemented by **Django** framework for starting fundraise projects in Egypt.

### Table of content

- [Get Started]: https://github.com/HebaMostafa123/Crowd-Funding#get-started

- [Main Features]: https://github.com/HebaMostafa123/Crowd-Funding#main-features

- [Built with]: https://github.com/HebaMostafa123/Crowd-Funding#built-with

- [About us]: https://github.com/HebaMostafa123/Crowd-Funding#about-us

##  🔧Get Started

1. Setup your environment by installing Python 3 and Django

2. Clone the project 

3. ```
   cd Crowd-Funding
   ```

   

4. You may need to install those libraries

   ```python
   pip3 install django-countries
   ```

   ```python
   pip3 install --upgrade django-crispy-forms
   ```

5. Start your Apache server and MySQL server

6. Create database with **crowdfunding** name

7. Move to crowdFunding/settings.py 

   - ​	scroll down to DATABASES and change USER,PASSWORD to your own

8. ```python
   python manage.py makemigrations
   python manage.py migrate
   ```

9. ```python
   python manage.py runserver
   ```

   ## 💻Main Features

🔐**Authentication System**

**Registration**

-  User able to register to the web application with his date (First name - Last name - Email - Password - Mobile phone [validated against Egyptian phone numbers] - Profile Picture)
- Once the user register he will receive an email with the activation link and he won't be able to login without activation.

**Login**

-  The user will be able to login after activation using his email and password
- **Forgot Password**
  -   The user will have an option to reset his password if he forgot it to receive a password reset link to his email

**User Profile** 

The user can view his profile that contains:

   - view his profile date except for the email
   - Edit his data and he can have extra optional info other than the info he added while registration (Birthdate, facebook profile URL, country)
   - User can delete his account (Note that there is a confirmation message before deleting)
   - User can view his projects
   - User can view his donations 

**Projects**

The user can create a project fund raise campaign which contains:

- Project data (Title - Details - Category - Multiple pictures - Total target - Multiple Tags - Set start and end time for the campaign) 

- Users can view any project and donate to the total target.
-  Users can add comments on the projects.
- Users can report inappropriate projects.
-  Users can report inappropriate comments.
-   Users can rate the projects.
-  Project creator can cancel the project if the donations are less than 25% of 
  the target.
-   Project page contains  project pictures, overall average rating of the project.

🏠**Homepage** 

-  show the highest five rated running projects to encourage   users to donate.
- Search bar that enables users to search projects by title or tag.
-  The latest 5 projects and latest 5 featured projects.
- List of the categories, user can open each category to view its   projects.

## 📋Built With

- **Django**
- **MySQL**
- **HTML - CSS - JS- Bootstrap**

## 📞About us

[Ahmed Mamdouh](https://www.linkedin.com/in/ahmed-mamdouh96/) 

[Hatem Sayed](https://www.linkedin.com/in/hatem-hashem/)

[Heba Mostafa](https://www.linkedin.com/in/heba-abdelmagead/)

[Mahmoud Atef](https://www.linkedin.com/in/mahmoudbenatef/)

[Mai Maher](https://www.linkedin.com/in/mai-maher/)



