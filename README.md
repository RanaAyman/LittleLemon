# LittleLemonCapstone
Meta Back-End Developer Course on Coursera

## Installation
To ensure Swagger integration for API documentation, install `drf_yasg` using:
*pipenv install drf_yasg*

## APIs
For user registration:
  - POST  /auth/users/
  - POST  /auth/token/login
  - POST  /auth/token/logout

For generating token:
  - POST /api/api-token-auth/
    
APIs without auth:
  - GET  /api/
  - GET  /api/about/
    
APIs with auth:
  - /api/menu/
  - /api/menu_item/{id}
  - GET   /api/bookings?date=2025-06-10
  - POST  /api/bookings
  - GET   /api/reservations/
