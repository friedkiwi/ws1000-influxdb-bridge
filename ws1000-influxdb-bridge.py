#!/usr/bin/env python

# settings

HOST=''
PORT=8086
USER=''
PASS=''
DB=''
LPORT=9999

# code
from flask    import Flask
from flask    import request
from influxdb import InfluxDBClient

import json
import os

app = Flask(__name__)

@app.route('/weatherstation/updateweatherstation.php', methods=['GET'])
def update_weatherstation():
    action = request.args.get('action')
    if action == 'updateraw':
        intemp = float(request.args.get('intemp'))
        outtemp = float(request.args.get('outtemp'))
        dewpoint = float(request.args.get('dewpoint'))
        windchill = float(request.args.get('windchill'))
        inhumi = float(request.args.get('inhumi'))
        rainrate = float(request.args.get('rainrate'))
        dailyrain = float(request.args.get('dailyrain'))
        weeklyrain = float(request.args.get('weeklyrain'))
        monthlyrain = float(request.args.get('monthlyrain'))
        yearlyrain = float(request.args.get('yearlyrain'))
        outhumi = float(request.args.get('outhumi'))
        windspeed = float(request.args.get('windspeed'))
        windgust = float(request.args.get('windgust'))
        winddir = float(request.args.get('winddir'))
        absbaro = float(request.args.get('absbaro'))
        relbaro = float(request.args.get('relbaro'))
        light = float(request.args.get('light'))
        uv = float(request.args.get('UV'))
        ws_id = request.args.get('ID')

        client = InfluxDBClient(HOST, PORT, USER, PASS, DB)

        ws_full_log_object = [{
            "measurement": "ws1000",
            "tags": {
                "id": ws_id
            },
            "fields": {
                "indoor_temp": intemp,
                "outdoor_temp": outtemp,
                "dewpoint": dewpoint,
                "windchill": windchill,
                "indoor_humidity": inhumi,
                "outdoor_humidity": outhumi,
                "rain_rate": rainrate,
                "rain_daily": dailyrain,
                "rain_weekly": weeklyrain,
                "rain_monthly": monthlyrain,
                "rain_yearly": yearlyrain,
                "wind_speed": windspeed,
                "wind_gustspeed": windgust,
                "wind_direction": winddir,
                "pressure_abs": absbaro,
                "pressure_rel": relbaro,
                "light_intensity": light,
                "uv_radiation": uv
            }
        }]

        client.write_points(ws_full_log_object)

    return ""

if __name__ == '__main__':
    HOST  = os.getenv("HOST", "localhost")
    PORT  = int(os.getenv("PORT", "8086"))
    USER  = os.getenv("USER", "")
    PASS  = os.getenv("PASS", "")
    DB    = os.getenv("DB",   "home")
    LPORT = int(os.getenv("LPORT", "9999"))

    app.run(port=LPORT, host='0.0.0.0')
