from django.http import HttpResponse
import json


def response_as_json(data):
    response = HttpResponse(
        json.dumps(data),
        content_type="application/json;charset=utf-8",

    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "成功",
        "data": data,
    }
    return response_as_json(data)