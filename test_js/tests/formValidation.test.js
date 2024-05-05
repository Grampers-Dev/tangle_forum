// formValidation.test.js

require('text-encoding').TextEncoder;


// Import necessary modules
const { JSDOM } = require('jsdom');
const $ = require('jquery');

// Load jQuery and jQuery Validation plugins
global.$ = $;
require('jquery-validation');

// Load your HTML file containing the form
const html = fs.readFileSync('path/to/your/html/file', 'utf8');
const dom = new JSDOM(html, { runScripts: 'dangerously' });
global.document = dom.window.document;

// Your test cases
describe('Form Validation', () => {
  beforeEach(() => {
    // Reset form fields before each test
    document.getElementById('username').value = '';
    document.getElementById('email').value = '';
    document.getElementById('password1').value = '';
    document.getElementById('password2').value = '';
  });

  test('Username field validation', () => {
    // Trigger validation for username field
    $('#username').trigger('focusout');
    // Assert that error message is displayed correctly
    expect($('#username-error').text()).toBe('Please enter a username');

    // Set a valid username
    $('#username').val('testuser');
    // Trigger validation again
    $('#username').trigger('focusout');
    // Assert that error message is not displayed
    expect($('#username-error').length).toBe(0);
  });

  // Write similar test cases for other form fields
});
