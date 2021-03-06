#!/usr/bin/python
#
# Copyright 2020 Google LLC
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

import logging
import requests

from google.datacatalog_connectors.tableau.scrape import constants


class Authenticator:

    @classmethod
    def authenticate(cls,
                     server_address,
                     api_version,
                     username,
                     password,
                     site_content_url=None):

        url = f'{server_address}/api/{api_version}/auth/signin'

        headers = {
            'Content-Type': constants.JSON_CONTENT_TYPE,
            'Accept': constants.JSON_CONTENT_TYPE
        }

        body = {
            'credentials': {
                'name': username,
                'password': password,
                'site': {
                    'contentUrl': site_content_url
                }
            }
        }

        response = requests.post(url=url, headers=headers, json=body).json()

        if not response.get('credentials'):
            logging.info(response)
            return

        return response['credentials']
