from trafficapp.uis.trafficapp import WTrafficApp
import sys

app = WTrafficApp()
status = app.exec()
sys.exit(status)
