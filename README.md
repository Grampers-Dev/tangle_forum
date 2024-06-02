# Tangle

![Main Logo](https://res.cloudinary.com/dhx65uemx/image/upload/v1715630230/Tangle_hokbbr.svg)

## Overview of Tangle

**Tangle** is a streamlined forum where users can engage in discussions by creating threads, replying to them, and expressing their preferences through likes. Designed with simplicity and seamless user experience in mind, Tangle offers an intuitive interface that makes online discussions both engaging and efficient.

![Responsive Mockup](https://res.cloudinary.com/dhx65uemx/image/upload/v1716649559/mockups/jpf2exnggx1fryt1p83a.png)


## Key Features

- **Thread Creation**: Users can start new discussion threads on topics of interest, fostering a community of sharing and learning.
- **Likes**: Users can like threads, which helps in surfacing popular discussions and acknowledging useful contributions.
- **Replies**: Participants can reply to threads to engage in deeper discussions, share opinions, or provide additional information.
- **Reply Updates**: Users have the flexibility to edit their replies, ensuring that the information remains accurate and relevant.
- **Reply Deletion**: Users can delete their replies, giving them control over their content and maintaining the cleanliness of the discussion.
- **Simplistic UI**: The user interface is designed to be minimalist, reducing cognitive load and enhancing focus on the content.
- **Seamless UX**: The user experience is smooth and uninterrupted, with a focus on user interactions and content discovery.

## Features

- User registration and authentication
- Create, read, update, and delete forum posts
- Comment on forum posts
- User profiles with activity history
- Like Threads

## Future Features

- Search Functionallity
- Admin moderation


# Design Process

## Strategy Plane for Django Agile Development Project

### Project Vision and Objectives

**Vision Statement Summary:**
The vision for Tangle is to develop a robust Django-based online forum that fosters meaningful discussions and connections among users. It aims to create a vibrant community space where individuals can engage in conversations on various topics of interest, promoting interaction, learning, and camaraderie.

**Project Objectives:**
1. **Seamless User Experience:** Tangle aims to provide a user-friendly platform with an intuitive interface, making it easy for users to navigate, interact, and contribute to discussions.
2. **Community Engagement:** The project seeks to enhance user engagement by offering interactive features such as forums, live chats, and responsive feedback mechanisms, fostering a sense of community.
3. **Security and Compliance:** Tangle prioritizes the security and privacy of user data, implementing state-of-the-art security measures to protect user information and ensure compliance with relevant regulations.
4. **Scalability and Maintainability:** The platform is designed to be scalable and maintainable, capable of supporting a growing community and accommodating future expansions easily.
5. **Continuous Improvement:** Post-launch, Tangle will undergo continuous updates and feature enhancements to remain relevant and improve user satisfaction over time.

**Primary Objective**
Deliver a fully functional, secure, and user-friendly web platform that allows for efficient management and interaction within the Django framework.

**Secondary Objectives**
1. Ensure the application is scalable and maintainable.
2. Implement state-of-the-art security measures to protect user data and ensure compliance with relevant regulations.

### Target Audience and Stakeholder Engagement

**Primary Users**
This application targets users who need a reliable and intuitive platform to interact with content dynamically, such as small business teams, educational groups, or community forums.

**Secondary Users**
Administrators and staff who require backend access to manage user interactions, content, and system settings efficiently.

**Stakeholder Engagement**
Regular updates and feedback sessions will be scheduled with potential end-users and stakeholders to ensure the platform meets their needs and to refine the product roadmap based on their input.

### User Experience Goals

**User-Centric Design**
The platform will be designed with a focus on user experience, aiming to provide a seamless and intuitive interface that facilitates easy navigation and minimal learning curve.

**Engagement and Interaction**
Enhance user engagement through interactive features like forums, live chats, and responsive feedback mechanisms.

**Accessibility**
Ensure that the application is accessible to users with disabilities, adhering to ADA (Americans with Disabilities Act) standards.

### Market Position and Competitive Advantage

**Unique Selling Proposition (USP)**
The application will offer unique features such as advanced reply management systems and integrated user analytics, which set it apart from competitors.

**Competitive Analysis**
Conduct a thorough analysis of competing products to identify gaps in the market that the Django application can fill, ensuring it offers distinct advantages over existing solutions.

### Technology and Development Framework

**Technology Stack**
- Django
- HTML/JavaScript/CSS (Frontend)
- PostgreSQL

**Development Practices**
Adopt Agile methodologies with structured sprints for continuous development and iteration based on user feedback and testing outcomes.

**Testing and Quality Assurance**
Implement comprehensive testing strategies including unit tests, integration tests, and user acceptance testing to ensure high-quality releases.

### Risk Management and Mitigation Strategies

**Risk Identification**
Regularly identify potential risks such as scope creep, technical challenges, or delays in development timelines.

**Mitigation Plans**
Develop contingency plans for significant risks, including additional resource allocation, schedule adjustments, and ongoing technical reviews to address potential issues proactively.

### Sustainability and Future Growth

**Scalability**
Design the application architecture to be scalable to handle increased load and to accommodate future expansions easily.

**Continuous Improvement**
Plan for ongoing updates and feature enhancements post-launch to keep the application relevant and to improve user satisfaction continuously.

## Conclusion

This Strategy Plane sets a solid foundation for my Django Agile Development project, ensuring that every aspect—from user experience to technology selection—is aligned with the overarching project goals. By maintaining a clear focus on the needs of both users and stakeholders, and by employing robust development and testing practices, this plan aims to guide the project towards a successful completion and sustainable future growth.

---

## Scope Plane: User Stories Within Project Scope

ℹ️ The following user stories were included in the current scope of the project.

### User Story #1: Authentication

**Epic:** Security  
**Priority:** Must-Have  
**Size:** M (3 story points)  
**GitHub Label:** Security, Backend, Must-Have  
**Acceptance Criteria:**
- Users can register using an email and password.
- Users can log in using their email and password.
- Passwords are stored securely.
- Users receive error feedback on failed login attempts.

**Tasks:**
- Set up Django’s authentication framework.
- Develop registration and login forms.
- Implement secure password storage using Django’s built-in hashing.
- Create unit tests for authentication functionalities.

### User Story #2: Reply Management

**Epic:** Content Interaction  
**Priority:** Must-Have  
**Size:** L (5 story points)  
**GitHub Label:** User Engagement, Backend, Must-Have  
**Acceptance Criteria:**
- Users can post replies to threads.
- Users can edit and delete their own replies.
- Reply edits are logged with timestamps.
- Only authenticated users can post replies.

**Tasks:**
- Create models and APIs for replying to posts.
- Develop front-end components for managing replies.
- Ensure user authentication checks are in place for posting replies.
- Set up backend logging for tracking edits and deletions.

### User Story #3: User Experience and User Interface

**Epic:** UI/UX  
**Priority:** Should-Have  
**Size:** S (2 story points)  
**GitHub Label:** UX/UI, Frontend, Should-Have  
**Acceptance Criteria:**
- The interface is intuitive and easy to navigate.
- The website is responsive on mobile, tablet, and desktop devices.
- Accessibility standards are met to ensure inclusivity.

**Tasks:**
- Design a responsive UI using CSS frameworks like Bootstrap.
- Implement navigation improvements based on user feedback.
- Conduct accessibility audits and make necessary adjustments.

### User Story #4: Content Management

**Epic:** Content Management  
**Priority:** Must-Have  
**Size:** M (3 story points)  
**GitHub Label:** Content, Backend, Must-Have  
**Acceptance Criteria:**
- Users can create, view, edit, and delete posts.
- Posts display the timestamp and the author’s username.
- Admin tools are available for content moderation.

**Tasks:**
- Develop CRUD operations for forum posts.
- Integrate user authentication to verify permissions for post interactions.
- Set up admin tools for content moderation.

### User Story #5: Security And Compliance

**Epic:** Compliance  
**Priority:** Should-Have  
**Size:** M (3 story points)  
**GitHub Label:** Security, Compliance, Should-Have  
**Acceptance Criteria:**
- The application complies with GDPR and other relevant privacy regulations.
- User data is encrypted at rest and in transit.
- Regular security audits are conducted to ensure compliance.

**Tasks:**
- Implement encryption methods for data security.
- Develop and integrate compliance checks within the application.
- Schedule and execute regular security audits.

ℹ️ User stories marked with the MVP label make up the Minimum Viable Product.

---

## Structure Plane

### Database Schema Overview

The database schema supports a Django application with user profiles, discussion threads, and interaction tracking. It ensures data integrity and efficient data retrieval through relational structures.

#### Users Table
- **id** (int, pk): Unique identifier for each user.
- **username** (string): User's chosen name.
- **email** (string): User's email address for contact and recovery.
- **password** (string): Hashed password for secure authentication.

#### Profiles Table
- **id** (int, pk): Primary key.
- **user_id** (int, fk): Links to the Users table.
- **likes** (int): Number of likes the profile has received.

#### Threads Table
- **id** (int, pk): Primary key.
- **title** (string): Title of the thread.
- **description** (string): Detailed thread content.
- **date_created** (datetime): Record of thread creation time.

#### Threads_Liked_By Table
- **thread_id** (int, fk): Reference to Threads table.
- **user_id** (int, fk): Reference to Users table.

#### Threads_Disliked_By Table
- **thread_id** (int, fk): Reference to Threads table.
- **user_id** (int, fk): Reference to Users table.

#### Replies Table
- **id** (int, pk): Primary key.
- **thread_id** (int, fk): Linked to the thread discussed.
- **user_id** (int, fk): Author of the reply.
- **message** (string): Content of the reply.
- **date_created** (datetime): Timestamp of initial creation.
- **updated** (datetime): Timestamp of last update.

**Relationships:**

- One-to-One: Users to Profiles - Each user has one profile.
- Many-to-Many: Users to Threads via Threads_Liked_By and Threads_Disliked_By - Users can like or dislike threads.
- One-to-Many: Threads to Replies - Each thread can have multiple replies.

 # Entity-Relationship Diagram

![ERD](https://res.cloudinary.com/dhx65uemx/image/upload/v1716642448/ERD/hvjul6xur93mr4noelbz.svg)

## Skeleton Plane

The overall layout of the website stays close to tried and tested forums, I wanted to modernize the look with a fresh edgey look

The website consists of three main sections: A header with the logo, the main title, and the navigation menu, a main section for the content, and a footer.

The website is designed to be responsive for all screen sizes.

The wireframes for the project can be found here:

![Login](https://res.cloudinary.com/dhx65uemx/image/upload/v1717323969/mockups/wireframes/tgmetewlz569smfgt5tp.png)
![Register](https://res.cloudinary.com/dhx65uemx/image/upload/v1717323972/mockups/wireframes/d3ug5cjheu56bo4hqri6.png)
![Profile](https://res.cloudinary.com/dhx65uemx/image/upload/v1717323975/mockups/wireframes/kelipd7yschsqhz0z1b1.png)
![Home](https://res.cloudinary.com/dhx65uemx/image/upload/v1717323973/mockups/wireframes/jlvcusdlu0uuddiggmgq.png)
![Thread](https://res.cloudinary.com/dhx65uemx/image/upload/v1717323970/mockups/wireframes/y2v0iiiz0xbbpymeaj8l.png)

## Surface Plane

Similar to the general layout, the goal of the visual design of the website was to stay close to the design of original forums, while updating and modernizing design elements where appropriate.

#### Colors

The project uses a fresh modern color scheme, the inspiration comes from various web3 related projects.

The color scheme consists of two main colors and one tertiary color:

<!-- Display colors in markdown: https://stackoverflow.com/a/41247934 -->
![#ff0000](https://placehold.co/100x100/ff0000/ff0000.png) Primary color: #ff0000

![#0000ff](https://placehold.co/100x100/0000ff/0000ff.png) Secondary color: #0000ff

![#33b770](https://placehold.co/100x100/33b770/33b770.png) Tertiary color: #33b770

### Agile Methodolgy

#### Sprint Setup

Each sprint spans one week, aligning perfectly with my three-week project timeline. The sizing of each user story will guide task complexity and expected effort.

- **Sprint 1:** May 4 - May 10, 2024
- **Sprint 2:** May 11 - May 17, 2024
- **Sprint 3:** May 18 - May 24, 2024

#### User Stories and Sizing

**Week 1: Sprint 1 - Core Functionalities**
- Objectives: Establish the foundational elements of the Django application, focusing on authentication and content management due to their critical importance.
- **User Stories to Complete:** User Story #1: Authentication, User Story #4: Content Management

**Week 2: Sprint 2 - Advanced Interactions and Security**
- Objectives: Develop advanced user interactions for reply management and implement robust security measures to protect user data.
- **User Stories to Complete:** User Story #2: Reply Management, User Story #5: Security And Compliance

**Week 3: Sprint 3 - Finalization and User Experience**
- Objectives: Polish the user interface and finalize the application for deployment, ensuring it delivers a seamless user experience.
- **User Stories to Complete:** User Story #3: User Experience and User Interface

#### GitHub Integration and Management

- **GitHub Issues:** Each task and bug tracked as individual issues.
- **GitHub Projects:** Utilize the Kanban board to manage tasks visually across columns (To Do, In Progress, Review, Done).
- **Milestones:** Link sprints to GitHub milestones to ensure timely delivery.
- **Labels:** Apply size labels (XS, S, M, L, XL) and priority labels to each issue.

---

## Conclusion

This structured approach not only allows me to manage my workload efficiently as a solo developer but also helps in maintaining a high level of organization and focus. Using GitHub effectively for issue tracking, project management, and documentation ensures that every aspect of the project is under control, aligning perfectly with my ambitious three-week timeline.

# Technologies Used

## Frameworks and Languages

- **Django:** The website has been built with Django, a Python web framework.
- **HTML, CSS, and JavaScript:** Used for implementing the website's front end.
- **Bootstrap:** Used for the visual design and layout of the front end.

## Additional Python Packages

The following Python packages are required for this project:

- **asgiref==3.8.1**: ASGI specs, helper utilities, and reference implementations.
- **certifi==2024.2.2**: Python package for providing Mozilla's CA Bundle.
- **charset-normalizer==3.3.2**: The Real First Universal Charset Detector.
- **cloudinary==1.40.0**: Cloudinary is a cloud service that offers a solution to a web application's entire image management pipeline.
- **dj-database-url==2.1.0**: Django database management.
- **Django==5.0.4**: The web framework for perfectionists with deadlines.
- **django-cloudinary-storage==0.3.0**: Using Cloudinary as Django file storage.
- **django-environ==0.11.2**: Django-environ allows you to utilize 12factor inspired environment variables to configure your Django application.
- **gunicorn==20.1.0**: WSGI server used for deployment.
- **idna==3.7**: Internationalized Domain Names in Applications (IDNA).
- **psycopg2==2.9.9**: PostgreSQL database adapter for the Python programming language.
- **python-dotenv==1.0.1**: Reads key-value pairs from a .env file and can set them as environment variables.
- **requests==2.31.0**: A simple, yet elegant, HTTP library.
- **six==1.16.0**: Python 2 and 3 compatibility utilities.
- **sqlparse==0.5.0**: A non-validating SQL parser for Python.
- **typing_extensions==4.11.0**: Backported and Experimental Type Hints for Python.
- **tzdata==2024.1**: IANA time zone database (tzdata).
- **urllib3==2.2.1**: A powerful, user-friendly HTTP client for Python.
- **whitenoise==6.6.0**: Serve static files directly from your application.
- **django-allauth==0.52.0**: Advanced authentication and user management for Django.
- **coverage==7.2.1**: Analyzing test coverage.

## Other Software

- **GitHub:** Used to store all project files in the repository. GitHub Issues have been used for Agile methodology by assigning user stories to issues and using labels to organize user stories. GitHub Projects have been used for Agile sprint planning and task tracking.
- **Git:** Used for version control by committing changes to Git and pushing them to GitHub from the command line.
- **Heroku:** Used to deploy the website.
- **ElephantSQL:** Used for the project's PostgreSQL database.
- **Cloudinary:** Used to store media files.
- **Balsamiq:** Used to create wireframes during the design process.
- **Mermaidv10.9.0 Live Editor:** Used to create entity relationship diagrams (ERD) for modeling the project database.
- **Google Fonts:** Used to import the font 'Unbounded'.
- **LightHouse:** Used to assess the website's performance.
- **WAVE:** Used to further evaluate the website's accessibility.
- **VS Code:** Used for writing code.

## Testing

[Testing documentation can be found here](TESTING.md)

## Deployment

The project was deployed to [Heroku](https://heroku.com). The live version of the project can be found at https://tangle-forum-bab6e990981f.herokuapp.com/

The necessary steps to deploy the project are:
  - Clone or fork the repository.
  - Create an account at https://cloudinary.com and get your Cloudinary URL from the dashboard.
  - Create a PostgreSQL database, for example at https://www.elephantsql.com/, and find the database address.
  - Create a new app from the [Heroku dashboard](https://dashboard.heroku.com).
  - Go to the Settings tab and click on `Reveal Config Vars` in the *Config Vars* section.
  - Now add the following config vars:
    |Name|Value|
    |---|---|
    |CLOUDINARY_URL|\<Your cloudinary url\>|
    |DATABASE_URL|\<Your database url\>|
    |DEFAULT_FROM_EMAIL|\<your email address\>|
    |DEVELOPMENT|FALSE|
    [EMAIL_HOST_PASSWORD|\<your email password\>|
    |EMAIL_HOST_USER|\<your email address\>|
    |PORT|8000|
    |SECRET_KEY|\<some random string\>|

  - Add `Python` to the *Buildpacks* section.
  - Click on the *Deploy* tab and connect the Heroku app to your GitHub repository.
  - Choose the branch you want to deploy in the *Manual deploy* section and click on **Deploy Branch**.

## Credits

The following resources were used for the project:

### Code

I made extensive use of the Django documentation avilable at: https://docs.djangoproject.com/en/stable/. 

The inital setup and the basic structure of the project followed the instructions from the Code Institute Django Blog walkthrough project.

All other used sources are listed here (all code from these sources has been thoroughly reviewd, understood and adapted to the best of my abillity for my project):
// References:
- [Django Models Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Cloudinary Django Integration](https://cloudinary.com/documentation/django_integration)
- [Django ManyToManyField](https://docs.djangoproject.com/en/stable/ref/models/fields/#django.db.models.ManyToManyField)
- [Django Model Methods](https://docs.djangoproject.com/en/stable/topics/db/models/#model-methods)
- [Django ContentTypes Framework](https://docs.djangoproject.com/en/stable/ref/contrib/contenttypes/)
- [Submit Forms with jQuery AJAX](https://stackabuse.com/submit-forms-with-jquery-ajax/)
- [How to Submit Form via Ajax using jQuery](https://www.codexworld.com/submit-form-via-ajax-using-jquery/)
- [Typing Effect Using JavaScript](https://www.w3schools.com/howto/howto_js_typewriter.asp)
- [How to Create an Animated Gradient Background](https://css-tricks.com/creating-an-animated-gradient-background/)
- [Debounce Function in JavaScript](https://davidwalsh.name/javascript-debounce-function)
- [MutationObserver API](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver)
- [GSAP Animation Library](https://greensock.com/gsap/)
- [jQuery toggle() Method](https://www.w3schools.com/jquery/eff_toggle.asp)