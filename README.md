# 🚀 Simple Docker CI/CD App

This project demonstrates skills in **Docker**, **Git**, and **CI/CD processes** using **GitHub Actions**.  
It implements a complete workflow: from running an application locally in a Docker container to automatic deployment to a remote environment after each push to the main branch.

---

## 📖 Application Description

This app is a minimalistic web service built with **Python (Flask)**.  
It has a single route `/` which, on each request:

- generates a random color in HEX format (e.g. `#7ae634`);
- displays it on the page in the format:
- Random Color: #7ae634
- styles the text with the generated color 🎨.

So every time you refresh the page, you see a new random color.

🔗 Live demo: [https://simple-docker-ci-app.fly.dev/](https://simple-docker-ci-app.fly.dev/)

### Code snippet (`app.py`)
```python
# Import the Flask framework to create the web application
from flask import Flask

# Import the random module to generate random numbers
import random

# Create a Flask application instance
# "__name__" tells Flask where to look for resources like templates and static files
app = Flask(__name__)

# Define a route for the root URL ("/")
# When a user visits the homepage, this function will be executed
@app.route("/")
def home():
    # Generate a random color in HEX format (e.g., #7ae634)
    # "%06x" ensures the color code is always 6 hexadecimal digits
    color = "#%06x" % random.randint(0, 0xFFFFFF)
    
    # Return a simple HTML response
    # The text "Random Color: ..." will be displayed in the generated color
    return f"<h1 style='color:{color}'>Random Color: {color}</h1>"

# Run the app only if this script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server
    # host="0.0.0.0" makes the app accessible from outside the container
    # port=5000 is the default port for Flask apps
    app.run(host="0.0.0.0", port=5000)
```

## 📌 Deliverables

- Public repository with source code and CI/CD pipeline → [GitHub](https://github.com/quarwork/simple-docker-ci-app)
- Docker image built from Dockerfile → [Docker Hub](https://hub.docker.com/r/quarwork/simple-docker-ci-app)
- Deployed demo app available online → [Demo](https://simple-docker-ci-app.fly.dev/)

## 🛠 Technologies Used

- Python + Flask — web application
- Docker — containerization of the app
- GitHub Actions — CI/CD pipeline automation
- Docker Hub — image registry
- Fly.io — container hosting service

## 📂 Project Structure

```bash
simple-docker-ci-app/
│── .github/
│   └── workflows/docker.yml      # GitHub Actions CI/CD workflow
│── assets/
│   └── demo.png                  # Demo screenshot
│── .gitignore                    # Git ignore file
│── Dockerfile                    # Docker container definition
│── LICENSE                       # MIT license
│── README.md                     # Documentation
│── app.py                        # Demo app source code (Python Flask)
│── fly.toml                      # Fly.io deployment configuration
│── requirements.txt              # Python dependencies
```

## ▶️ Run Locally

1. Clone the repository:
```bash
    git clone https://github.com/quarwork/simple-docker-ci-app.git
    cd simple-docker-ci-app
```
2. Build the Docker image:
```bash
    docker build -t simple-docker-ci-app .
```
5. Run the container:
```bash
    docker run -p 5000:5000 simple-docker-ci-app
```
7. Open in your browser:
    [http://localhost:5000/](http://localhost:5000/)

## 🚀 Automatic Deployment on Fly.io

After each push to the main branch, GitHub Actions automatically:
1. Builds the Docker image from Dockerfile.
2. Publishes it to [Docker Hub](https://hub.docker.com/r/quarwork/simple-docker-ci-app)
3. Deploys the container to Fly.io.
As a result, the app is available online at:
👉 [https://simple-docker-ci-app.fly.dev/](https://simple-docker-ci-app.fly.dev/)

## ⚙️ CI/CD Workflow

Simplified pipeline diagram:
```lua
   ┌─────────────┐        ┌───────────────┐       ┌────────────────┐        ┌─────────────┐
   │   GitHub    │  push  │ GitHub        │ build │ Docker Hub     │  pull  │   Fly.io    │
   │ Repository  │──────▶ │ Actions CI/CD│──────▶│ Image Registry │──────▶│ Deployment  │
   └─────────────┘        └───────────────┘       └────────────────┘        └─────────────┘
```
1. Push to main → triggers GitHub Actions.
2. Workflow steps:
- Build Docker image.
- Push to Docker Hub.
- Deploy to Fly.io.
3. App becomes publicly available.
Pipeline file: [.github/workflows/docker.yml](https://github.com/quarwork/simple-docker-ci-app/blob/main/.github/workflows/docker.yml)

## 📦 Docker Hub

Public image available here:
👉 Docker Hub: [https://hub.docker.com/r/quarwork/simple-docker-ci-app](https://hub.docker.com/r/quarwork/simple-docker-ci-app)

## 🌍 Demo

The app is automatically deployed and accessible at:
👉 [https://simple-docker-ci-app.fly.dev/](https://simple-docker-ci-app.fly.dev/)

## 🖼️ Example Output

Here’s how the application looks in action:
[Demo Screenshot](https://github.com/quarwork/simple-docker-ci-app/blob/main/assets/demo.png)

## ✅ Conclusion

This project demonstrates:
- Development of a Python Flask app (random color generator)
- Containerization with Docker
- CI/CD automation with GitHub Actions
- Publishing Docker images to Docker Hub
- Automatic deployment to Fly.io



👤 Author: [quarwork](https://github.com/quarwork)
