## Do
* refactor image uploading to use flask-uploads

* image upload check should appear if the form starts with an image in it
  * for example if the user hits the back button the check should be there

* style the 404 and 413 pages to be friendlier


## Do (User Experience Interview Feedback)
* The view page should have the settings in a sidebar (if screen space permits) so that the user can look at their full image while they adjust settings
  * User should be able to view full image on a new blank tab
  * generate a small preview so that the user can see the ascii art without scrolling

* Download should be quicker and not freeze the page
  * This is mostly so slow because of each character being wrapped in a span. If we could find a way to color without this the download would go much faster

* find a way to allow for custom color picking for the text color of the output
  * This might be an acceptable situation to use !important to force color over top of the spans

## Doing
* Organize CSS styles and add index (table of contents) to css file


## Done
* Fix auto determine height to work better with landscape photos
* submit button should fit theme better
* Replace Toggle Buttons with Tabs or Dropdowns
  * Font Color - Done
  * Character Set - Done
* Possibly make the tooltip for custom characters flash when you swap to it so that users know to hover over it
* convert label tips (parts in parentheses) to tooltips
* Make tooltips for every input
* upload checkmark should not appear if image was too large
* max upload size labels are now set by flask server config
* fix heroku memory error on large file upload
  * refactor converter.py to shrink the image before converting the pixels to pixel objects
* Add a description telling the user that the height and width are how many characters the art will have and that bigger means more detail will be in the ascii conversion.
* Add placeholder for the custom character creator to show what an example key would look like
* Put the font drop down above the font weight slider
* create 404 and 413 (upload size exceeded) error pages
* create save as image tool for viewer page
* fix background blur only appearing on desktop google chrome >:O
* fix custom button on convert page dropping down
* deploy
* create hero image for home page
* create about us bio for home page
* create icon for the website
* on preview page
  * the color settings on the preview page should change the ascii image's color
    * there should be a button to toggle default or custom and the button should change text when toggled so it would say Default Colors and then when toggled it would say Custom Colors 
      * if default it shoud have a checkbox for use black only
      * if custom it should have a color input
    * there should be a color picker for background color as well
  * there should be a dropdown that lets you change the font of the ascii image
  * there should be a slider to change the font weight
* create a second page to preview the conversion
* build settings ui for convert page
  * on the convert page the sliders for height and width should change the height and width of a preview ascii image for reference
  * there should be a toggle for character sets. text on button should switch between default and custom. 
    * if it is default the user should be able to choose the set from a dropdown menu
    * if it is custom the user should be able to enter a comma seperated list that is the character set.
* upload image loading bar
* allow user to specify height in lines or leave it to default
* add an option to use color in images
* make flask web server and add bootstrap to base template
* create a color -> symbol key
* working ascii converter in python terminal with black and white shading
* make converter work with png files
* add a way to reduce the 

## Icebox