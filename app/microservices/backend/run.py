from app import create_app, db
import os

app = create_app()
DEBUG_MODE = os.getenv('DEBUG_MODE') == 'True'
HOST = '0.0.0.0'
PORT = 8080

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=DEBUG_MODE, host=HOST, port=PORT)
