from locust import HttpUser, task

class MyEventsUser(HttpUser):
    host = "http://localhost:8000"
    wait_time = lambda self: 1

    @task
    def view_my_events(self):
        self.client.get("/my-events")