# BDD-Tests-for-demola.com
demola.com Automated BDD Testing Framework

📚 Technologies:

BDD (Behaviour Driven Development):
features folder
steps folder
Behave Library
Gherkin
Python & PyCharm
POM (Page Object Model) in pages folder
📝 Commands in cmd file for Behave and Selenium

pip install -u selenium
pip install behave
pip install behave-html-formatter
pip install webdriver-manager
To run the BDD tests use in Terminal:
behave -f html -o behave-report.html --tags=smoke for sign_in BDD tests
behave -f html -o behave-report.html --tags=regression for all BDD tests

➡️ Gherkin syntax keywords:

Feature
Given, When, Then, And, But for steps (or *)
Background
Scenario
Scenario Outline - data in tables + Examples
➡️ POM:

classes, objects, methods
OOP: Inheritance principle
⏩ Steps to download the repository:

Navigate to the upper level of the project;
Click on the blue ‘Code’ button;
Choose either ‘Open with Github Desktop’ if you have installed ‘Github Desktop’ on your computer or ‘Download ZIP’ to download as ZIP document
Make sure you use PyCharm with this repository
Install the commands from cmd file
Run the test with:
- behave -f html -o behave-report.html --tags=smoke for sign_in BDD tests
- behave -f html -o behave-report.html --tags=regression for all BDD tests
