# Rinse and Repeat dry cleaning

[View the live project here.](**ADD LINK LATER**)


![Program Mockup](**ADD IMAGE LATER**)

## About the Program


## Planning phase
### User Experience (UX)

#### User stories

As a [type of user], I want [an action] so that [a reason/a value]

**First Time Visitor Goals**
1. As a First Time Visitor, I want to 

#### Strategy

<details>
<summary>Project Goals</summary>

</details>

<details>
<summary>Business Goals</summary>


**Audience:** the program targets
</details>

<details>
<summary>Customer Goals</summary>

</details>

#### Scope

The scope defines which features will be implemented and which will not be implemented at this stage. 
The following features will be included in the current project's scope:

- **:** 



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

  - 1: Enter a new order
  - 2: Find order by ID
  - 3: List dropped off orders
  - 4: List ready for pickup orders
  - 5: List picked up orders
  - 0: Quit


<details>
<summary>Future features</summary>
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

6. [VS Code](https://code.visualstudio.com/)
    - VS Code is used to edit the code on Gitpod.

7. [Git](https://git-scm.com/)
    - Git was used for version control with the Gitpod terminal to commit to Git and then push to GitHub.

8. [GitHub](https://github.com/)
    - GitHub is used to get the initial project template from Code Institute's repository. Then all of the incremental progress was documented through commits pushed to this ![GitHub repository](https://github.com/adrinecl/milestone-project2), where you can also find the code and files that belong the project. After being pushed from Git, the files are updated and the ![commit history](https://github.com/adrinecl/milestone-project2/commits/master) is available here. The website was also deployed to GitHub pages for the live demo.


</details>

## Testing

### Validator Testing

#### Python
No validator testing was used for Python

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
4. Using the Terminal on Gitpod, type "python3 -m http.server".
5. A blue button will pop on the bottom right of the screen with the options to make it public, open in preview or the browser (Port 8000).

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

1. 

#### Content

- All concept and text created by the developer.

#### Media

- No media is used in this project.

### Acknowledgements

I appreaciate the availability, support, feedback and guidance of the following people throughout this project:

- My mentor [Rohit Sharma](https://github.com/rohit0286).
- My fellow colleagues for the support and encouragement on Slack.
- The Tutor support and the whole staff at Code Institute for being so helpful and readily available on Slack and in general just making the Full-Stack Software Development Program possible.