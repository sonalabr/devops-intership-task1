from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hi I am Python Flask App from CI/CD with GitHub Actions and Dockerhub"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
