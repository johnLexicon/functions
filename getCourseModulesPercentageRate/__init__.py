import logging
from .utils import get_coursemodule_percentage, get_modules_names
import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    moduleName = req.params.get('moduleName')

    if not moduleName:
        return func.HttpResponse('You have to add a module name in the query string')

    moduleName = moduleName.lower()
    if moduleName == 'all':
        data = []
        names = get_modules_names()
        for name in names:
            percentage = get_coursemodule_percentage(name)
            data.append({name: percentage})
        return func.HttpResponse(json.dumps(data))


    result = get_coursemodule_percentage(moduleName)
    return func.HttpResponse(json.dumps({moduleName: result}), status_code=200)

