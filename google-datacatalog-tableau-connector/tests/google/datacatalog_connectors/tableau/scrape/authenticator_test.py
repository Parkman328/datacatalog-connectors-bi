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

import unittest
from unittest import mock

from google.datacatalog_connectors.tableau.scrape import authenticator

from . import metadata_scraper_mocks

__SCRAPE_PACKAGE = 'google.datacatalog_connectors.tableau.scrape'


@mock.patch(f'{__SCRAPE_PACKAGE}.authenticator.requests.post')
class AuthenticatorTest(unittest.TestCase):

    def test_authenticate_should_return_credentials_on_success(
            self, mock_post):

        mock_post.return_value = metadata_scraper_mocks.make_fake_response(
            {'credentials': {
                'token': 'TEST-TOKEN',
            }}, 200)

        credentials = authenticator.Authenticator.authenticate(
            'https://test-server.com', 'test-api', 'test-username',
            'test-password')

        self.assertEqual('TEST-TOKEN', credentials['token'])

    def test_authenticate_should_return_none_on_failure(self, mock_post):

        mock_post.return_value = metadata_scraper_mocks.make_fake_response(
            {'error': {}}, 401)

        credentials = authenticator.Authenticator.authenticate(
            'https://test-server.com', 'test-api', 'test-username',
            'test-password')

        self.assertIsNone(credentials)
