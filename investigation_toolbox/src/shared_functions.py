import requests
import docs.conf as conf
import json
from datetime import datetime

def logger(input_data):
  current_date = datetime.today().strftime('%Y-%m-%d')
  current_time = datetime.today().strftime('%H:%M:%S')
  with open(f"logs\error_log-{current_date}.txt", "a") as f:
    f.write(f"{current_time} | {input_data}\n")
  f.close()
