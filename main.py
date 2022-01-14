from app import create_app


def run():
    """Run the flask app."""

    flask_app = create_app()
    flask_app.run(debug=True, port=8080)


if __name__ == "__main__":
    run()
