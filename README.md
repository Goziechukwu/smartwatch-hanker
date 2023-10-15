# Smartwatch Hanker

Smartwatch Hanker is an inventory management eCommerce platform designed with Python language, which runs in the Code Institute mock terminal on Heroku.

## Using Smartwatch Hanker

Upon visiting Smartwatch Hanker's platform, the user will be greeted with a welcoming message, and first of all asked if the user wants to update the inventory. If the user answers a 'yes', the user is given the opportunity to add stock values to the inventory, but if the user answers a 'no' or any other character or word, the user is taken to the check inventory step. The platform is responsive to all device types and works effectively on all browser types.

<img src="./assets/images/responsiveness.png" alt="Responsiveness screenshot">
 
Source: [Responsivity measurement](https://ui.dev/amiresponsive?url=https://smartwatch-hanker-d850ba2552c2.herokuapp.com/)

## Features


### • Update Inventory

The first input function in the platform is for updating the inventory. The user is asked to input new stock with values of product name and quantity. The user can input as many new stock as possible and the google worksheet adds every new stock to the bottom of the old stock worksheet in the google spreadsheet of stocks.

<img src="./assets/images/update-inventory.PNG" alt="Update Inventory image">


### • Getting Customer Orders

The next input function in the platform is for getting the customer orders. This function allows the user input customer ordered products with their corresponding quantities and saves the user's inputs in order to use the inputs to compare with the available stock.

<img src="./assets/images/customer-orders.png" alt="Customer Orders image">


### • Check Inventory

The check inventory input function compares the inputed quantity of each ordered product with the corresponding stock quantity value, for all inputed customer orders. The function further gives report to the user whether there is enough quantity of product in stock to meet the quantity ordered. In the case that the quantity ordered is greater than the quantity in stock, the function tells the user what quantity was orderd and also what quantity is available in stock of the product, so that the user can quickly have a good estimate of what quantity might be required to meet the quantity ordered.

<img src="./assets/images/check-inventory.png" alt="Check Inventory image">


## Technologies Used:

• The platform was created with the Python 3 programming language and gspread and json libraries were imported and used. A google spreadsheet containing a worksheet having all the available stock products and their corresponding quantity values was used. The link to the google spreadsheet is as follows:

[Google Spreadsheet of Stock Values](https://docs.google.com/spreadsheets/d/1g8xChW8Bc8L3gRskRAvlpJbzW4Tld_9Tezh3JE8Ubd8/edit?usp=sharing)

• The workspace used to write the code was:

- Codeanywhere workspace

• All codes and commits were pushed to GitHub repository

• The terminal used to run the code was the Code Institute's Heroku mock terminal:

## Validation Testing

The python code used in the platform was passed through the Pycode linter and tested for validation, and no errors were returned.

<img src="./assets/images/validation-testing-screenshot-1.png" alt="First Validation Testing">


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