# python-redis-app<br />
<br />
    👉 This project demonstrates a simple web application built with Flask and Redis using Docker Compose.<br />
    👉 Each time you access the webpage, the counter increments and displays the number of visits.<br />
    👉 An image is also served through Flask’s static folder.<br />
<br />    
<strong>Project Structure</strong><br />
<br />
<pre>
<code>
.
├── app.py                # Flask application code
├── docker-compose.yml    # Docker Compose file to set up Flask and Redis
├── requirements.txt      # Python dependencies
└── static/
    └── stickman.png      # Static image served on the webpage
</code>
</pre>
<strong>Features</strong><br />
<br />
    i.Flask app connected to Redis for counting visits.<br />
    ii.Static image serving through Flask.<br />
    iii.Simple containerized setup using Docker Compose.<br />
<br />
📢 <strong>Getting Started</strong><br />
<br />
    📌 <strong>Prerequisites</strong><br />
<br />
        👉Docker<br />
        👉Docker Compose<br />
<br />
    📌 <strong>Steps</strong><br />
<br />
        👉Clone this repository:<br />
            
            git clone https://github.com/AniketDhanai/python-redis-app.git
            cd python-redis-app
  <br />
    📌 <strong>Start the application:</strong><br />
        
            docker-compose up
<br />
    📌 <strong>Access the app in your browser:</strong><br />
            
        http://localhost:5000
<br />
    📌 <strong>You should see:</strong><br />
<br />
        👉A "Hello Everyone!" message<br />
        👉A stickman image<br />
        👉A counter showing how many times the page has been visited<br />
    <br />
    📌 <strong>Notes</strong><br />
<br />
        👉The Flask app automatically connects to Redis using the service name redis.<br />
        👉Static files like images must be placed inside the static/ folder.<br />
        👉If you add new Python packages, update the requirements.txt file accordingly.<br />


