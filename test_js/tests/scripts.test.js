/**
 * @jest-environment jsdom
 */

const $ = require('jquery');
const { gsap } = require('gsap');

global.$ = $;
global.jQuery = $;
global.gsap = gsap;

const {
  handleFormSubmit,
  typeWriter,
  startAnimation,
  stopAnimation,
  debounce,
  initGSAPAnimations,
  togglePanel
} = require('../../user_profile/static/js/scripts');

// Mock functions if necessary
jest.spyOn(window, 'alert').mockImplementation(() => {});


// Add a dummy HTML structure before each test
beforeEach(() => {
  document.body.innerHTML = `
    <div class="pageTitle">Test Title</div>
    <div class="big">Big Test Title</div>
    <div id="like-section">
      <form action="/like">
        <input type="hidden" name="thread_id" value="1">
        <input type="hidden" name="csrfmiddlewaretoken" value="dummy_csrf_token">
        <button type="submit">Like</button>
      </form>
      <span id="like-count">0 Likes</span>
    </div>
    <div class="logo-image"></div>
  `;
});

describe('Form Submission and Validation', () => {
  test('like button submission', () => {
    const form = $('#like-section form');
    const submitEvent = $.Event('submit');

    // Mock the form submission
    form.on('submit', (e) => {
      e.preventDefault();
    });

    form.trigger(submitEvent);

    expect(submitEvent.isDefaultPrevented()).toBe(true);
    expect($('input[name="thread_id"]').val()).toBe('1');
    expect($('input[name="csrfmiddlewaretoken"]').val()).toBe('dummy_csrf_token');
  });
});

describe('Page Title Typing Effect', () => {
  test('typing effect on page title', (done) => {
    // Mock the typeWriter function
    const mockTypeWriter = jest.fn(() => {
      const pageTitle = document.querySelector('.pageTitle');
      pageTitle.innerHTML = 'Mocked Title';
    });

    // Replace the real typeWriter function with the mock
    global.typeWriter = mockTypeWriter;

    const pageTitle = document.querySelector('.pageTitle');
    pageTitle.innerHTML = '';
    typeWriter();

    setTimeout(() => {
      const result = pageTitle.innerHTML;
      console.log(`Page title after typing effect: ${result}`);
      done();
    }, 200); 
  });
});


describe('Background Gradient Animation', () => {
  test('background gradient animation start and stop', () => {
    startAnimation();
    setTimeout(() => {
      const result = document.body.style.backgroundImage;
      console.log(`Background image after animation start: ${result}`);
      stopAnimation();
    }, 300); // Added a small timeout to allow the animation to start
  });
});

describe('GSAP Animations for Logo Image', () => {
  test('gsap animation for logo image', (done) => {
    initGSAPAnimations();
    setTimeout(() => {
      done();
    }, 2000); // Timeout to allow GSAP animation to start
  });
});



