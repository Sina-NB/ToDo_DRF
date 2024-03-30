from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    
    @task
    def accounts_index(self):
        self.client.get("/accounts")