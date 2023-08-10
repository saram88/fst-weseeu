## Project WeSeeU / Intro
  
WeSeeU is a service company that offers virtual services for other companies in marketing and IT services. 
WeeSeU can book customers themselves in the associated booking system provided, 
but the customer himself can also choose to create a profile so that he can book services that he wants WeeSeU to perform.
The system is fully developed to start using. There is development potential but is fully used in the current version.

### Why WeSeeU ?

WeSeeU was born after a long time of insight. Realization that there are simpler and more cost-effective ways to handle both smaller and larger projects, which are not within the entrepreneur's core business but which are necessary to carry out in order to maintain their place in the market, carry out their mission towards their customer or to develop. With our solution, the customer can easily book in for services through our user-friendly booking system.

![Home](/documentation/readme_images/home_menu.png)

### User Experience(UX)

My costumer is other business that run small or middle companys that need help to their administration. 
By joining WeSeeU, you can easily focus on what your core business offers instead. Many of WeSeeU customers have no idea how much time is spent on the work that cannot be derived to a certain income, and what this overhead cost is difficult to master financially. If you look at what your own hourly wage is per month, and then evaluate the number of hours spent in overhead tasks, you can easily see what it costs you. Time you could instead spend on developing your core business. WeSeeU always offers "try for hours" so you as a customer can know with certainty that you are getting quality for the money!

## User Stories

### Getting Started/ Enviroment Setup

- As the developer, I can create a new project so that I can develop the website.
- As the developer, I can create a new project on GitHub so that I am ready to start developing the website.
- As the developer I can install Django and any other libraries needed so that I can start developing the website.
- As the developer, I can test the project locally so that I will be able to see any changes locally before pushing to GitHub / Heroku.

### | Landing Page 
As the developer, I can design a functional, easy-to-use landing page so that users can easily navigate through pages and use the site.
#### User Stories
- As a user, I can contact the developer through social links so that learn more about their work or get questions answered.
- As a user, I can use the website on all device sizes so that I can see the same information on small and large devices.
- As a user, I can use the navigation bar so that I can view all pages of the website easily

### | Initial Deployment
As the developer, I can deploy the app on Heroku so that users can view and interact with the site publicly.
#### User Stories
- As the developer I can deploy the app to Heroku so that I can ensure it works properly before heavily starting development on the site.
- As the developer, I can link the GitHub repository to the Heroku app so that when I commit changes on GitHub they are reflected on Heroku automatically.

### | Website Aesthetics
As the developer, I can design an aesthetically pleasing webpage so that users can easily navigate the site.
#### User Stories
- As the developer, I can use complimentary colors so that users can navigate the website easily.
- As a user, I can see the favicon on the web tab so that know I'm on the WeSeeU page.
- As a user, I can click the logo of the website so that I can easily get back to the homepage.

### | User Account
As the developer, I can create a register / login feature so users and create an account and login / logout.
#### User Stories
- As a user I can sign up, log in and log out so that I can see the features available to registered users.

### | Site Administration & Booking
As a site admin, I can manage all bookings and create, read, update and delete services items so that I can control site bookings.
#### User Stories
- As a user, I can create, read, update or delete service items so that the menu is up to date.
- As a logged in user, I can click the 'booking' button so that I can easily view and manage my booking.

### | Testing & Documentation
As the developer, I can concisely document my testing and deployment methods so assessors and other developers can understand the website from a technical standpoint.
#### User Stories
- As the developer, I can create a README.md file so that other developers and the assessors can have an in-depth look at the website's structure and programming.
- As the developer, I can create a TESTING.md file so that the assessors can see the bugs and their solutions identified and the validation passed.
- As the developer, I can concisely describe the Heroku deployment process so that others know how to deploy an app on Heroku.

### | Error Pages
As the developer, I can create status error pages so users will know if there is a problem.
#### User Stories
- As the developer I can create a 500 error page so that users will know if there are internal server errors.
- As the developer I can create a 404 error page so that users will know when they've tried to access a page that doesn't exist.


### Design

The website design is set in simple, paragraph form, which is intended to make it easier for the reader to navigate. The navigation bar is clear on each page, as is the footer and the pages are labelled with a 'banner' format thus ensuring users know where they are at all times. 

#### Color Scheme
The color palette was created using the palette generator [Coolers](https://coolors.co/).

The color scheme is chosen based on what statistically you say colors are associated with. Green is associated with harmony, growth and nature. Green color can have a calming effect as well as make us more focused on specific tasks.  It together with a gray tint reflects well.

All combinations of the colors used illustrate a contrast between background and text to ensure maximum user accessibility.

![Color Palette](/documentation/readme_images/color%20palette.png)

#### Image
One background picture that floats when you move the webbpage up and down. The other images follow the theme to match UX and so my costumer get a good experience.
 

#### Fonts
 The "Times new roman" 
 
## Agile Methodology

The agile methodology was used throughout project development. User stories and the steps of the process are shown on [GitHub projects](https://github.com/users/saram88/projects/8/views/1)

Creating User stories for this project facilitated a smooth working environment where both general and something i need to make a good overwiev what i should do and want to do. 

### Form Validation
- All fields in the contact forms are required. If a user attempts to submit the form without filling in all fields, a warning text will appear at the bottom of the form asking them to complete the fields. The form will not submit until all fields are filled in.


## Data Model
I used principles of Object-Oriented Programming throughout this project and Django’s Class-Based Generic Views. Django AllAuth was used for user authentication.

The Customer model displays a working contact form on the Contact page and in Booking page. [Email js](https://www.emailjs.com/) was also used to ensure queries are addressed. For the purpose of this project, the emails arrive in my personal inbox.

## Database Design
An Entity Relationship Diagram was created using [DB Designer](https://erd.dbdesigner.net/) to better visualize the relations between data tables. 

![Database Schema](/documentation/readme_images/db.png)


## Security Features and Defensive Design

### User Authentication

- Django's LoginRequiredMixin is used to ensure that any requests to access secure pages by non-authenticated or, in some cases, non-admin users, are redirected to the login page. 

## Features

### Header

![Header](/documentation/readme_images/navbar.png)

**Logo**
- A customized logo was created using [Canva](https://www.canva.com/), it was made by my self.
- The logo is positioned at the top left of the navigation bar. The logo is linked to the home page so the user can easily navigate the site.

![Header](/documentation/readme_images/logo.png)

**Navigation Bar**

- The navigation bar is present at the top of every page and includes all links to the other pages.

### Footer
- The footer section includes working links to GitHub, Twitter, Instagram and Facebook. Clicking each link will open a separate browser page to the login of that website.

### Home Page

**Call to Action Section**
- The landing page includes a call to action section which encourages the user to book a service with WeSeeU.

![Landing Page - Call to Action](/documentation/readme_images/calltoaction.png)


**About**
- The 'About' section gives a brief overview of who we are so they can get saftey inscoure that we are a good company.

![Successful Log Out](/documentation/readme_images/aboutus.png)


**Log in or log out messeage** 

- Success messages inform the user if they have logged in and logged out successfully and are present on the site for 3 seconds before automatically disappearing.
- Django allauth was installed and used to create the Sign up, Log In and Log Out functionality and pages. 

![Successful Log Out](/documentation/readme_images/logout.png)


### Menu Page

**Menu Section for non-authenticated and non-admin visitors**

- This page displays that you can schoose to be a member
- Non logged in visitors and non-admin users will see a static page with items, they will not be able to add, edit, or delete items.


**Menu Section for admin users**

- The overall look of the page is the same. If a user is logged in as an Admin super user, they can add, edit and delete menu items.

![Menu Page - Admin users](/documentation/readme_images/adminnavbar.png)


### Contact Us Page
The Contact Us page includes a Google Map of where the company is. Given that WeSeeU is not a real place, a substitute was used for the purpose of this project. 

![Contact Us Page](/documentation/readme_images/contactus.png)

- The page includes a contact form on the left-hand side that was implemented with [Email JS](https://www.emailjs.com/) and a Google Map on the right side.

- Filling out the contact form will send a message to my personal in box. The user is alerted both after successfully filling out and submitting the form and if they need to fill in a field. All fields are obligatory. The success or error messages stay for three seconds and disappear automatically.


### Book A Service

![Book A service Page](/documentation/readme_images/addbooking.png)

- The Add booking page is visible only to authenticated, logged in users.
- The user fills out the form, selecting a service choice and the dates they want to book. 
- The dates are static by default to show the formatting and the user can change to different dates.
- Clicking 'Add booking' will take them to the My Bookings page where they will see their booking.


### My Bookings

- The My Bookings page shows the bookings of the logged in user.
- On each booking card, there are buttons to edit and delete the booking. 
- Users can only delete their own bookings.

![Edit Bookings Page](/documentation/readme_images/mybooings.png)

### Edit A Booking

- The Edit Your Booking card shows the specific booking the user wants to edit with the fields pre-populated.
- They can change any of the fields and click 'Update' when finished.
- Clicking 'Update' will save their changes and revert them back to the My Bookings page where they will see a message saying their booking was updated correctly.
- The success message remains on the screen for three seconds before fading automatically. 


### Delete A Booking

![Delete A Booking Page](/documentation/readme_images/deletebooking.png)

- Logged in users can delete their own bookings by clicking the 'delete' button on the My Bookings page. 
- They will be taken to the Delete Your Booking page and asked if they're sure they want to delete this specific booking.
- Clicking 'Cancel' will revert them to the My Bookings page.
- Clicking 'Delete Booking' will delete that booking permanently and take them back to the My Bookings page where they will see a message saying their booking was deleted successfully and they will no longer see that booking.



### Future Features

I have some improvements but have chosen not to include them in this version as there was not enough time, but also because I received the feedback from friends and family at a final stage, so automatically chose to include it in a next version.


1. I would like the costumer to sign in and add a booking and get a confirmed message right away, and not need to wait for us to send them a confirming mail.
3. Incorporate a payment option, rates and pricing for booking. 
4. A page that you can se serivces in a list and se other costumers review and get tips what they should book.
5. A chat, so the costumer can ask questions right away and book faster. And if you are a paid costumer you get priority service. 
6. That you can move around on the webpage from headmenu to booking and in the other direction as well.

## Deployment - Heroku

The following steps were taken to deploy the live website to Heroku from the GitHub repository:

### Create a Heroku App:
- Log into your heroku account or create an account.
- On the main page click the 'New' button at the top right corner and select 'Create New App' from the dropdown menu. 
![Heroku Create App](/documentation/readme_images/createnewapp.png)
- Enter in a unique app name
- Select your region
- Click 'Create App'


### Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file:
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save all files and make migrations.
- Add the Cloudinary URL to env.py
- Add the Cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

### Create files / directories
- Create a requirements.txt file
- Create directories in the main directory; media, static and templates.
- Create a "Procfile" in the main directory and add the following: web: gunicorn project_name.wsgi
- Make sure the Procfile is capitalized and only has one line.

### Update Heroku Config Vars
Add the following Config Vars in Heroku:
- SECRET_KEY value 
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1
- HEROKU_POSTGRESQL_OLIVE_URL value
- DATABASE_URL value

### Deploy
- Make sure DEBUG = False in the settings.py
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is updated.
- Click 'Open App' to view the deployed live site.

The site is now live and operational.

## Languages

- Python
- HTML
- CSS
- Javascript

#### Format for commit messages

1. Git add .
2. Git commit -m "TEXT"
3. Git Push


### Most common bugs when i build my site

- Could not deploy to heroku. Understood i need to set up my static files to another (Cloudinary) to make it work
  
## Credits 

I have pick up idea from my family and friends what they thougt can be a good webpage for my future costumer, but i have also pick up ideas when it comes to this README from [Github] (https://github.com/Kaylaesmith1/bed-and-breakfast/blob/main/README.md) 
I have also use google translate to make my english to work well. 


### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site

## Frameworks - Libraries - Programs Used 
- [Font Awesome](https://fontawesome.com/): The icons in the footer
- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): Authentication library used to create user accounts
- [PostgreSQL](https://www.postgresql.org/) Used as the database for this project.
- [Heroku](https://dashboard.heroku.com/login) - Used as the cloud-based platform to deploy the site.
- [DB Designer](https://erd.dbdesigner.net/) - Used to visualize data models.
- [Favicon](https://favicon.io/) - Used to create the icon for the browser tab.
- [GitHub](https://github.com/) - Used for version control and agile methodology.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [PEP8 Online](https://pep8ci.herokuapp.com/#) - Used to validate all Python code pages in the project.
- [Jshint](https://jshint.com/) - Used to validate the JavaScript page.
- [Coolors](https://coolors.co/) - Used to create color scheme.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) Used to manage Django Forms
- [Cloudinary](https://cloudinary.com/): Used to upload all images used on the website.
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/): CSS used for developing responsiveness and styling the website.
- [Canva](https://www.canva.com/): Used for page image banners (colored overlay and opacity)
- [Google](https://www.google.com/): All images used were sourced from a Google search.
- [EmailJS](https://www.emailjs.com/): Used to link the contact form to developer's personal email account.

### Contact

- Sara_mentzer@hotmail.com
- Contact me at LinkedIn https://www.linkedin.com/in/sara-mentzer-17b9b1170/
- Contact me at GitHub https://github.com/saram88
