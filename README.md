# python-selenium-util
Set of convenient methods for **Selenium WebDriver** making your code **clean** and less verbose.

## Installation
To install dependencies:
```
$ pip install selenium
```

For Firefox download [geckodriver](https://github.com/mozilla/geckodriver/releases) for your OS and put it in the main dir.

For Chrome download [ChromeDriver](https://chromedriver.chromium.org/downloads) for your OS and put it in the main dir.

## Example
To train and predict:
```
import selenium_util

driver = selenium_util.init('Firefox')
driver.get('https://www.wikipedia.org/')
sleep(1)
selenium_util.find_first_input(driver).send_keys('Slovio' + Keys.RETURN)
```
## License
[Apache License 2.0](LICENSE)