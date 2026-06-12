from flask import Flask
import os
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def dashboard():
    app_name = os.getenv("APP_NAME", "Gaming Platform")
    version = os.getenv("APP_VERSION", "v1.0")
    environment = os.getenv("ENVIRONMENT", "development")

    return f"""
    <h1>{app_name}</h1>
    <h2>Version: {version}</h2>
    <h3>Environment: {environment}</h3>

    <br>

    <a href="/cpu">Run CPU Stress Test</a>
    """

@app.route("/cpu")
def cpu():
    x = 0

    # Heavy CPU workload
    for i in range(500000000):
        x += i

    return f"CPU Stress Test Completed! Result = {x}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)