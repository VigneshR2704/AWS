
Cloud and DevOps Lab Experiments Report
1) Launch EC2 Instance, Configure CloudWatch and CloudTrail
Step 1: Launch EC2 Instance
- Go to AWS Console > EC2 > Launch Instance
- Choose Amazon Linux AMI, t2.micro, and configure security group with SSH port 22 open.
Step 2: Install CloudWatch Agent
$ sudo yum update -y
$ sudo yum install -y amazon-cloudwatch-agent
Step 3: Create CloudWatch Agent Config
$ sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
Step 4: Start CloudWatch Agent
$ sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a start
Step 5: Enable CloudTrail
- Go to CloudTrail > Create trail
- Choose S3 bucket and enable for all regions
Step 6: Simulate Activity
- SSH into instance using: ssh -i key.pem ec2-user@<public-ip>
- CloudTrail logs login and API actions
Step 7: View Logs
- Go to CloudTrail > Event history
- Go to CloudWatch > Logs > View log group created



2) Git Operations: Clone, Commit, Push, Fetch, Pull, Checkout, Reset, Delete Branch
Step 1: Clone Repo
$ git clone https://github.com/your/repo.git
Step 2: Make Changes
$ echo "New Line" >> test.txt
Step 3: Add and Commit
$ git add test.txt
$ git commit -m "Added new line"
Step 4: Push Changes
$ git push origin main
Step 5: Fetch and Pull
$ git fetch origin
$ git pull origin main
Step 6: Checkout Branch
$ git checkout -b new-feature
Step 7: Reset Commit
$ git reset --hard HEAD~1
Step 8: Delete Branch
$ git branch -d new-feature
$ git push origin --delete new-feature





3) Clone GitHub Repo, Modify File, Commit, Push, View Git Log
Step 1: Clone Repository
$ git clone https://github.com/your/repo.git
Step 2: Modify a File
$ echo "Modified line" >> index.html
Step 3: Commit Changes
$ git add index.html
$ git commit -m "Updated index"
Step 4: Push to GitHub
$ git push origin main
Step 5: View Git Log
$ git log --oneline




4) Simulate Brute-force SSH Login and Detect with CloudTrail/CloudWatch
Step 1: Simulate Brute-force
Run from another system:
$ for i in {1..10}; do ssh wrong@<ec2-ip>; done
Step 2: Enable CloudTrail (if not already)
- Go to CloudTrail > Trails > Create trail
Step 3: Send Auth Logs to CloudWatch
- Edit CloudWatch agent config to include /var/log/secure (Amazon Linux)
Step 4: Create Metric Filter
- Go to CloudWatch > Logs > Metric filters
- Filter pattern: "Failed password"
Step 5: Create Alarm
- CloudWatch > Alarms > Create alarm on metric filter
- Action: Send notification via SNS
Step 6: Check Logs
- View log stream for SSH failure entries




5) Dockerize a Simple Web Application
Step 1: Create Files
- app.py:
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello(): return "Hello from Docker!"
if __name__ == "__main__": app.run(host="0.0.0.0", port=5000)
- requirements.txt:
flask
Step 2: Dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
Step 3: Build Docker Image
$ docker build -t flask-web-app .
Step 4: Run Container
$ docker run -d -p 5000:5000 flask-web-app
Step 5: Access in Browser
Go to http://localhost:5000




6) Create Git Repository & Perform Git Commands
- git init
- git remote add origin <repo-url>
- git clone <repo-url>
- Modify file, then: git add ., git commit -m "msg", git push
- Fetch remote changes: git fetch
- Pull latest: git pull
- Create/switch branch: git checkout -b feature
- Reset: git reset --hard HEAD~1
- Delete branch: git branch -d feature, git push origin --delete feature




Cloud and DevOps Lab Experiments (7-10)
7) Enable AWS CloudTrail and CloudWatch, Simulate Event and View Logs
Step 1: Enable CloudTrail
- Go to AWS Console > CloudTrail > Create trail
- Choose "Apply to all regions" and an S3 bucket to store logs
Step 2: Enable CloudWatch
- Create a log group in CloudWatch Logs
Step 3: Configure CloudTrail to send logs to CloudWatch
- Under CloudTrail > Trails > Edit > Enable log delivery to CloudWatch
Step 4: Generate Simulated Event
- Log out and log back into AWS account
- Or delete a test DynamoDB table or EC2 instance
Step 5: View LogsLaunchLaunch
- Go to CloudTrail > Event history > Filter by event type (e.g., ConsoleLogin)
- Or go to CloudWatch > Log groups > View logs






8) Modify EC2 Security Group to Restrict HTTP (Port 80) to Specific IPs and Allow HTTPS (443) for AStep 1: Go to EC2 > Instances > Select your instance
Step 2: Click on Security > Security Groups > Inbound Rules > Edit
Step 3: Modify HTTP rule
- Protocol: HTTP, Port: 80
- Source: Custom (e.g., 192.168.1.0/24) - restrict to internal IPs
Step 4: Add HTTPS rule
- Protocol: HTTPS, Port: 443
- Source: Anywhere (0.0.0.0/0)
Click Save rules





9) Create IAM Policy to Allow Access to Specific S3 Buckets Only
Step 1: Go to IAM > Policies > Create policy
Step 2: Choose JSON and paste:
{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::example-bucket",
 "arn:aws:s3:::example-bucket/*"
 ]
 },
 {
 "Effect": "Deny",
 "Action": "*",
 "Resource": "*"
 }
 ]
}
Step 3: Review and create policy with a name like "S3LimitedAccess"





10) Create IAM User 'john_doe' with Specific Access
Step 1: Go to IAM > Users > Add user
Step 2: Set username to "john_doe", enable both programmatic and console access
Step 3: Attach existing policies directly:
- AmazonS3ReadOnlyAccess
- AmazonEC2FullAccess
Step 4: Review and create the user
Step 5: Sign in as john_doe using the AWS account ID login URL
Step 6: Verify Access
- Go to EC2 Dashboard > Should be able to create/terminate instances
- Go to S3 > Buckets > View files allowed, but no write/delete permission
