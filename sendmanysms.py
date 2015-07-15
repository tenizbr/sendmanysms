#!/usr/bin/env python
# sample script to show how to send multiple SMS to multiple recipients

import gammu
import sys

# Check parameters count
if len(sys.argv) < 3 or sys.argv[1] in ['--help', '-h', '-?']:
    print 'Usage: mass-sms <TEXT> [number]...'
    sys.exit(1)

# Configure Gammu
sm = gammu.StateMachine()
sm.ReadConfig()
sm.Init()
i=1
for number in sys.argv[3:]:
  message = {'Text': sys.argv[i], 'SMSC': {'Location': 1}}
  message['Number'] = number
  print "message =",message
  try:
        sm.SendSMS(message)
  except Exception, exc:
        print 'Sending to %s failed: %s' % (number, exc)
  i=i+1
