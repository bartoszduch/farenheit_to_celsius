from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def test_f_to_c(self):
        self.client.post("/v1/models/f_to_c_model:predict", json={"signature_name": "serving_default", "instances": [{"fahrenheit": [32.0]}]})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
