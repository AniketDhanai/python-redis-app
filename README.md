# python-redis-app

👉 This project demonstrates a simple web application built with Flask and Redis using Docker Compose.
👉 Each time you access the webpage, the counter increments and displays the number of visits.
👉 An image is also served through Flask’s static folder.

**Project Structure**
.
├── app.py                # Flask application code
├── docker-compose.yml    # Docker Compose file to set up Flask and Redis
├── requirements.txt      # Python dependencies
└── static/
    └── stickman.png      # Static image served on the webpage

**Features**
i.Flask app connected to Redis for counting visits.
ii.Static image serving through Flask.
iii.Simple containerized setup using Docker Compose.

📢 **Getting Started**

📌 **Prerequisites**<br />
👉Docker
👉Docker Compose

📌 **Steps**
👉Clone this repository:
git clone https://github.com/your-username/flask-redis-counter.git
cd flask-redis-counter
  
📌 **Start the application:**
docker-compose up

📌 **Access the app in your browser:**
http://localhost:5000

📌 **You should see:**
👉A "Hello Everyone!" message
👉A stickman image
👉A counter showing how many times the page has been visited

📌 **Notes**
👉The Flask app automatically connects to Redis using the service name redis.
👉Static files like images must be placed inside the static/ folder.
👉If you add new Python packages, update the requirements.txt file accordingly.


