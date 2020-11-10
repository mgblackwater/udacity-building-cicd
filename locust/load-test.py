import time
from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 2)
    baseUrl = "https://mgblackwater-udacity-building-cicd.azurewebsites.net"

    @task
    def prediction_page(self):
        self.client.get(baseUrl)
    
    @task(5)
    def prediction_page(self):
        self.client.get(baseUrl+ "/predict")