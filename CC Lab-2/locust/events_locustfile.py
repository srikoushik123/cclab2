from locust import HttpUser, task, between


class EventsUser(HttpUser):
    # Base URL (add this to avoid host errors)
    host = "http://localhost:8000"   # 🔁 change if needed

    # Slower think time → controlled load
    wait_time = between(2, 4)

    @task
    def view_events(self):
        with self.client.get(
            "/events",
            params={"user": "locust_user"},
            name="View Events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure("Failed to load events")

