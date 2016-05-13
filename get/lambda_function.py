import json


class TestingState:

    status_saved = None

    def set_status(self):
        self.status_saved = True

    def get_status(self):
        return self.status_saved

def lambda_handler(event, context):

    ola = TestingState()
    if ola.get_status() == None:
        ola.set_status()
        return "Status is not saved, force set status"

    if ola.get_status() == True:
        return "Status saveedd"