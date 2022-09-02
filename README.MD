## **Python Behave BDD Framework**

This is a BDD automation framework developed on Selenium and Python Behave.
Sample test side used in this project is  http://10.4.4.20:6120/login


Page Object Model is followed in this framework

**pages** folder contains the elements and corresponding actions of the pages

**features** folder contains **steps** folder which has all the test files and also the feature files.

**requirements.txt** file contains all the python packages needed to run this framework

**allure** directory contains the files generated with allure reports

### **Commands to run the tests**

**To run the test with allure report**
` behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features -D url= http://10.4.4.20:6120/login
`
' behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features -D url= http://10.4.4.20:6120/login
'

**To run the test without allure report** 
`behave features`

**To run the test with allure report in parallel**
  python ./behave_parallel.py "-D url=https: http://10.4.4.20:6120/login" 
  python ./behave_parallel.py "-D url=http: http://10.4.4.20:6121/auth/login"