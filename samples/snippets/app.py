# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
