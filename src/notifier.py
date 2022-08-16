from pynotifier import Notification
import requests

def __always_true():
    return True

class Notifier:
    def __always_true():
        return True

    def __init__(self, title: str, info: str, state = __always_true):
        self.title, self.info = title, info
        self.status_check = state

    def send(self):
        requests.post(url='https://grouch-webhook-service.tmthecoder.workers.dev/', json={
            "title": self.title,
            "description": self.info
        })

    def run(self):
        while not self.status_check():
            continue
        self.send()

    def run_async(self):
        if self.status_check():
            self.send()

    def run_force(self):
        self.send()
