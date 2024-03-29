# Technical Test: Python/API Development and DevOps

## Overview

This technical test is designed to evaluate your skills in Python/API development with an additional focus on DevOps practices, particularly containerization using Docker. You will be required to create a simple REST API and then dockerize your application.

## Submission Instructions

- **Repository:** Provide a GitHub repository link with the complete project code, Dockerfiles, docker-compose file, and any additional documentation.
- **README.md:** Ensure it clearly explains how to setup and run your application, including any prerequisites and how to execute your deployment script.

## Part 1: Python and API Development

### Objective

Create a REST API to manage a basic resource (e.g., users, tasks, products) with CRUD (Create, Read, Update, Delete) functionality.

### Requirements

#### API Specification

- **Framework:** Use Flask or FastAPI to create the API.
- **Endpoints:** Define routes for creating, retrieving, updating, and deleting items of the chosen resource.
- **Validation:** Implement validation for incoming data on creation and update endpoints.

#### Data Storage

- **Database:** Use SQLite for data storage.
- **Schema:** Design a simple schema relevant to the managed resource.

#### Testing

- **Framework:** Write unit tests for each endpoint using pytest or another testing framework.
- **Coverage:** Ensure that tests cover all API functionalities.

## Part 2: DevOps Integration

### Objective

Containerize the API application using Docker to ensure easy setup and environment consistency.

### Requirements

#### Dockerfile

- Create a Dockerfile for your application, optimizing for minimal image size.

#### Docker Compose

- **Compose File:** Create a `docker-compose.yml` file to run the API and a separate SQLite database container.
- **Volumes:** Use volumes for database data persistence and optional live code reloading.

#### Deployment Script

- **Script:** Write a script (bash or shell) to build the Docker image, run the containers, and make a test request to check if the API is up.

#### Bonus: CI/CD Integration (Optional)

- Set up a basic CI/CD pipeline (e.g., using GitHub Actions, GitLab CI/CD) to build the Docker image and run tests on commits.

## Evaluation Criteria

- **Code Quality:** Including clarity, maintainability, and best practices.
- **Functionality:** Correct CRUD operations and API behavior.
- **Error Handling:** Appropriate error reporting and handling.
- **Docker Integration:** Efficient containerization and docker-compose setup.
- **Documentation:** Clear Docker usage documentation.