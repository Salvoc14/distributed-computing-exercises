from flask import Flask
import redis
import os

app = Flask(__name__)
redis = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'))

@app.route("/")
def count():
    redis.incr('counter')
    return "Counter is %s" % redis.get('counter').decode("utf-8")

if __name__ == "__main__":
    app.run(host="0.0.0.0")

