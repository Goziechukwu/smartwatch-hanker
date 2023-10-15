# Smartwatch Hanker

Smartwatch Hanker is an inventory management eCommerce platform designed with Python language, which runs in the Code Institute mock terminal on Heroku.

## Using Smartwatch Hanker

Upon visiting Smartwatch Hanker's platform, the user will be greeted with a welcoming message, and first of all asked if .

<img src="./assets/images/responsiveness-screenshot.png" alt="Responsiveness screenshot">
 
Source: [Responsivity measurement](https://ui.dev/amiresponsive?url=https://goziechukwu.github.io/decor-awesome/)

## Features

### • Navigation Bar

The navigation bar is displayed on all three pages of the website, including links to the Logo, Home page, Gallery and Sign Up.

The navigation bar is fully responsive to all device-size types, from desktops, to laptops, tablets, handsets.

<img src="./assets/images/navigation-highlight-image.PNG" alt="Navigation highlight image">

### • The landing page image

<img src="./assets/images/landing-page-image-screenshot.png" alt="Landing page image">

[Source of Landing Page Image](https://unsplash.com/photos/0jmXOqUhpTQ)


### • Enhanced Mood Section

o Showing the benefits of using our decoration hacks.

o Highlighting the benefits as relevant for student-life experience.

<img src="./assets/images/enhanced-mood-section-screenshot.png" alt="enhanced-mood-section-screenshot">

### • Services Section

o Showing the advancing range of services provided to meet the specific change-of-state(mood) need of a student, at any relevant period of his semester and also at holidays.

o Showing how Decor Awesome provides both simple and advanced room decoration techniques for different expected enhancements of moods and states

<img src="./assets/images/services-section-screenshot.png" alt="Services section screenshot">

### • The Footer

o The footer contains links to relevant social media sites.

<img src="./assets/images/footer-image-screenshot.png" alt="Footer image screenshot">

### • Gallery

<img src="./assets/images/gallery-images-screenshot.png" alt="Gallery images screenshot">

### • The Sign Up Page

<img src="./assets/images/sign-up-page-screenshot-1.png" alt="Sign Up page first screenshot">

<img src="./assets/images/sign-up-page-screenshot-2.png" alt="Sign Up page second screenshot">

## Technologies Used:

• The following programming languages were used:

- HTML5

- CSS3

• The workspace used to write the code was:

- Codeanywhere workspace

• All codes and commits were pushed to:

- GitHub repository

• The library in google that was used for the fonts is:

- Font Awesome

• The styling layout (framework) used for the gallery section was:

- Masonry layout

The website looks the same when opened on different kinds of browsers. I have observed that the website's user interface looks the same on the Google Chrome, the Mozilla Firefox and the Microsoft browsers.

## Validation Testing

The HTML and CSS codes have been tested for validation in the w3C HTML Validator and the w3C (Jigsaw) CSS Validator respectively, and no errors were returned.

<img src="./assets/images/validation-testing-screenshot-1.png" alt="First Validation Testing">


<img src="./assets/images/validation-testing-screenshot-2.png" alt="Second Validation Testing">


## Accessibility Requirements

Decor Awesome has been tested using Lighthouse on Google and found to completely meet Accessibility Requirements, in addition to having Best Practices, and more, as indicated in the screenshot below:

<img src="./assets/images/accessibility-requirements-score-screenshot.png" alt="Accessibility Requirements Score">

## Bugs, and How I Fixed Them

I had a challenge with my social media icons. The code syntax I used made my icons within the footer to be clickable beyond the perimeter of each icon. I solved this by copying out the class names from the scripts of the downloaded social media icon tags and putting the class names in the anchor element tags, thus giving the anchor elements the class of the icon elements and taking out the icon tags from the code.

This worked, but then the icons changed to their default blue colors, and I wanted them to be black colour in the website, I then had to create a new css rule for the icons, having the class names “fa-brands” and setting a color property of black. This gave me what I desired, the black-colored icons.

## File Structure

Folders and Files in the workspace are created as follows:

Folders: - Assets folder

Contents: - CSS folder and Images folder

Files: - index.html, gallery.html, signup.html and style.css files (in the CSS folder)

Other files are photo files in the images folder, like the hero-image, mood-center-image, services-background image, signup-background-image, and others in the gallery.

## Deployment

The site was deployed to GitHub pages by the following steps:
Navigating in the GitHub repository to the Settings tab,
Clicking the drop-down menu under the source section and selecting 'Master Branch', and finally waiting for the page to refresh and display a detailed ribbon sign indicating that deployment was successful.

This brought forth, under the Pages section under Settings, Decor Awesome's live link which is as follows:

https://goziechukwu.github.io/decor-awesome/


## Contact information

The website developer's contact details are as follows:

Email: inekwegoziechukwu@gmail.com

## Acknowledgements and References

- _Love-Running Project_- from Code Institute: Some of the Love-Running Project's style of naming was used in naming some of the ids and classes in Decor Awesome's website; also a few of Love-Running Project's css style rules were used in Decor Awesome's 'style.css' file.

- _Unsplash website_: All photos in the website were obtained from the [Unsplash website](unsplash.com) website.

- _Font Awesome_: All icons used in the 'enhanced-mood' section and in the footer section were gotten from the [Font Awesome](https://fontawesome.com/) website.

- _Google Fonts_: The two fonts, Oswald and Lato used in the website design were obtained from [Google Fonts](https://fonts.google.com/).