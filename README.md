# S3 Dashbard

## Purpose

Getting familier with S3 service by building a custom CMS for interacting with the service,
in which the functionalities are similar to [AWS console](https://aws.amazon.com/console/), such as creating buckets, uploading or downloading files, etc.

> About S3

A storage service, with 2 interactable entities:
- Bucket: a containers for files, which is physically located at a specific region.
- Object: a file.

> Tools for interacting with S3 serivce
- CLI: an interactive command line interface, handy for daily usage but not for implementing applications.
- API: an web interface, which is very low level and should not be used directly.
- SDK: an abstraction of API, use this method for implementing applications.

> Application flows
- EC2 flow
```
App <--------> EC2 instance <--------> S3

Using SDK to develop API hosted on (a) servers for serving client apps.
Pros:
    - Greatest level of controls.
    - Client simplicity (only need to consume API).
Cons:
    - Costly (since its use an EC2 instance).
```

- Lambda flow
```
App <--------> Lambda function <--------> S3

Using SDK to develop lambda functions, hosted via an API gateway or triggered via SQS.
Pros:
    - May reduce costs.
    - Reduce workload of server.
Cons:
    - Increase complexity of testing & deploying.
```

- Client direct flow
```
APP <--------> AWS Javascript SDK <-------> S3

Client talks directly to S3 service.
Pros:
    - Simple for implementing.
    - Reduce workload of server.
Cons:
    - Need to config CORS manually on aws console.
    - Security concerns.
    - Duplication of implementations if number of client type increase, such as Web, mobile, etc.
```
## Installation

> Setting environment variables

```
cp ./py-server/.env.example ./py-server/.env
```

> Build project

```
docker compose build
```

> Run development server

```
docker compose up
```

> Debugging

For debugging, please run another server instance outside of the Docker containers (since debugger cannot run inside containers).

> About Localstack

Localstack is a local service which acts similar to actuals AWS services. Hence, using localstack first for reducing actual AWS service costs.

For interacting by CLI, use **awslocal** instead of **aws**

## Documentation

- [Official docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [AWS python SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
- [AWS node SDK](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html)
- [Localstack](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html)


## Workflow

- Use [Fork flow](https://gist.github.com/Chaser324/ce0505fbed06b947d962)
- Start working by creating an Github issues

## Progress

- [ ] client
  - [ ] bucket
    - [ ] create a bucket
    - [ ] delete a bucket
    - [ ] change bucket settings
  - [ ] file
    - [ ] list files (thumbnails only) by buckets
    - [ ] load single file (full size)
    - [ ] upload single file
    - [ ] upload multiple files
    - [ ] service: upload file via server
    - [ ] service: upload file directly
- [ ] py-server
  - [x] CRUD bucket
  - [x] CRUD file
  - [x] convert s3 client to s3 resrource (no need, some operations is performed in batch with s3 client)
  - [ ] provide cache layer
  - [x] integrate with actual service
  - [ ] add tests
- [ ] node-server
  - [ ] CRUD bucket
  - [ ] CRUD file
  - [ ] provide cache layer
  - [ ] integrate with actual service
  - [ ] add tests
- [ ] env
  - [x] development
  - [ ] production
  - [ ] setup CI
  - [ ] setup CD

## TIL

> 2021/12/5

- To call a container from another container in the same network, use `http://host.docker.internal:{port-of-other-service}/`.
- To add & read environment variable in python, use package `python-dotenv`.

> 2021/12/6

- Access point is created to interact with a specified bucket, hence not suitable for bucket manipulation (but buckets are mostly manually created).
- Do not provide url for s3 client (or resource) if its connect directly to actual service  
