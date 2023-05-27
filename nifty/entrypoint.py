import os


WEBAPP_HOST = os.environ['WEBAPP_HOST']
WEBAPP_PORT = os.environ['WEBAPP_PORT']


def run_cmd(command: str):
    return os.system(command)


run_cmd(f"uvicorn api.app:app --host {WEBAPP_HOST} --port {WEBAPP_PORT}")
