# Rinse and Repeat Dry Cleaning

[View the live project here.](https://rinse-and-repeat.herokuapp.com/)


![Program](https://github.com/adrinecl/milestone-project3/blob/master/docs/images/rinse-and-repeat_start.jpg)

## About the Program

"Rinse and Repeat" is a command-line interface program for a fictional dry cleaning company. It is intended for the small, newly started dry cleaning company lacking the resources to spend on an expensive order management system. 

The program can be accessed by a link on the browser, running a mockup terminal.
It is possible to enter new orders, see an individual order in detail, consult the status of the orders and see all order history. It is also possible to change the status from "dropped off" to "ready for pickup" and later to "picked up" when the customer gets their order. Finally, it is possible to quit the program.

## Planning phase
### User Experience (UX)

#### User stories

As a [type of user], I want [an action] so that [a reason/a value].

**User Goals**
1. As a User, I want to have a smart, inexpensive and efficient solution to manage orders in my dry cleaning business. 
2. I want to be able to enter new orders, as clients come into the store with items dropped off for dry cleaning.
3. I want to be able to enter how many and the type of items that are being dropped off.
4. I want to be able to consult orders in details, so I know which orders still need to be done and I can mark them as ready to avoid mixing them up.
5. I want to identify the orders with unique numbers, so I can quickly find my client's clothes when they are picking up at the store.
6. I want to mark orders as "picked up" when the customer gets their order.

The ideal user is the owner / manager, dry cleaner and store assistent at a dry cleaning company, attending customers and managing orders on a daily basis. Since in a small store all of these functions can be performed by the same person, only one type of user is considered above for these user stories, but it is possible that users with different roles can all benefit from different functions of this order management system. As a general example:
- A business owner / manager can consult the order history and check the general status of all orders, the total amounts and so on to better plan for the business.
- A dry cleaner can see which orders are still left to be worked on.
- A store assistant can easily enter new orders and change order status as customers come into the store.

In future features, it would be good to do further research on the needs of different roles in different dry cleaning companies of varied sizes.

#### Strategy

<details>
<summary>Project Goals</summary>
The purpose of this project is to build a command-line interface program, using Python. The program should have some basic, but essential features to bring value to a small dry cleaning business. The user should feel confident to quickly learn how to use the program and be shown at each step what other options are possible.
Although it is a simple program, it is an efficient alternative to expensive order management systems. In this project, the main goal is to make sure that the user can quickly figure out how to operate it and center all business activities in one place and organized fashion.
</details>

<details>
<summary>Business Goals</summary>
The main goal of the program is to offer a an alternative to expensive order management systems for dry cleaning stores. This is the first ever version of the program for "Rinse and Repeat" and it runs on the browser through Heroku deployment. The program is free and this is a good way to test for features before potentially developing it further or even creating a paid version. Developing and deploying a program in this manner can save time, by just "shipping it" with the MVP (minimun viable product) and later iterating and improving it little by little.

**Audience:** the program targets mainly business owners and managers of small dry cleaning stores looking for efficient and inexpensive order management solutions. Basic knowledge of English is needed.
</details>

<details>
<summary>Customer Goals</summary>
Users: quickly learn to operate and access order information to keep all business activities organized. One main goal is for the user to have one main source of truth for adding and handling customer's orders, while making it easier to manage and plan for the business as whole.
</details>

#### Scope

The scope defines which features will be implemented and which will not be implemented at this stage. 
The following features will be included in the current project's scope:

- **1: Enter a new order:** Allows the user to create a new order. All new orders are automatically marked as "dropped off".
- **2: Find order by ID:** Allows the user to consult one individual order in detail. Here the user can change the order status to "ready for pickup" or to "picked up", depending on the current applicable situation.
- **3: List dropped off orders:** This option lists all orders that have been dropped off by customers and still need to be dry cleaned / washed.
- **4: List ready for pickup orders:** This option lists all orders that are cleaned and ready for customers to pickup.
- **5: List picked up orders:** This option lists all finalized orders that have already been cleaned and picked up by customers.
- **6: List all orders:** This option allows the user to view the order history.
- **0: Quit:** This option quits the program.


#### Structure

- The program runs on the browser thanks to Heroku deployment and some presettings. The structure is based on a menu selection style for viewing and editing order, as well as further option within each main category.
- For safety reasons, it is not possible to delete an order from the menu, since it can be easy to select an option by mistake. This is also important for the eventual bookkeeping of the orders.


#### Skeleton

- The focus of this project is to create a command-line interface program. Therefore wireframes are not relevant concerns at the moment. The information will be presented in a mock terminal with a menu selection style for viewing and editing orders.


#### Surface
##### Design

- The focus of this project is to create a command-line interface program. Therefore design elements and planning related to color scheme, typography, imagery and so on are not relevant concerns at the moment.


## Implementation phase
### Features 
### Existing Features

- __Main Menu section__
The main menu offers the main operations the user directly needs access to.
The options are ordered by relevance and the need to provide fast service to the customer. Therefore, creating an order is the first item.

When the program starts, a welcome message is displayed "Welcome to Rinse and Repeat Dry Cleaning" and the user is prompted to select an option "Enter menu commands (1 through 6) from the list below using the keyboard."
"Press return to perform the command. To exit the program, enter 0 or Q."

- __1: Enter a new order__
Allows the user to create a new order. The user sees the individual prices in Euros for dry cleaning each item and is expected to enter the quantity. If an item has quantity 0, the user can simply press "Enter" to skip it. All orders numbers are generated automatically by increments of 1, starting at 1, which is the first order number manually entered in the spreadsheet. All new orders are automatically marked as "dropped off" and the "dropped off date" is also set then.

The new order line is then created and further options are given for that order just created.
    - 1: Mark as ready for pickup: changes the status of the order to "ready for pickup", sets the date of "ready for pickup".
    - 2: Mark as picked up: changes the status of the order to "picked up", sets the date of "picked up".
    - 3: View customer contact information: shows the customer name, email and phone number, so that the store can contact the customer when an order is ready to be picked up.
    - 0: Back

- __2: Find order by ID__
Allows the user to consult one individual order in detail. Here the user can change the order status to "ready for pickup" or to "picked up", depending on the current applicable situation.

The order line is then displayed and further options are given for the order comsulted.
    - 1: Mark as ready for pickup: changes the status of the order to "ready for pickup", sets the date of "ready for pickup".
    - 2: Mark as picked up: changes the status of the order to "picked up", sets the date of "picked up".
    - 3: View customer contact information: shows the customer name, email and phone number, so that the store can contact the customer when an order is ready to be picked up.
    - 0: Back

- __3: List dropped off orders__
This option lists all orders that have been dropped off by customers and still need to be dry cleaned / washed.
All the main menu options appear below the list.

- __4: List ready for pickup orders__
This option lists all orders that are cleaned and ready for customers to pickup.
All the main menu options appear below the list.

- __5: List picked up orders__
This option lists all finalized orders that have already been cleaned and picked up by customers.
All the main menu options appear below the list.

- __6: List all orders:__
This option allows the user to view the order history.
All the main menu options appear below the list.

- __0: Quit:__
This option exits the program when the user selects 0, q or Q. The program then shows the message "Goodbye, have a fantastic day!"


<details>
<summary>Future features</summary>
- The possibility to have a better customer database, by reusing the customer contact information for new orders, instead of creating of asking for the customer's name, email and phone number every single time.
- The possibility to mark individual items as "ready for pickup" and later "picked up". This allows the customer to pickup items that are ready first in case they are in a rush.
- The possibility to (in a safe way) delete to cancel orders and generate "refunds".
- The possibility to mark an order as paid, partially paid or to be paid on pickup.
- The possibility to offer other services such as shoe repair, smaller sewing adjustments and repairs as well as price calculation based on dimensions or material, which is important for some items like curtains and carpets.
- The possibility to email/SMS customers with a confirmation email when their order has been dropped off, paid and then when their order is marked as ready to be picked up.
- The possibility to see business statistics.
- The possibility to log changes.
- Future features could include a website and front-end layout connected to a database instead of Google Drive and Google Sheets.
- More functionalities could be added for creating and editing an order.
- It could be possible for the customer to login to the website to check the status of their orders, when they are ready to be picked up, if they are already paid and their general order history.
</details>

## Responsiveness

- Responsiveness on different devices and screens sizes is dependable on the presettings used to deploy the program to Heroku. Unfortunately, it might be not such a great experience running it in smaller screens and touchscreens.

## Technologies Used

### Languages Used
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

<details>
<summary>Frameworks, Libraries & Programs Used</summary>

1. [Gitpod](https://www.gitpod.io/) 
    - Gitpod was used for the development of the website, by running Visual Studio Code (VS Code) to edit code, commiting to Git and pushing to GitHub.

2. [VS Code](https://code.visualstudio.com/)
    - VS Code is used to edit the code on Gitpod.

3. [Git](https://git-scm.com/)
    - Git was used for version control with the Gitpod terminal to commit to Git and then push to GitHub.

4. [GitHub](https://github.com/)
    - GitHub is used to get the initial project template from Code Institute's repository. Then all of the incremental progress was documented through commits pushed to this ![GitHub repository](https://github.com/adrinecl/milestone-project2), where you can also find the code and files that belong the project. After being pushed from Git, the files are updated and the ![commit history](https://github.com/adrinecl/milestone-project2/commits/master) is available here. The website was also deployed to GitHub pages for the live demo.

5. [Google Cloud Platform](https://cloud.google.com/)
    - Google Cloud Platform was used to wipe up the Google Drive and Google Sheets APIs to the project.

6. [Google Sheets](https://www.google.com/sheets/about/)
    - Google Sheets was used for the spreadsheet to store and access data used in the program.

7. [Google Drive](https://www.google.com/drive/)
    - Google Drive is used indirectly, since this is where the Google Sheets spreadsheet is stored.

8. [GSpread API Reference](https://docs.gspread.org/en/latest/api.html)
    - The API reference for the GSpread library for Python. It provides an easy interface for working with Google Sheets from code.


</details>

## Testing

### Validator Testing

#### Python
[PEP8 Online - Python Validator](http://pep8online.com/)

### Test Cases

[Test cases (user story based with screenshots)](https://github.com/adrinecl/milestone-project3/blob/master/docs/TESTING.md)

### Fixed Bugs

Throughout the project some bugs were fixed:

[Fixed bugs](https://github.com/adrinecl/milestone-project3/blob/master/docs/TESTING.md)

### Unfixed Bugs

- 

### Supported Screens and Browsers

- The program is a command-line interface deployed to Heroku, in order to make it possible for viewing the project in a mock terminal, so it can be accessed from the browser. There are no website layout changes to best fit on the screen it is displayed on. With deployment to Heroku, the program can run on all screen sizes from large desktops to small phones. 

## Deployment

### Gitpod

The project was deployed to Gitpod.

These are the steps to deploy to GitHub Pages:

1. Log in to GitHub and locate the GitHub Repository one wishes to deploy with Gitpod.
2. At the top right of the Repository (not top of page), locate the "Gitpod" button.
3. This will create a workspace on Gitpod for this project.
4. Using the Terminal on Gitpod, type "python3 run.py".
5. The program will then run in the terminal.

### Heroku

The project was deployed to Heroku.

These are the steps to deploy to Heroku:

1. Log onto Heroku and click the "Create new app" button.
2. Enter a unique name for your application.
3. Select the region closest to you.
4. Go to settings, then click on reveal config vars.
5. Enter your key value pairs in "Config Vars" as needed. For this project, the information from creds.json listed in the .gitignore file is added here.
6. Add "Buildpacks" if needed. For this project, Python and Node.js were selected in this order.
7. Set your deployment method to "GitHub" and click "Connect to Github".
8. Search for the repository you wish to deploy from and click "Connect".
9. Enable automatic deploy or choose to deploy manually as you prefer.


## Credits

### Code

All code written by the developer, Adrine Curcio Lindström.

### Resources

Main sources used for consultation and troubleshooting:

1. [Python Developer's Guide](https://devguide.python.org/)
2. [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/?#code-lay-out)
3. [Python Tutor](http://pythontutor.com/)

#### Content

- All concept and text created by the developer.

#### Media

- No media is used in this project.

### Acknowledgements

I appreaciate the availability, support, feedback and guidance of the following people throughout this project:

- My mentor [Rohit Sharma](https://github.com/rohit0286).
- My fellow colleagues for the support and encouragement on Slack.
- The Tutor support and the whole staff at Code Institute for being so helpful and readily available on Slack and in general just making the Full-Stack Software Development Program possible.