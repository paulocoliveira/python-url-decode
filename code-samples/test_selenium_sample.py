import pytest
from urllib.parse import unquote

@pytest.mark.parametrize("url, expected_decoded_url", [
    ("https://www.lambdatest.com/selenium-playground/simple-form-demo?my%20message=Tests%20are%20covering%2097%%20of%20the%20scope.%20Total%20cost%20of%20testing%20activities%20this%20sprint%20was%20$1299.55%20(US%20Dollar)", 
     "https://www.lambdatest.com/selenium-playground/simple-form-demo?my message=Tests are covering 97% of the scope. Total cost of testing activities this sprint was $1299.55 (US Dollar)"),
    ("https://www.lambdatest.com/selenium-playground/input-form-demo?my%20message=Minimum%20lib%20versions%20to%20run%20these%20codes%20are%20selenium%3E%3D4.11.2%2C%20requests%3E%3D2.31.0%2C%20and%20pytest%3E%3D7.4.3", 
     "https://www.lambdatest.com/selenium-playground/input-form-demo?my message=Minimum lib versions to run these codes are selenium>=4.11.2, requests>=2.31.0, and pytest>=7.4.3"),
    ("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo?my%20message=We%20can%20run%20all%20these%20tests%20in%20parallel%20using%20pytest-xdist", 
     "https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo?my message=We can run all these tests in parallel using pytest-xdist")
])
def test_selenium_sample(url, expected_decoded_url, driver):   
    # Navigate to the URL
    driver.get(url)

    # Maximize browser window
    driver.maximize_window()

    # Get and print the current browser URL
    current_url = driver.current_url
    print("\nCurrent URL:", current_url)

    # Decode the URL
    decoded_url = unquote(current_url)

    # Check output
    assert decoded_url == expected_decoded_url

    # Print the decoded URL
    print("\nDecoded URL:", decoded_url)