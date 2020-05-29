# DevOps-Take-Home
1. Create your own AWS Account to utilize during this exercise.  Utilize free-tier where possible to avoid costs being charged to you, and don't forget to destroy all resources when you're done.  We don't want this to cost you money :)

2. Then, create a Kubernetes cluster in AWS that hosts the Flask application (app.py) as well as a Postgres database for the application to access.  *HINT:*  You will need image(s) and files to deploy the application and database in Kubernetes.  *HINT2:* Your image(s) will need to be accessible from within AWS.

3. Once your Flask application and Postgres database are running in Kubernetes, proceed.

4. Scale your application to 2 instances.

5. Follow instructions below for *interacting with the API.*

## Interact with the API
POST a message to the API:
```bash
curl -X POST http://127.0.0.1:5000/message -H "Content-Type: application/json" --data '{"message": "hi"}'
```

GET a message
```bash
curl http://127.0.0.1:5000/message/1
```

HEALTHCHECK
```bash
curl http://127.0.0.1:5000/healthcheck
```

# Test Locally
If you desire to test locally to see things working there first before you put it on Kubernetes, you can follow the instructions below:

## Install the app
```bash
git clone https://github.com/geezerP/devops-assessment.git
cd devops-assessment
virtualenv -p python3 .
source bin/activate
pip install -r requirements.txt
```

## Start the app
If you're using a local postgres db use the following to run the app.
```bash
DATABASE_URL='postgresql://postgres:postgres@localhost:5432/groundspeed_devops' python app.py
```