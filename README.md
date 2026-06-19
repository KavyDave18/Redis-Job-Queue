# Redis Background Job Queue

A FastAPI and Redis based background job processing system implementing the Producer-Consumer pattern. The project demonstrates how tasks can be queued, processed asynchronously by workers, and tracked through different lifecycle states.

---

## Overview

In many modern applications, certain operations take significant time to complete. Running these tasks directly inside API requests can increase response times and reduce system performance.

This project solves that problem using Redis as a message queue and FastAPI as the API layer. Jobs are submitted through REST endpoints, stored inside a Redis queue, processed by background workers, and their status can be tracked throughout execution.

The architecture follows the Producer-Consumer model commonly used in distributed systems, AI pipelines, video processing systems, notification systems, and large-scale backend applications.

---

## Features

* FastAPI REST API
* Redis Queue Implementation
* Background Worker Processing
* Producer-Consumer Architecture
* UUID-Based Job Tracking
* Job Status Monitoring
* Result Storage
* Failed Job Handling
* Asynchronous Processing
* Modular Backend Architecture

---

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Queue System

* Redis

### Development Tools

* Git
* GitHub
* Virtual Environment (venv)

---

## System Architecture

```text
Client
   │
   ▼
POST /jobs
   │
   ▼
Redis Queue
   │
   ▼
Background Worker
   │
   ▼
PROCESSING
   │
   ▼
COMPLETED / FAILED
   │
   ▼
Result Stored In Redis
```

---

## Producer-Consumer Workflow

### Producer

The API acts as a Producer.

```text
Client Request
      ↓
Create Job
      ↓
Store Status = PENDING
      ↓
Push To Redis Queue
```

### Consumer

The Worker acts as a Consumer.

```text
Read Job From Queue
      ↓
PROCESSING
      ↓
Execute Task
      ↓
COMPLETED / FAILED
```

---

## Job Lifecycle

Every job passes through the following states:

```text
PENDING
   ↓
PROCESSING
   ↓
COMPLETED
```

If an error occurs:

```text
PENDING
   ↓
PROCESSING
   ↓
FAILED
```

---

## API Endpoints

### Create Job

```http
POST /jobs
```

Request:

```json
{
    "task": "transcribe_video"
}
```

Response:

```json
{
    "job_id": "a1b2c3d4",
    "status": "PENDING"
}
```

---

### Check Job Status

```http
GET /jobs/{job_id}
```

Response While Processing:

```json
{
    "job_id": "a1b2c3d4",
    "status": "PROCESSING",
    "result": null
}
```

Response After Completion:

```json
{
    "job_id": "a1b2c3d4",
    "status": "COMPLETED",
    "result": "Task 'transcribe_video' completed successfully"
}
```

Response After Failure:

```json
{
    "job_id": "a1b2c3d4",
    "status": "FAILED",
    "result": "Simulated Failure"
}
```

---

## Project Structure

```text
redis-job-queue/

app/
│
├── config/
│   └── redis.py
│
├── models/
│   └── schemas.py
│
├── routes/
│   └── jobs.py
│
├── services/
│   ├── queue_service.py
│   └── worker_service.py
│
├── workers/
│   └── worker.py
│
└── main.py

tests/

requirements.txt
README.md
```

---

## Key Redis Concepts Used

### LPUSH

Adds jobs into the queue.

```text
Job Created
    ↓
LPUSH
    ↓
Redis Queue
```

### BRPOP

Worker waits for incoming jobs and consumes them.

```text
Worker Waiting
      ↓
BRPOP
      ↓
Job Received
```

### SET / GET

Used for storing:

* Job Status
* Job Results
* 
---

### Create Job Endpoint

<img width="1058" height="431" alt="image" src="https://github.com/user-attachments/assets/d06f6e0d-ff5f-4f16-bb61-45dc2448a09a" />


```text
docs/screenshots/create-job.png
```

---

### Job Processing

<img width="1052" height="622" alt="image" src="https://github.com/user-attachments/assets/4c4b9e9b-1d12-4387-81a8-cf2cbb7587c3" />

```text
docs/screenshots/job-processing.png
```

---

### Job Completed

<img width="1066" height="620" alt="image" src="https://github.com/user-attachments/assets/34513e5d-82dd-42c2-b9be-78e50d9db44a" />

```text
docs/screenshots/job-completed.png
```

---

## Installation

Clone Repository

```bash
git clone <repository-url>
```

Move Into Project

```bash
cd redis-job-queue
```

Create Virtual Environment

```bash
python3 -m venv venv
```

Activate Environment

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Start Redis

```bash
redis-server
```

Start FastAPI

```bash
uvicorn app.main:app --reload
```

Start Worker

```bash
python3 -m app.workers.worker
```

Open Swagger

```text
http://127.0.0.1:8000/docs
```

---

## Learning Outcomes

This project helped me understand:

* Redis Fundamentals
* Message Queues
* Producer-Consumer Pattern
* Background Workers
* Asynchronous Processing
* FastAPI Development
* API Design
* Job Status Management
* Result Storage
* Error Handling
* Backend System Architecture

---

## Future Improvements

* Multiple Worker Support
* Docker Deployment
* Celery Integration
* Retry Mechanism
* Queue Monitoring Dashboard
* Distributed Worker Architecture
* Task Scheduling

---

## Author

Kavy Dave

B.Tech Computer Science Engineering Student

Interested in Backend Systems, Machine Learning, AI Infrastructure, and Scalable Software Engineering.
