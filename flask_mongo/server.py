from flask import Flask
from flask import request

import models

app = Flask(__name__)

@app.route('/')
def hello_world():
    ip, _, _ = request.headers.get('x-forwarded-for',
                                   request.remote_addr).partition(',')
    hit_counter = models.IPHitCounter.get_or_create(ip)
    hit_counter.update(inc__hits=1)
    hit_counter.reload()
    return 'Hello World, hit no {}!'.format(hit_counter.hits)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
