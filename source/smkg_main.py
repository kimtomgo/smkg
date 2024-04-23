from flask import Flask

from source.front.smkg_index import smkg_index

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(smkg_index)
    app.run()
