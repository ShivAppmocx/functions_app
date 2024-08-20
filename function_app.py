import azure.functions as func
from azure.functions import FunctionApp
import logging

app = FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
@app.route(route="funcRunPythonScript")
def funcRunPythonScript(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

if __name__ == '__main__':
    app.run(debug=True)

