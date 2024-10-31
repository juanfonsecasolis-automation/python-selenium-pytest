# python-selenium-pytest

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
pytest -m <testSuite>
deactive
```

# References
1. Python Software Foundation. venv — Creation of virtual environments. URL: https://docs.python.org/3/library/venv.html#how-venvs-work
2. PyTest Dev Team. Get Started. URL: https://docs.pytest.org/en/stable/getting-started.html#get-started
3. Sergey Pirogov. webdriver-manager 4.0.2. URL: https://pypi.org/project/webdriver-manager/
4. PyTest Dev Team. Changing standard (Python) test discovery. URL: https://docs.pytest.org/en/7.1.x/example/pythoncollection.html
5. Baiju Muthukadan. 2. Getting Started. URL: https://selenium-python.readthedocs.io/getting-started.html#simple-usage