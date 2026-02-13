from locust import HttpUser, task

class DemoUser(HttpUser):
    @task
    def analytics(self):
        self.client.get("/analytics")