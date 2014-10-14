# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock

from rally.benchmark.scenarios.ceilometer import resources
from tests.unit import test


class CeilometerResourcesTestCase(test.TestCase):
    def test_list_resources(self):
        scenario = resources.CeilometerResource()
        scenario._list_resources = mock.MagicMock()
        scenario.list_resources()

        scenario._list_resources.assert_called_once_with()