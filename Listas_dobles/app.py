from flask import Flask
from routes import bp as turnos_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(turnos_bp)
    return app


def main():
    app = create_app()
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    main()
