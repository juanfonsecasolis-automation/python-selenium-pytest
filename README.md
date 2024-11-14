# python-selenium-pytest

[![Python application](https://github.com/juanfonsecasolis-automation/python-selenium-pytest/actions/workflows/python-app.yml/badge.svg)](https://github.com/juanfonsecasolis-automation/python-selenium-pytest/actions/workflows/python-app.yml)

2024 Juan M. Fonseca-Solís

# Set up [1]
```
sudo apt-get install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Run [1]
```
source .venv/bin/activate 
pytest -m <testSuite> --browser='Chrome' --html=reports/report.html -n auto
deactive
```

# Theory
* PyTest is a syntax framework that can be integrated to Selenium WebDriver [2, 3, 5].
* The set-up and tear-down code blocks are stored in the same function but separated by the keyword "yield" [6].
* Test suites are specified putting the "pytest.mark.nameOfSuite" annotation above test methods and registered in the pytest.ini file.
* PyTest finds test methods that starts with prefix "_test" (on clases), the classes that store those methods need to start with the "Test" suffix [4].
* User can add extra options to the pytest command by modifying the "pytest_addoption" method of the conftest.py file [6].
* The function for providing the webdriver as a fixture to methods goes in the conftest.py [7].
* Single leading underscore (like in _variable) indicates that the member (variable or method) is for internal use (private or protected?) and _should_ not be invoked outside the class. Double leading underscore (like in __variable) triggers Python's name mangling, which means that the member can be access only by appending the class name (for example, _MyClass__variable) and prevents child classes from overriding it [8].
* _Page Object Modal_ is a test automation standard that separates the verification logic from the webpages interaction logic to make the code more maintenable [9].

# References
1. Python Software Foundation. venv — Creation of virtual environments. URL: https://docs.python.org/3/library/venv.html#how-venvs-work
2. PyTest Dev Team. Get Started. URL: https://docs.pytest.org/en/stable/getting-started.html#get-started
3. Sergey Pirogov. webdriver-manager 4.0.2. URL: https://pypi.org/project/webdriver-manager/
4. PyTest Dev Team. Changing standard (Python) test discovery. URL: https://docs.pytest.org/en/7.1.x/example/pythoncollection.html
5. Baiju Muthukadan. 2. Getting Started. URL: https://selenium-python.readthedocs.io/getting-started.html#simple-usage
6. Jen Chen. pytest - fixture; Setup and Teardown. URL: https://hackmd.io/@jenc/SJYmGcKsK
7. QA Automation Expert. Page Object Model Implementation of Python with Selenium – PyTest. April 2, 2024. URL: https://qaautomation.expert/2024/04/02/page-object-model-implementation-of-python-with-selenium-pytest/ (last consulted on 11/04/24).
8. Leodanis Pozo Ramos. Single and Double Underscores in Python Names. Real Python. Nov 29, 2023. URL: https://realpython.com/python-double-underscore (last consulted on 11/11/24).
9. Phil Ebiner, Dmitry Shyshkin, Video School. Learn Selenium WebDriver Python Course for professional Selenium WebDriver browser testing and automation. URL: https://www.udemy.com/course/selenium-webdriver-python-course (yes, I purchased this course by my own means to complete the training I left incomplete!)