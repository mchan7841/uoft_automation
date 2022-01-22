# uoft_automation

This repository contains functions used to automate the registration of activity programs and Ucheck.

The webdriver for this project is for google chrome version 97. If you run a different version of chrome or use a different browser, replace this file with the correct driver. The drivers for other Chrome versions can be found here: https://chromedriver.chromium.org/downloads.

When using the Ucheck functionality ensure that you do not have symptoms of COVID-19, you are fully vaccinated, neither you nor anyone in your immediate bubble has tested positive for COVID-19, and you have been identified as someone who has been in close contact with any individuals that have tested positive for COVID-19. For more information on COVID-19, please visit https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19.html.

Setting up the Python Script
- Change the Password and Username in the login.yml file.
- View the file sample_test.py and modify it based on your specific needs.
- Replace "url" with the url of the program you want to sign up for

Different Functions for Program Registration
- For sport and rec programs use sport_rec
- For Hart House programs use hart_house

For information on running python scripts repeatedly view the documentation for schedule here: https://pypi.org/project/schedule/.
