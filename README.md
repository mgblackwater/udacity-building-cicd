![Python application test with Github Actions](https://github.com/mgblackwater/udacity-building-cicd/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

# Overview

This project expose an api to allow user to get the prediction of housing price based on pre-trained model.

The project source code is maintained on github repository and using git action to run linting and testing automatically upon checking into the source code.

For the deployment of the project, it is automated by using azure devops pipeline to deploy directly to azure app service when the code has checked into the main branch.

The project uses - Flask and scikit-learn to provide ML API and there is no frontend UI for the enduser to directly get the prediction.

## Project Plan

Project Planning can be found on this google spreadsheet - https://docs.google.com/spreadsheets/d/1uivvu4tP8pS4hrBvUzjOVptkkaY-F9Z_h72sHcPnbVA/edit?usp=sharing

Build status of the projecte can be tracked here - https://trello.com/b/nYpH9FUr/simple-project-board

## Instructions

![Architecutre](architecture-diagram.png)

To host the application on azure to try out, please follow below steps -

1. Clone the repository

```
git clone git@github.com:mgblackwater/udacity-building-cicd.git
```

![Clone Github](Screenshot-git-clone.png)

2. Prepare the virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

2. Execute make all script to install dependencies, lint and test

```
make all
```

![Make all](Screenshot-make-all.png)
![Test Passsed](Screenshot-test-passed.png)

3. Implement CI with Github Action

Follow steps below to setup CI

- Successful deploy of the project in Azure Pipelines. [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

- Running Azure App Service from Azure Pipelines automatic deployment

- Successful prediction from deployed flask app in Azure Cloud Shell. [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
  The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

- Output of streamed log files from deployed application

>

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo

<TODO: Add link Screencast on YouTube>
