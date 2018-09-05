# ws1000-influxdb-bridge

This is a simple flask app that allows you to load the data submitted by your WS-1000 based weather station into InfluxDB for use with Grafana.

This app is also compatible with the Maplin N23dq WiFi Weather station (this is the station I have, but it's essentially a WS-1000 clone).

## Usage and installation

Settings are stored in the following environmental variables:

 * `HOST` - The InfluxDB host to log to, default: `localhost`
 * `PORT` - The port on which InfluxDB listens, default: `8086`
 * `USER` - InfluxDB Username, default: `(none)`
 * `PASS` - InfluxBD Password, default: `(none)`
 * `DB` - InfluxDB database name, default: `home`
 * `LPORT` - Local port to listen on for the WS1000 to connect to, default: `9999`

These settings can be conveniently set in the included systemd service template file.

The included service file can be edited and copied to e.g. `/etc/systemd/system`. Don't forget to issue `systemctl daemon-reload` and to enable to service.
