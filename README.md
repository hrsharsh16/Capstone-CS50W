# Capstone-CS50W
Capstone Project for CS50’s Web Programming with Python and JavaScript

In this project, I have developed a web application for a news outlet that allows users to view articles, create comments, and bookmark their favorite articles. The application is built using Django, a Python web framework, and incorporates several features to satisfy the distinctiveness and complexity requirements.

## Features

### User Authentication

- Users can register, log in, and log out.
- User-specific data, such as bookmarks and comments, are linked to their accounts.
- A secure authentication system is implemented to protect user data.

### Bookmarking System

- Users can bookmark articles for later reading.
- Bookmarks are stored in a many-to-many relationship between users and articles.
- Users can easily save and remove bookmarks from articles they find interesting.

### Article Management

- Articles are displayed in a user-friendly format.
- Markdown content is rendered into HTML for rich text formatting.
- Users can click on articles to view detailed information.

### Comment System

- Users can create comments on articles.
- Comments are displayed on article detail pages.
- Comment functionality enhances user engagement and discussion.

### Admin Panel

- An admin panel is available for site administrators.
- Administrators can manage users, articles, and comments through the admin interface.
- It provides a convenient way to moderate content and user accounts.

### Responsive Design

- The application is designed with a responsive and user-friendly interface.
- Bootstrap is used for styling, ensuring compatibility with various devices and screen sizes.

## Distinctiveness and Complexity:

- Bookmarking System: One of the key features that distinguish this project is the bookmarking system. Users can bookmark articles, and these bookmarks are stored in a many-to-many relationship between the User and Article models. This adds complexity to the project as it involves handling user interactions to save and remove bookmarks, displaying bookmarked articles on a user's dashboard, and ensuring that the bookmark state persists between sessions.

- User Authentication: The project includes a user authentication system. Users can register, log in, and log out. This feature not only adds security to the application but also provides a personalized experience for each user. User-specific data, such as bookmarks and comments, are linked to their accounts.

- Markdown Rendering: Articles are stored in Markdown format, and the application uses a library to render this Markdown into HTML for display. This feature enhances the user experience by allowing rich text formatting in articles.

- Comments System: Users can create comments on articles. This functionality is implemented with a foreign key relationship between comments and articles, and comments are displayed on article detail pages. It adds complexity in managing the relationship between articles and comments.

- Dynamic JavaScript Functionality: JavaScript is used to create dynamic behavior on the front end. For example, when a user clicks the bookmark button, JavaScript sends an asynchronous request to save or remove the bookmark without requiring a full page reload. This enhances the user experience by making the application more responsive.

## File Descriptions:

models.py: Defines the database models, including User, Article, Comment, and Bookmark, and their relationships.
views.py: Contains view functions for rendering HTML templates and handling user interactions.
urls.py: Defines URL patterns for routing user requests to the appropriate view functions.
templates/: Directory containing HTML templates for rendering web pages.
static/: Directory for storing static files like CSS and JavaScript.
article_detail.js: JavaScript code for handling bookmark functionality on the article detail page.
forms.py: Defines forms for user registration, login, and comment submission.
settings.py: Configuration settings for the Django application.

## How to Run the Application:

Install Python and Django on your system if not already installed.
Clone the project repository.
Navigate to the project directory using the command line.
Run python manage.py migrate to apply database migrations.
Create a superuser using python manage.py createsuperuser to access the admin panel.
Start the development server with python manage.py runserver.
Open a web browser and go to http://localhost:8000 to access the application.

## Additional Information:

The project is designed with a responsive and user-friendly interface using Bootstrap for styling.
User data and article content are stored securely in the database.
Extensive error handling and validation are implemented to ensure a smooth user experience.

## Conclusion:

This project stands out in terms of complexity due to its bookmarking system, user authentication, and dynamic JavaScript functionality. It provides a platform for users to interact with articles, make comments, and save their favorite content. The README aims to provide comprehensive documentation for both users and developers, making it easy to understand, run, and maintain the application.