import functions_framework
from flask import Request
from mathematics import add

@functions_framework.http
def hello_add(request: Request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    Note:
        For more information on how Flask integrates with Cloud
        Functions, see the `Writing HTTP functions` page.
        <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
    """
    result = "0"
    if not request.is_json:
        return result
    
    # Get the JSON data
    data = request.get_json()
    
    # Check if the required fields exist
    if 'num1' not in data or 'num2' not in data:
        return result
    
    # Extract the values
    num1 = data.get('num1')
    num2 = data.get('num2')

    # Add numbers together
    result = str(add(num1, num2))
    return result
