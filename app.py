from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host=&apos;redis&apos;, port=6379)

@app.route(&apos;/&apos;)
def hello():
    redis.incr(&apos;hits&apos;)
    count = redis.get(&apos;hits&apos;).decode(&apos;utf-8&apos;)  # decode bytes to string
    return f&quot;&quot;&quot;
        &lt;html&gt;
            &lt;head&gt;&lt;title&gt;Hello from Flask + Redis&lt;/title&gt;&lt;/head&gt;
            &lt;body style=&quot;text-align: center; margin-top: 50px;&quot;&gt;
                &lt;h1&gt;Hello Everyone!&lt;/h1&gt;
                &lt;img src=&quot;/static/stickman.png&quot; alt=&quot;image not available&quot;&gt;
                &lt;p&gt;You have been hit {count} times.&lt;/p&gt;
            &lt;/body&gt;
        &lt;/html&gt;
    &quot;&quot;&quot;
if __name__ == &quot;__main__&quot;:
    app.run(host=&quot;0.0.0.0&quot;, debug=True)
