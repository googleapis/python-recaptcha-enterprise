from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/assess/<site_key>", methods=['GET'])
    def assess(site_key):
        return render_template("index.html", site_key=site_key)

    @app.route("/", methods=['GET'])
    def index():
        return "Helloworld!"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
