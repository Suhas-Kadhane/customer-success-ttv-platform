# API Design

## Overview

The Customer Success TTV Platform exposes REST APIs to enable communication between the React frontend and the FastAPI backend. All APIs exchange data in JSON format over HTTPS and follow RESTful design principles.

## API Design Principles

- RESTful architecture
- JSON request and response format
- Stateless communication
- JWT-based authentication
- Consistent endpoint naming
- Standard HTTP status codes
- Version-ready endpoint structure

## Base URL

```
/api/v1
```

## Core Resources

- Customers
- Users
- Onboarding Plans
- Milestones
- Tasks
- Health Scores
- Activity Logs

## Sample Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /api/v1/customers | Retrieve all customers |
| GET | /api/v1/customers/{id} | Retrieve a specific customer |
| POST | /api/v1/customers | Create a new customer |
| PUT | /api/v1/customers/{id} | Update a customer |
| DELETE | /api/v1/customers/{id} | Delete a customer |
| GET | /api/v1/onboarding-plans | Retrieve onboarding plans |
| GET | /api/v1/health-scores | Retrieve customer health scores |

## Authentication

Protected endpoints require a valid JWT access token.

Example:

```
Authorization: Bearer <JWT_TOKEN>
```

## Standard HTTP Methods

| Method | Purpose |
|---------|----------|
| GET | Retrieve data |
| POST | Create data |
| PUT | Update existing data |
| DELETE | Remove data |

## Standard Response Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Resource Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Resource Not Found |
| 500 | Internal Server Error |

## Future APIs

Future releases will expose APIs for:

- AI Recommendations
- Salesforce Integration
- Slack Notifications
- Email Automation

## Summary

The API design provides a scalable and consistent communication layer between the frontend and backend while remaining extensible for future platform capabilities.