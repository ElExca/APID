from flask import Flask, jsonify
from flask_cors import CORS
from user.infrastructure.routers.user_router import user_router
from task.infrastructure.routers.task_router import task_router
from notification.infrastructure.routers.notification_router import notification_router
from user.infrastructure.middleware.user_middleware import token_required

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 
app.register_blueprint(user_router)
app.register_blueprint(task_router)
app.register_blueprint(notification_router)

@app.route('/protected')
@token_required
def protected_route():
    return jsonify({"message": "This route is only accessible with a valid token."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')