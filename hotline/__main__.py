# Copyright 2019 Alethea Katherine Flowers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

import hotline.config
from hotline.app import app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

hotline.config.load()

# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
