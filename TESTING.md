# Testing

## User Story Testing

All user stories have been tested. The results can be found here: [User Story Tests](USERSTORYS.md)

## Automated Testing

The Python and JavaScript code written for the project has been tested by writing automated unit tests and measuring code coverage. Since even 100% code coverage is no guarantee for bug-free code, thorough [manual tests](#manual-testing) have been conducted as well.

### Python Testing

All Python code written for the project has been tested by writing automated unit tests using [unittest](https://docs.python.org/3/library/unittest.html#module-unittest).

### JavaScript Testing

All JavaScript code written for the project has been tested by writing automated tests using [Jest](https://jestjs.io/). 98% of the JavaScript code is covered by the tests.
![Jest Results](https://res.cloudinary.com/dhx65uemx/image/upload/v1716749483/testing/t0tz48h2mjbbz18ntah8.png)

## Manual Testing

- The website was manually tested on a variety of devices (desktop, laptop, tablet, and smartphone) and browsers. The following browsers and operating systems have been tested:
  - Linux: Firefox, Google Chrome
  - macOS: Safari
  - Microsoft Windows: Microsoft Edge
  - iOS: Safari, Firefox

- The website is working as expected in all tested browsers.
- All links, buttons, and forms were thoroughly tested to make sure they work as expected.
- Friends and family members were asked to review the application and documentation to point out any bugs or user experience issues.

### W3C Validators

Both HTML and CSS pass the [W3C Markup Validator](https://validator.w3.org) and [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) with no errors:
 [W3C Markup Validator results](https://validator.w3.org/nu/?showsource=yes&showimagereport=yes&doc=https%3A%2F%2Ftangle-forum-bab6e990981f.herokuapp.com%2F)
[![W3C CSS Validator results](https://res.cloudinary.com/dhx65uemx/image/upload/v1716719100/testing/nkqhntixqqkex9zlsdo9.png)](https://jigsaw.w3.org/css-validator/)

(The W3C validator does not work with Bootstrap. Therefore, only the custom CSS code in style.css has been validated)

### PEP 8 Linter

All python code written for the project passes through the PEP 8 [python linter](https://pep8ci.herokuapp.com/) by Code Institute with no issues.

### Jshint

All JavaScript code was validated with the [Jshint linter](https://jshint.com/). All code passed with no errors.

### Chrome Lighthouse

A report on the application website generated with [Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/) showed no major issues with the performance or accessibility of the application.

![Lighthouse results summary](https://res.cloudinary.com/dhx65uemx/image/upload/v1716750247/testing/jzci0wuvctdekvv8zovb.png)

## Knowing Limitations

## Key Features

- **User Registration and Authentication**: Secure user registration and login processes to ensure the authenticity and privacy of users.
- **Thread Creation**: Users can start new discussion threads on topics of interest, fostering a community of sharing and learning.
- **Likes**: Users can like threads, which helps in surfacing popular discussions and acknowledging useful contributions.
- **Replies**: Participants can reply to threads to engage in deeper discussions, share opinions, or provide additional information.
- **Reply Updates**: Users have the flexibility to edit their replies, ensuring that the information remains accurate and relevant.
- **Reply Deletion**: Users can delete their replies, giving them control over their content and maintaining the cleanliness of the discussion.
- **Simplistic UI**: The user interface is designed to be minimalist, reducing cognitive load and enhancing focus on the content.
- **Seamless UX**: The user experience is smooth and uninterrupted, with a focus on user interactions and content discovery.

## Current Status

### Core Features Implemented

- Basic user registration and authentication

### Areas for Improvement

#### Error Handling

- Error pages are not set up.
- Future updates will include comprehensive error handling to improve user experience.

#### User Registration

- A complete setup for user password reset is not included.
- Enhanced messaging systems and feedback mechanisms need to be integrated to align with industry standards.

#### User Experience

- More user-friendly interfaces and feedback during interactions.
- Improved overall messaging to guide users through processes seamlessly.

## Future Features

- **Search Functionality**: Implement search capabilities to allow users to find threads and posts more easily.
- **Admin Moderation**: Provide tools for admins to moderate content and manage the community.
- **Implementing Custom Error Pages**: Handle various user errors gracefully.
- **Full User Password Reset Feature**: Enhance user account management.
- **Enhanced Messaging System**: Provide better feedback and notifications to users.
- **Continuous Improvements**: Align the project with industry standards and best practices.

## Conclusion

The focus on core functionalities ensures that the MVP is functional and can be demonstrated effectively. Future updates will address the current limitations and enhance the overall user experience, making the project more robust and user-friendly.
