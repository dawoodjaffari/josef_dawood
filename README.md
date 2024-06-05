Sure, here's a basic README file for your Flask application:

```markdown
# Flask Blog API

This is a RESTful API built with Flask for managing blog posts, users, comments, and categories.

## Getting Started

### Prerequisites

- Python 3.x
- SQLite

### Installing

1. Clone the repository:

   ```bash
   git clone https://github.com/sachinda96/blog-back-end.git
   ```

2. Navigate to the project directory:

   ```bash
   cd blog-back-end
   ```

3. Install the required Python packages:

   ```bash
   pip install Flask Flask-CORS
   ```

### Running the Application

1. Run the Flask application:

   ```bash
   python app.py
   ```

   The application will start running on `http://localhost:5000`.

## Endpoints

- **GET /users**: Retrieve all users or create a new user.
- **GET /users/<int:user_id>**: Retrieve, update, or delete a specific user.
- **GET /blogs**: Retrieve all blogs or create a new blog.
- **GET /blogs/<int:blog_id>**: Retrieve, update, or delete a specific blog.
- **GET /comments**: Retrieve all comments or create a new comment.
- **GET /comments/<int:comment_id>**: Retrieve, update, or delete a specific comment.
- **GET /categories**: Retrieve all categories or create a new category.
- **GET /categories/<int:category_id>**: Retrieve, update, or delete a specific category.
- **GET /blogs/category/<int:category_id>**: Retrieve blogs by category.
- **GET /comments/blog/<int:blog_id>**: Retrieve comments by blog.
- **GET /blogs/category/<int:category_id>/<int:page_number>/<int:per_page>**: Retrieve paginated blogs by category.
- **GET /blogs/page/<int:page_number>/<int:per_page>**: Retrieve paginated blogs.

## Authentication

- **POST /register**: Register a new user.
- **POST /login**: Login with username and password.

## Database

![bloger](https://github.com/sachinda96/blog-back-end/assets/33303027/1bb248f4-4bc2-41d4-93ee-940fe8d13a99)


This application uses SQLite as the database backend. The database file (`blog-database.db`) will be created automatically when the application is run for the first time.

## Authors

- Your Name - [@yourusername](https://github.com/yourusername)

