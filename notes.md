# Project Plan for RESTful Web Service with Django

## Week 1

### Day 1: Project Setup and Initial Planning (DONE)

- **Task**: Set up the project repository and initial environment.
  - Create a new repository on GitHub. (DONE)
  - Set up a virtual environment and install Django. (DONE)
  - Initialize a new Django project and create a `.gitignore` file. (DONE)
  - Create an initial README file with project description and goals.
- **PR**: Initial project setup.

### Day 2: Basic Django Setup (DONE)

- **Task**: Set up the Django project structure.
  - Create a new Django app. (DONE)
  - Set up initial configurations (settings.py, URLs, etc.). (DONE)
  - Create models for the dataset (based on your chosen domain). (DONE)
  - Create and apply initial migrations. (DONE)
- **PR**: Basic Django app setup.

### Day 3: Database Design and Seed Script (DONE)

- **Task**: Design the database and create a data loading script.
  - Finalize the database schema. (DONE)
  - Create a script to load data from CSV files into the database. (DONE)
  - Add the `requirements.txt` file with necessary dependencies. (DONE)
- **PR**: Database design and seed script.

### Day 4: RESTful Endpoints - Part 1

- **Task**: Implement the first set of RESTful endpoints.
  - Create views and serializers for initial endpoints (e.g., GET requests).
  - Implement URL routing for these endpoints.
  - Test the endpoints using tools like Postman or curl.
- **PR**: Initial RESTful endpoints.

### Day 5: RESTful Endpoints - Part 2

- **Task**: Implement the remaining RESTful endpoints.
  - Create views and serializers for the remaining endpoints (e.g., POST, DELETE).
  - Implement URL routing for these endpoints.
  - Test the endpoints using tools like Postman or curl.
- **PR**: Complete RESTful endpoints.

### Day 6: Unit Testing

- **Task**: Write unit tests for all implemented endpoints.
  - Use Django's testing framework to create test cases for each endpoint.
  - Ensure tests cover various scenarios and edge cases.
- **PR**: Unit tests for RESTful endpoints.

### Day 7: Code Review and Refactoring

- **Task**: Review and refactor code.
  - I need to reduce the database entries to be below 10,000 entries
  - Perform a thorough code review to ensure code quality.
  - Refactor code for better readability and maintainability.
  - Ensure adherence to PEP8 standards.
- **PR**: Code review and refactoring.

## Week 2

### Day 8: Report Writing - Part 1

- **Task**: Start writing the project report.
  - Document the dataset and its significance.
  - Describe the endpoints and their functionality.
  - Explain how the application requirements have been met.
- **PR**: Initial report draft.

### Day 9: Report Writing - Part 2

- **Task**: Continue writing the project report.
  - Discuss the application of Django and Django REST framework.
  - Include critical evaluation of the work/approach.
  - Document the development environment and instructions for running the application.
- **PR**: Complete report draft.

### Day 10: Video Demonstration

- **Task**: Create a video demonstrating the application.
  - Record the process of unzipping the application, installing dependencies, and deploying the application.
  - Show how to populate the database using the seeding script.
  - Demonstrate all RESTful endpoints.
  - Explain the dataset choice, endpoints, and database design.
- **PR**: Video demonstration.

### Day 11: Deployment (Optional for Bonus Points)

- **Task**: Deploy the application to a cloud service (e.g., AWS, Digital Ocean).
  - Set up an instance and deploy the Django application.
  - Provide details in the report and video.
- **PR**: Deployment to cloud service.

### Day 12: Final Review and Testing

- **Task**: Perform a final review and testing of the entire application.
  - Ensure all functionalities work as expected.
  - Double-check all documentation and instructions.
  - Validate unit tests and application deployment.
- **PR**: Final review and testing.

### Day 13: Submission Preparation

- **Task**: Prepare submission materials.
  - Compress the Django application and related files into a ZIP file.
  - Ensure all deliverables (D1-D7) are included.
  - Prepare a clean and final version of the report and video.
- **PR**: Submission materials preparation.

### Day 14: Final Submission

- **Task**: Submit the project.
  - Submit the compressed ZIP file.
  - Upload the report and video.
  - Ensure all links and instructions are clear and accessible.
- **PR**: Final submission.

## References

- <https://github.com/rdswyc>

- Retrieve all products containing a specific ingredient and sort them by the concentration of that ingredient:

Endpoint: GET /products/ingredient/{ingredient_id}/sorted_by_concentration/
Description: This endpoint returns all products that contain a specific ingredient, sorted by the concentration of that ingredient in descending order.
Complexity: Involves joining the Product, ProductIngredient, and Ingredient tables, and sorting based on a field in the intermediary table.


- Get detailed information of a product including its ingredients and their concentrations:

Endpoint: GET /product/{product_id}/details/
Description: This endpoint retrieves detailed information about a product, including its ingredients and their respective concentrations.
Complexity: Requires nested serialization to include related data from ProductIngredient and Ingredient tables.

- Add a new product along with its ingredients and their concentrations:

Endpoint: POST /products/add/
Description: This endpoint allows adding a new product along with its ingredients and their concentrations. The request body should include product details and a list of ingredients with their concentrations.
Complexity: Involves handling nested data in the request and performing multiple inserts into different tables.
Serialization: Uses serialization to validate and save the nested data.

- Delete all products that do not belong to any brand or line and are not vegan:

Endpoint: DELETE /products/unbranded_unvegan/
Description: This endpoint deletes all products that are not associated with any brand or line and are not marked as vegan.
Complexity: Involves conditional filtering and bulk deletion operations.

- Update a product’s information:

Endpoint: PUT /product/{product_id}/update/
Description: This endpoint updates the information of an existing product. The request body should include the updated details of the product.
Complexity: Involves updating fields of an existing product and handling partial updates if necessary.
Serialization: Uses serialization to validate and update the product data. 
