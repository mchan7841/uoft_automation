
import yaml
import time
import website_login
import recreation
import datetime

DAYS = 2

with open("login.yml", "r") as stream:
    try:
        conf = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

utorid = conf['uoft_user']['utorid']
password = conf['uoft_user']['password']

website_login.uoft_login(utorid, password)
time.sleep(5)
website_login.program_time("https://recreation.utoronto.ca/Program/GetProgramDetails?courseId"
                        "=d02a8d46-e2d5-450b-90d9-de40a36d870c&semesterId=0ceb5a30-42f1-4069-a97b"
                        "-5e015b379e14", datetime.datetime(2021, 12, 30, 19, 0), 60)
