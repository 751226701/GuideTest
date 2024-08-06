class Requests:

    token = ''

    URL = "http://192.168.21.244:80/getmsginfo"

    loggin = {
        "action": "request",
        "cmdtype": 501,
        "sequence": 1,
        "message": {
            "username": "admin",
            "password": "Tewp+df7dfmTQy2d5S/fmuiCXRleo26a8VYu6M0kzK1CF/UfgqMRSDiOnniU0l9nAzemdqOIt0so360nRrgM6Fun20LKGcqddentxQLpiRkKUqWQOGSPnnPxg5jb0GfKJcgymt5MhKx71vRpd/nZRFVTOkGEg6qN9+FRDrSo+hY="
        }
    }

    logout = {
        "action": "request",
        "cmdtype": 502,
        "sequence": 1,
        "token": token,
        "message": {
        }}

    resultDir = '/APP/pycharm/project/GuideTest/Report/result'
    reportDir = 'allure generate /APP/pycharm/project/GuideTest/Report/result -o /APP/pycharm/project/GuideTest/Report/report --clean'

    request_01 = {
        "action": "request",
        "cmdtype": 500,
        "sequence": 1,
        "message": {}
    }

    request_02 = {
        "action": "request",
        "cmdtype": 501,
        "sequence": 1,
        "message": {
            "username": "admin",
            "password": "Tewp+df7dfmTQy2d5S/fmuiCXRleo26a8VYu6M0kzK1CF/UfgqMRSDiOnniU0l9nAzemdqOIt0so360nRrgM6Fun20LKGcqddentxQLpiRkKUqWQOGSPnnPxg5jb0GfKJcgymt5MhKx71vRpd/nZRFVTOkGEg6qN9+FRDrSo+hY="
        }
    }

    request_03 = {
        "action": "request",
        "cmdtype": 530,
        "sequence": 1,
        "token": token,
        "message": {
            "type": 0
        }

    }

    request_04 = {
        "action": "request",
        "cmdtype": 532,
        "sequence": 1,
        "token": token,
        "message": {
            "type": 5,
            "value": 500
        }
    }

    re = {
        "action": "request",
        "cmdtype": 9999,
        "message": {},
        "sequence": 1,
        "token": token
    }
