from flask import Blueprint
from flask import jsonify
from flask import request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

from application import db
from application import jwt
from application.auth.models import User

# Blueprint Configuration

auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    # Signup logic goes here
    return 'Logout'


@auth_bp.route('/create', methods=["GET"])
def create():
    db.create_all()
    return "created"


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


@auth_bp.route('/signup', methods=["POST"])
def signup():
    print('register function')
    username = request.form['username']
    email = request.form['email']
    password = generate_password_hash(request.form['password'])
    try:
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        print("New user", username, "added")
    except:
        print("Can't add user")
        return jsonify({
            "status": "error",
            "message": "Could not add user"
        })

    return jsonify({
        "status": "success",
        "message": "User added successfully"
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    # creates dictionary of form data
    print('login function')
    username_ = request.form['username']
    password_ = request.form['password']

    if not username_:
        # returns 401 if any email or / and password is missing
        return jsonify(result='Login  required')

    user = User.query \
        .filter_by(username=username_) \
        .first()

    if not user:
        # returns 401 if user does not exist
        return jsonify(result='User does not exist')
    print(password_)
    print(user.password)
    if check_password_hash(user.password, password_):
        # generates the JWT Token
        access_token = create_access_token(identity=user)
        print("You are logged")
        print("new tokens")
        return jsonify(access_token=access_token, result='You are logged')
    # returns 403 if password is wrong
    return jsonify(result='Password is wrong')


@auth_bp.route("/user", methods=["GET"])
@jwt_required()
def protected():
    # We can now access our sqlalchemy User object via `current_user`.
    print('hi')
    return jsonify(
        id=current_user.id,
        username=current_user.username,
    )


@auth_bp.route("/check_logged", methods=["GET"])
@jwt_required()
def check_logged():
    # We can now access our sqlalchemy User object via `current_user`.
    print('hi')
    return "logged"
