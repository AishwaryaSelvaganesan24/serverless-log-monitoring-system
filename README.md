# 🚀 Serverless Log Processing & Monitoring System

## 📌 Overview

This project demonstrates a serverless event-driven architecture using AWS services. It processes incoming API requests, stores logs, and triggers alerts based on conditions.

---

## 🏗️ Architecture

API Gateway → Lambda → S3 + DynamoDB → SNS → Email Alerts

---

## ⚙️ Tech Stack

* AWS Lambda
* API Gateway
* Amazon S3
* DynamoDB
* Amazon SNS
* CloudWatch

---

## 🔥 Features

* Real-time log processing
* Serverless architecture (no servers used)
* Dual storage:

  * S3 → raw logs
  * DynamoDB → structured logs
* Alert system:

  * Sends email when error detected
* Monitoring using CloudWatch logs

---

## 📊 Workflow

1. Client sends request via API Gateway
2. Lambda function processes request
3. Logs stored in:

   * Amazon S3
   * DynamoDB
4. If message contains "error":

   * SNS triggers email alert
5. CloudWatch logs used for monitoring

---

## 🧠 Key Learnings

* Event-driven architecture
* AWS serverless services integration
* IAM roles and permissions
* Debugging using CloudWatch
* Handling real-time alerts

---

## 🚀 Future Improvements

* Add dashboard (CloudWatch / Grafana)
* Add authentication
* Infrastructure as Code (Terraform / SAM)
* CI/CD pipeline

---


