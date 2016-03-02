from subprocess import call
from flask import Flask
app = Flask(__name__)

CODESEND = "/var/www/rfoutlet/codesend"

codes = {
  "1": {
    "on": 87347,
    "off": 87356
  },
  "2": {
    "on": 87491,
    "off": 87500
  }
}

@app.route('/<num>/<cmd>')
def exec_command(num, cmd):
  if num in codes:
    if cmd in codes[num]:
      call([CODESEND, str(codes[num][cmd])])
      return "success", 200
  return "fail", 500

if __name__ == '__main__':
  app.run(host='0.0.0.0')