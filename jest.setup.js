const $ = require('jquery');
const { gsap } = require('gsap');

global.$ = $;
global.jQuery = $;
global.gsap = gsap;

// Mock window.alert if necessary
jest.spyOn(window, 'alert').mockImplementation(() => {});

// Add a dummy HTML structure
document.body.innerHTML = `
  <div class="pageTitle">Test Title</div>
  <div class="big">Big Test Title</div>
`;

