from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse


def health(request):
    return JsonResponse({"status": "ok"}, safe=False)


def error(request):
    headers = request.headers
    code = "404"

    if 'X-Code' in headers:
        code = headers['X-Code']

    if 'X-Service-Name' in headers:
        service = headers['X-Service-Name']

    if code == "500":
        error_code = "50"
    elif code == "503":
        error_code = "53"
    elif code == "400":
        error_code = "40"
    elif code == "403":
        error_code = "43"
    elif code == "405":
        error_code = "45"
    elif code == "406":
        error_code = "46"
    else:
        error_code = "44"

    return JsonResponse({"Tiebreaker": "111", "NearRealTimeRsnCode1": error_code}, safe=False, status=code)
