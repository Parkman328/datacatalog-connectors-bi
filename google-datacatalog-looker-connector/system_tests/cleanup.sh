#!/bin/bash -eu
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

echo 'Execute CLEANUP'
python google-datacatalog-looker-connector/tools/scripts/cleanup_datacatalog.py --datacatalog-project-ids $LOOKER2DC_DATACATALOG_PROJECT_ID

# Wait 5 seconds for the search index update
sleep 5
echo 'Assert CLEANUP'
python google-datacatalog-looker-connector/system_tests/cleanup_results_test.py
