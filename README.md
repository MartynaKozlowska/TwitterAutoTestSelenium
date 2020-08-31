# TwitterAutoSeleniumTest
Automated testing of Twitter Web App using Selenium with Python.

## Configuration
* Install required software:
  * Google Chrome
  * Python 3
  * Chromedriver (version compatible with Google Chrome)
* Add Python and Chromedriver to the environment variable PATH
* Install Python packages:
```
pip install -r requirements.txt
```
* Configure Python Virtual Environment:
```
pip install -U virtualenv
virtualenv -p python.exe venv
```
* Activate Python Virtual Environment:
```
venv\Scripts\activate
```
## Running tests
**To run all tests:**  
```
pytest
```
**To run only one test:**  
```
pytest <test_file_name.py>
```