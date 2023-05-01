from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def my_task(self):
        self.client.get("/my-url")

    @task
    def another_task(self):
        self.client.post("/my-url", {"param": "value"})
