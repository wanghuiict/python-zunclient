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

from zunclient.common import base


class Version(base.Resource):
    def __repr__(self):
        return "<Version>"


class VersionManager(base.Manager):
    resource_class = Version

    def list(self):
        url = "%s" % self.api.get_endpoint()
        url = "%s/" % url.rsplit("/", 1)[0]
        return self._list(url, "versions")

    def get_current(self):
        for version in self.list():
            if version.status == "CURRENT":
                return version
        return None
