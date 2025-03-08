# E-Commerce API

## continuation of https://github.com/yohanse/e-commerce-backend

## Overview
This is a RESTful API for an e-commerce platform built using Django and Django REST Framework. It provides functionality for managing products, categories, customers, orders, shopping carts, and reviews. The API is designed with scalability, security, and cost-effectiveness in mind, utilizing AWS serverless architecture with **Zappa**, **API Gateway**, **Lambda**, **RDS**, and **S3**.

## Features
- User authentication and customer management
- Product and category management
- Shopping cart and checkout process
- Order and payment status tracking
- Review and rating system
- Efficient filtering with Django Filter Backend
- Secure API endpoints with role-based access control
- Serverless deployment with **AWS Lambda**, **API Gateway**, and **RDS**

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: MySQL (AWS RDS in a private subnet)
- **Storage**: Amazon S3 (for static and media files, connected via VPC Gateway endpoint)
- **Serverless Deployment**: AWS Lambda with Zappa
- **Networking**: API Gateway (public subnet), Lambda and RDS (private subnet)
- **Security**: IAM roles, API Gateway authorization, private subnet for sensitive services

## Installation
### Prerequisites
- Python 3.8+
- PostgreSQL
- AWS CLI configured with necessary permissions
- Zappa installed (`pip install zappa`)

### Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone <repository_url>
   cd <project_directory>
   ```
2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   - Create a `.env` file and set AWS credentials, database URL, and other settings.

5. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## Deployment
### Deploying with Zappa
1. **Initialize Zappa:**
   ```sh
   zappa init
   ```
2. **Deploy to AWS:**
   ```sh
   zappa deploy dev
   ```
3. **Update deployment:**
   ```sh
   zappa update dev
   ```
4. **Set up API Gateway for S3 static files:**
   - Use API Gateway to expose S3 bucket securely
   - Configure CORS and IAM permissions

## API Endpoints
### Base
- `Base https://2h7n2ttbu6.execute-api.us-east-1.amazonaws.com/dev`

### Authentication
- `POST /auth/users/` - User login
- `POST /auth/jwt/create/` - User registration

### Products
- `GET /products/` - List all products
- `POST /products/` - Create a product (admin only)

### Categories
- `GET /categories/` - List all categories
- `POST /categories/` - Create a category (admin only)

### Cart
- `POST /carts/` - Create a shopping cart
- `POST /carts/{cart_id}/items/` - Add an item to the cart

### Orders
- `GET /orders/` - List all orders (admin only)
- `POST /orders/` - Place an order

### Reviews
- `GET /products/{product_id}/reviews/` - List product reviews
- `POST /products/{product_id}/reviews/` - Add a review (authenticated users)

## Security Measures
- **Private Subnet for Sensitive Data**: Lambda and RDS are deployed in a private subnet to prevent external access.
- **IAM Role-Based Access Control**: Permissions are granted based on roles to minimize security risks.
- **API Gateway with Authentication**: Ensures only authorized requests reach backend services.
- **S3 Secure Access**: Static files are served via API Gateway to avoid public exposure.
