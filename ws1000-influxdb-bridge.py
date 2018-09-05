#!/usr/bin/env python

# settings

HOST='grafana.analprolap.se'
PORT=8086
USER=''
PASS=''
DB='home'

# code
from flask    import Flask
from flask    import request
from influxdb import InfluxDBClient

import json

app = Flask(__name__)

@app.route('/weatherstation/updateweatherstation.php', methods=['GET'])
def update_weatherstation():
    action = request.args.get('action')
    if action == 'updateraw':
        intemp = request.args.get('intemp')
        outtemp = request.args.get('outtemp')
        dewpoint = request.args.get('dewpoint')
        windchill = request.args.get('windchill')
        inhumi = request.args.get('inhumi')
        rainrate = request.args.get('rainrate')
        dailyrain = request.args.get('dailyrain')
        weeklyrain = request.args.get('weeklyrain')
        monthlyrain = request.args.get('monthlyrain')
        yearlyrain = request.args.get('yearlyrain')
        outhumi = request.args.get('outhumi')
        windspeed = request.args.get('windspeed')
        windgust = request.args.get('windgust')
        winddir = request.args.get('winddir')
        absbaro = request.args.get('absbaro')
        relbaro = request.args.get('relbaro')
        light = request.args.get('light')
        uv = request.args.get('uv')
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
    app.run(port=9999, host='0.0.0.0')
