from flask import Flask, render_template, request
import time
import os

#Telnet Added Information
import getpass
import sys
import telnetlib
#End Telnet Added Information

TiVo_IP_Address = "192.168.0.47"

app = Flask(__name__)

@app.route('/TiVo/<channel>')
def TiVo(channel):
       try:
           tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
           tn.write('SETCH '+ str(channel).replace("."," ") + '\r')
           tn.close()
           print "Channel Changed to", channel
       except:
           print "Telnet Error, Check TiVo IP Address"
       return 'TiVo channel as been changed to ' + channel


@app.route('/TiVo_Command/<command>')
def TiVo_Command(command):
       try:
           tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
           tn.write('IRCODE '+ str(command).upper() + '\r')
           tn.close()
           print "TiVo " + command
       except:
           print "Telnet Error, Check TiVo IP Address"
       return 'TiVo command ' + command + ' has been entered'

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)
