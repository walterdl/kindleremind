# Kindleremind

Kindleremind helps avid readers revisit their favorite book highlights. It uses push notifications to remind users of the highlights they've taken from books on their Kindle device.

### Features
- Highlight Reminders: Users receive push notifications for their Kindle book highlights.
- Customizable Schedule: Users can set preferred times to receive reminders.
- CLI for Easy Upload: The CLI enables straightforward uploading of Kindle highlights through a user-friendly interface.

### Stack

- Mobile App: React Native, TypeScript, Firebase Cloud Messaging
- CLI Program: Python
- Server System: Python, MongoDB, AWS Lambda, AWS API Gateway, [Amazon Cognito](https://aws.amazon.com/es/cognito/), [Amazon Route 53](https://aws.amazon.com/es/route53/), [ACM](https://aws.amazon.com/es/certificate-manager/), [SSM Parameter Store](https://aws.amazon.com/es/systems-manager/), [EventBridge Scheduler](https://aws.amazon.com/eventbridge/scheduler/), SNS
- Unit testing: [Pytest](https://docs.pytest.org/en/7.4.x/)
- IaC: [AWS CDK](https://aws.amazon.com/es/cdk/)

### Mobile App Usage

#### Registration

Upon opening the app, users are prompted to sign up by providing an email address and creating a secure password. A verification code is sent to the user's email address. Users must enter this code into the app to verify their account and activate it.

<img src="https://github.com/walterdl/kindleremind/assets/26971414/fe5aa8cd-4c4b-438c-a8a7-c9989ebe9983" width="281" height="577"> <img src="https://github.com/walterdl/kindleremind/assets/26971414/06d5983a-9ddc-45df-84d2-f4b9af413460" width="281" height="577">

#### Managing API Keys
Once signed in, users can create and manage API keys, which authenticate requests from the CLI tool:

1. API Key Section: Users navigate to the 'API Keys' section within the app.
2. Generation of API Key: The app provides an option to generate a new API key.
3. API Key Utilization: Users are instructed to securely copy the API key for use with the CLI tool when uploading their Kindle highlights.

<img src="https://github.com/walterdl/kindleremind/assets/26971414/8c4fb718-ca67-4584-8d77-cde5b692eca1" width="281" height="577"> <img src="https://github.com/walterdl/kindleremind/assets/26971414/01b5a7aa-26ad-45c9-a98c-4e87755a052f" width="281" height="577">

#### Setting Up Reminder Schedules
The app allows users to configure schedules for receiving highlight reminders:

1. Schedule Management: Within the 'Schedules' section, users can manage their reminder times.
2. Creating a Schedule: By selecting 'Add New,' users can set up a new reminder schedule, specifying preferred days and times.
3. Modifying Schedules: The app also permits users to edit or remove existing schedules as needed.

<img src="https://github.com/walterdl/kindleremind/assets/26971414/eef0a74a-39b5-49ef-8841-482848b5bff1" width="281" height="577"> <img src="https://github.com/walterdl/kindleremind/assets/26971414/4d8d5013-4faa-4c59-a6c5-a8526e09d09a" width="281" height="577">

#### Receiving Push Notifications

With schedules configured, the app manages the delivery of reminders. At predetermined times based on the schedules, the app sends push notifications containing a random highlight to the user.

<img src="https://github.com/walterdl/kindleremind/assets/26971414/20781e9a-9279-43bd-8d21-28462e2e0527" width="281" height="577"> <img src="https://github.com/walterdl/kindleremind/assets/26971414/33c31146-c21c-490c-a2d9-d5615f2b042e" width="281" height="577">

### CLI Program Usage

#### Prerequisites

Before using the CLI program, ensure that:

- You have generated an API key using the mobile app.
- You know the URL to the API Gateway provided by the Kindleremind backend.
- You have located the clippings file on your Kindle device. Usually, it is located in the file "My Clippings.txt" in the root of the Kindle directory.

Also, note that only English and Spanish are supported. Kindle clipping files with other languages break the CLI.

#### Syncing Highlights
To upload the Kindle highlights, use the sync command with the appropriate parameters:

```
./kindleremind sync \
   --server-url <URL to the API Gateway> \
   --api-key <API Key created from the mobile app> \
   --file <Absolute or relative path to the clippings file in the Kindle device>
```

### Architecture

![kindleremind](https://github.com/walterdl/kindleremind/assets/26971414/7e0b1144-73d3-49a7-a1fe-4d46fdda3003)

### User Interaction
Users interact with the system through two main interfaces:

- CLI (Command Line Interface): Allows users to upload Kindle highlights.
- Mobile App: Enables users to sign up/sign in, manage API keys (used to authenticate CLI requests), receive push notifications, and manage their reminder schedules. Requests are secured with JWT authorization after successful sign-in with Cognito. The authentication view is based on the [Authenticator component](https://ui.docs.amplify.aws/react-native/connected-components/authenticator) of Amplify UI.

### Backend
- API Gateway: All backend HTTP requests are routed through the API Gateway, which provides a secure entry point for the services.
- AWS Cognito: Manages user authentication for the system. Doesn't provide a hosted page to authenticate since it is performed on the mobile app. Self-service sign-up is activated so any user with a verifiable email address can join the system.

### Data Management
- MongoDB: Hosts the database that stores user highlights, and schedules.
- AWS Systems Manager Parameter Store: Securely manages system secrets and configuration data such as database credentials.

### Notifications
- EventBridge Scheduler: Orchestrates the timing of push notification delivery based on user-configured schedules.
- SNS: AWS Simple Notification Service topics are used to manage dispatch scheduled executions of notification senders. The usage of an SNS topic in front of EventBridge Scheduler allows the system to leverage the fan-out pattern, where a single scheduled message can trigger multiple sending implementations such as Email or SMS senders.
- Firebase Cloud Messaging: Integrated to deliver push notifications to the mobile app.

### Network
- Route 53: AWS DNS web service that routes user requests to the infrastructure.
- ACM (AWS Certificate Manager): Manages TLS certificates for secure communication. Used by API Gateway to implement HTTPS with a custom domain.

### Backend Deployment and Local Development

Deploying the backend of Kindleremind requires a combination of AWS Cloud Development Kit (CDK) automation and manual resource setup. Below is the guide for the initial deployment and subsequent local development setup.

#### Initial Backend Deployment

Before deploying the backend using AWS CDK, certain resources must be manually created due to security considerations and cost management:

1. MongoDB Database Creation: Utilize a service like MongoDB Atlas to set up the database instance.
2. Firebase Cloud Messaging: Manually create a Firebase project to obtain the private key for push notifications.
3. Route53 Hosted Zone: Create the Hosted Zone manually to manage DNS records, if not using an existing zone.
4. AWS Systems Manager (SSM) Parameters: After obtaining the necessary details from steps 1-3, create the SSM parameters:
   - MongoDB Connection URI: Store as `/kindleremind/mongo-atlas/connection-uri`.
   - Firebase Private Key: Store as `/kindleremind/firebase/service-account/private-key`.
   - API Key: Generate a random UUID v4 and store it as `/kindleremind/api-key` for local development authentication (feature not yet implemented).

#### Deploying with AWS CDK

Once the manual resources are set up, proceed with the CDK deployment:

1. Install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and configure its credentials and permissions.
2. Have the [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) installed.
3. `cd server/infrastructure/cdk`.
4. `npm install` to install the CDK dependencies.
5. `cdk bootstrap` to prepare your AWS environment for the CDK deployment.
6. `cdk deploy` to deploy the backend stack to the AWS account.

#### Starting Backend Locally

To run the Kindleremind backend locally after the first deployment:

1. Create a copy of the file `.env.example` in the root of the project and complete the value of the variables using the deployed cloud resources.
2. Install [pipenv](https://pipenv-es.readthedocs.io/es/latest/):
3. `pipenv shell` to start a session with the correct Python version for the project. Also, this isolates the project dependencies from the global scope of the OS.
4. `pipenv sync -d` to install the backend app dependencies.
5. `pipenv run local` to execute the local web server which acts as the entry point to the HTTP endpoints of Kindleremind API. This starts the web server at port 5001.
6. Endpoint paths and HTTP methods can be found in `server/infrastructure/lambdas.yml`. The payload for POST and PUT operations do not have documentation yet but the source code of the mobile app can be used to discover this.

### Starting Mobile App Locally

The mobile app is bootstrapped with bare react-native. Only Android is supported, although the project can be adapted for iOS by just setting up the app dependencies. Details about how to run it locally can be found in its README file: `clients/mobile-app/README.md`. But besides such vendor documentation the following steps must be taken into account:

1. `cd clients/mobile-app`
2. Generate Keystore file: The guide [Publishing to Google Play Store](https://reactnative.dev/docs/signed-apk-android) from the official react-native docs can be used to generate the Keystore file.
3. Generate [google-services.json](https://rnfirebase.io/#generating-android-credentials) file.
4. Create a `.env` file in the root of the mobile app project using environment variable names from the `.env.example`.
5. With the `.env` file filled up with proper values taken from the backend resources and 3rd party integrations such as Firebase, the app can be run with `npm run android`.

### Starting CLI Locally

1. `cd clients/cli`
2. `pipenv shell` to start a virtual environment.
3. `pipenv sync -d` to install all dependencies including dev ones.
4. Create a `.env` file in the root of the CLI project using environment variable names from the `.env.example`. Special attention to the `PYTHONPATH`: prepend the absolute path of the `src` folder. E.g. supposing the project is cloned in the path `/Users/myuser/kindleremind` the value of `PYTHONPATH` becomes `/Users/myuser/kindleremind/clients/cli/src:$PYTHONPATH`.
5. Move to the source code directory with `cd src/kindleremind`. Then run the program with `python main.py`.

### Unit tests

Unit tests are present in the CLI program and the backend system. Both are run with the command `pytest`. Also, the command `ptw` from the package `pytest-watch` can be used to start tests in watch mode.
