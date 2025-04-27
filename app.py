from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    count = redis.get('hits').decode('utf-8')  # decode bytes to string
    return f"""
        <html>
            <head><title>Hello from Flask + Redis</title></head>
            <body style="text-align: center; margin-top: 50px;">
                <h1>Hello Everyone!</h1>
                <img src="/static/image.png" alt="image not available">
                <p>You have been hit {count} times.</p>
            </body>
        </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

