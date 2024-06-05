import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def connect_to_db():
    conn = sqlite3.connect('blog-database.db')
    return conn

# Database operations
def execute_query(query, params=None, fetchone=False):
    conn = connect_to_db()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    if fetchone:
        result = cursor.fetchone()
    else:
        result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

# Users
@app.route('/users', methods=['GET', 'POST', 'PUT'])
def users():
    if request.method == 'GET':
        users = execute_query("SELECT * FROM User")
        return jsonify(users)
    elif request.method == 'POST':
        data = request.json
        print(data)
        try:
            execute_query("INSERT INTO User (email, username, password, firstname, lastname, isActive) VALUES (?, ?, ?, ?, ?, ?)", (data['email'], data['username'], data['password'], data['firstname'], data['lastname'], data['isActive']))
            return jsonify({'message': 'User created successfully'}), 201
        except sqlite3.IntegrityError:
            return jsonify({'error': 'User already exists'}), 400
    elif request.method == 'PUT':
        data = request.json
        user_id = data.get('id')
        if not user_id:
            return jsonify({'error': 'Missing id in request'}), 400
        try:
            execute_query("UPDATE User SET email=?, username=?, password=?, firstname=?, lastname=?, isActive=? WHERE userId=?", (data['email'], data['username'], data['password'], data['firstname'], data['lastname'], data['isActive'], user_id))
            return jsonify({'message': f'User with ID {user_id} updated successfully'}), 200
        except sqlite3.IntegrityError:
            return jsonify({'error': f'Update failed for User with ID {user_id}'}), 400


@app.route('/users/<int:user_id>', methods=['GET','DELETE'])
def user(user_id):
    if request.method == 'GET':
        user = execute_query("SELECT * FROM User WHERE userId=?", (user_id,), fetchone=True)
        if user:
            return jsonify(user)
        else:
            return jsonify({'error': 'User not found'}), 404
    elif request.method == 'DELETE':
        try:
            execute_query("DELETE FROM User WHERE userid=?", (user_id,))
            return jsonify({'message': f'User with ID {user_id} deleted successfully'}), 200
        except sqlite3.IntegrityError:
            return jsonify({'error': f'Delete failed for User with ID {user_id}'}), 400
 
# Blogs
@app.route('/blogs', methods=['GET', 'POST', 'PUT'])
def blogs():
    if request.method == 'GET':
        query = """
    SELECT b.*, c.name, u.firstName, u.lastName
    FROM Blog AS b
    INNER JOIN Category AS c ON b.categoryId = c.categoryId
    INNER JOIN User AS u ON b.userId = u.userId
"""     
         
        blogs = execute_query(query)
        return jsonify(blogs)
    elif request.method == 'POST':
        data = request.json
        try:
            execute_query("INSERT INTO Blog (title, mainImage, description, createDate, categoryId, userId) VALUES (?, ?, ?, ?, ?, ?)", (data['title'], data['mainImage'], data['description'], data['createDate'], data['categoryId'], data['userId']))
            return jsonify({'message': 'Blog created successfully'}), 201
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Blog creation failed'}), 400
    elif request.method == 'PUT':
        data = request.json
        blog_id = data.get('blogId')
        if not blog_id:
            return jsonify({'error': 'Missing blogId in request'}), 400
        try:
            execute_query("UPDATE Blog SET title=?, mainImage=?, description=?, createDate=?, categoryId=?, userId=? WHERE blogId=?", (data['title'], data['mainImage'], data['description'], data['createDate'], data['categoryId'], data['userId'], blog_id))
            return jsonify({'message': f'Blog with ID {blog_id} updated successfully'}), 200
        except sqlite3.IntegrityError:
            return jsonify({'error': f'Update failed for Blog with ID {blog_id}'}), 400

@app.route('/blogs/<int:blog_id>', methods=['GET', 'DELETE'])
def blog(blog_id):
    if request.method == 'GET':
        blog = execute_query("SELECT * FROM Blog WHERE blogId=?", (blog_id,), fetchone=True)
        if blog:
            return jsonify(blog)
        else:
            return jsonify({'error': 'Blog not found'}), 404
    elif request.method == 'DELETE':
        try:
            execute_query("DELETE FROM Blog WHERE blogId=?", (blog_id,))
            return jsonify({'message': f'Blog with ID {blog_id} deleted successfully'}), 200
        except sqlite3.IntegrityError:
            return jsonify({'error': f'Delete failed for Blog with ID {blog_id}'}), 400

# Comments
@app.route('/comments', methods=['GET', 'POST', 'PUT'])
def comments():
    if request.method == 'GET':
        comments = execute_query("SELECT * FROM Comment")
        return jsonify(comments)
    elif request.method == 'POST':
        data = request.json
        try:
            execute_query("INSERT INTO Comment (comment, rating, commentDate, username, email, blogId) VALUES (?, ?, ?, ?, ?, ?)", (data['comment'], data['rating'], data['commentDate'], data['username'], data['email'], data['blogId']))
            return jsonify({'message': 'Comment created successfully'}), 201
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Comment creation failed'}), 400
    elif request.method == 'PUT':
        data = request.json
        comment_id = data.get('commentId')
        if not comment_id:
            return jsonify({'error': 'Missing commentId in request'}), 400
        try:
            execute_query("UPDATE Comment SET comment=?, rating=?, commentDate=?, username=?, email=?, blogId=? WHERE commentId=?", (data['comment'], data['rating'], data['commentDate'], data['username'], data['email'], data['blogId'], comment_id))
            return jsonify({'message': f'Comment with ID {comment_id} updated successfully'}), 200
        except sqlite3.IntegrityError:
            return jsonify({'error': f'Update failed for Comment with ID {comment_id}'}), 400


@app.route('/comments/<int:comment_id>', methods=['GET', 'PUT', 'DELETE'])
def comment(comment_id):
    if request.method == 'GET':
        comment = execute_query("SELECT * FROM Comment WHERE commentId=?", (comment_id,), fetchone=True)
        if comment:
            return jsonify(comment)
        else:
            return jsonify({'error': 'Comment not found'}), 404
    elif request.method == 'PUT':
        data = request.json
        try:
            execute_query("UPDATE Comment SET comment=?, rating=?, commentDate=?, username=?, email=?, blogId=? WHERE commentId=?", (data['comment'], data['rating'], data['commentDate'], data['username'], data['email'], data['blogId'], comment_id))
            return jsonify({'message': f'Comment with ID {comment_id} updated successfully'}), 200
        except sqlite3.IntegrityError:
            return jsonify({'error': f'Update failed for Comment with ID {comment_id}'}), 400
    elif request.method == 'DELETE':
        try:
            execute_query("DELETE FROM Comment WHERE commentId=?", (comment_id,))
            return jsonify({'message': f'Comment with ID {comment_id} deleted successfully'}), 200
        except sqlite3.IntegrityError:
            return jsonify({'error': f'Delete failed for Comment with ID {comment_id}'}), 400

@app.route('/categories', methods=['GET', 'POST', 'PUT'])
def categories():
    if request.method == 'GET':
        categories = execute_query("SELECT * FROM Category")
        return jsonify(categories)
    elif request.method == 'POST':
        data = request.json
        try:
            execute_query("INSERT INTO Category (name) VALUES (?)", (data['name'],))
            return jsonify({'message': 'Category created successfully'}), 201
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Category creation failed'}), 400
    elif request.method == 'PUT':
        data = request.json
        category_id = data.get('id')
        if not category_id:
            return jsonify({'error': 'Missing categoryId in request'}), 400
        try:
            execute_query("UPDATE Category SET name=? WHERE categoryId=?", (data['name'], category_id))
            return jsonify({'message': f'Category with ID {category_id} updated successfully'}), 200
        except sqlite3.IntegrityError:
            return jsonify({'error': f'Update failed for Category with ID {category_id}'}), 400


@app.route('/categories/<int:category_id>', methods=['GET', 'PUT', 'DELETE'])
def category(category_id):
    if request.method == 'GET':
       
        category = execute_query("SELECT * FROM Category WHERE categoryId=?", (category_id,), fetchone=True)
        if category:
            return jsonify(category)
        else:
            return jsonify({'error': 'Category not found'}), 404
    elif request.method == 'PUT':
        data = request.json
        try:
            execute_query("UPDATE Category SET name=? WHERE categoryId=?", (data['name'], category_id))
            return jsonify({'message': f'Category with ID {category_id} updated successfully'}), 200
        except sqlite3.IntegrityError:
            return jsonify({'error': f'Update failed for Category with ID {category_id}'}), 400
    elif request.method == 'DELETE':
        try:
            execute_query("DELETE FROM Category WHERE categoryId=?", (category_id,))
            return jsonify({'message': f'Category with ID {category_id} deleted successfully'}), 200
        except sqlite3.IntegrityError:
            return jsonify({'error': f'Delete failed for Category with ID {category_id}'}), 400
        
@app.route('/blogs/category/<int:category_id>', methods=['GET'])
def blogs_by_category(category_id):
    
    query = """
    SELECT b.*, c.name, u.firstName, u.lastName
    FROM Blog AS b
    INNER JOIN Category AS c ON b.categoryId = c.categoryId
    INNER JOIN User AS u ON b.userId = u.userId WHERE b.categoryId=?
    """    

    blogs = execute_query(query, (category_id,))
    return jsonify(blogs)

@app.route('/comments/blog/<int:blog_id>', methods=['GET'])
def comments_by_blog(blog_id):
    comments = execute_query("SELECT * FROM Comment WHERE blogId=?", (blog_id,))
    return jsonify(comments)

@app.route('/blogs/category/<int:category_id>/<int:page_number>/<int:per_page>', methods=['GET'])
def blogs_by_category_paginate(category_id, page_number, per_page):

    offset = (page_number - 1) * per_page

    query = """
    SELECT b.*, c.name, u.firstName, u.lastName
    FROM Blog AS b
    INNER JOIN Category AS c ON b.categoryId = c.categoryId
    INNER JOIN User AS u ON b.userId = u.userId
    WHERE b.categoryId = ?
    LIMIT ?
    OFFSET ?
"""

    blogs = execute_query(query, (category_id, per_page, offset))

    return jsonify(blogs)


@app.route('/blogs/page/<int:page_number>/<int:per_page>', methods=['GET'])
def blogs_by_paginate(page_number, per_page):

    offset = (page_number - 1) * per_page

    query = """
    SELECT b.*, c.name, u.firstName, u.lastName
    FROM Blog AS b
    INNER JOIN Category AS c ON b.categoryId = c.categoryId
    INNER JOIN User AS u ON b.userId = u.userId
    LIMIT ?
    OFFSET ?
"""

    blogs = execute_query(query, (per_page, offset))

    return jsonify(blogs)

@app.route('/register', methods=['POST'])
def register():
    data = request.json

    required_fields = ['email', 'username', 'password', 'firstName', 'lastName']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    hashed_password = hashlib.sha256(data['password'].encode()).hexdigest()

    try:
        execute_query("INSERT INTO User (email, username, password, firstname, lastname) VALUES (?, ?, ?, ?, ?)", 
                      (data['email'], data['username'], hashed_password, data['firstName'], data['lastName']))
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    login_data = request.json

    if 'username' not in login_data or 'password' not in login_data:
        return jsonify({"error": "Username and password are required"}), 400

    user = execute_query("SELECT email, username, password, firstname, lastname, userid FROM User WHERE username=?", (login_data['username'],))

    if user:

        user = user[0]

        stored_password = user[2]  
        input_password_hash = hashlib.sha256(login_data['password'].encode()).hexdigest()
        if stored_password == input_password_hash:
            return jsonify(user), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    else:
        return jsonify({"error": "Invalid username or password"}), 401

if __name__ == '__main__':
    app.run(debug=True)
