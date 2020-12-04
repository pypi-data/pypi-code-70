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

import datetime
import uuid

from keystoneauth1 import fixture
from oslo_utils import timeutils

from keystoneclient import access
from keystoneclient.tests.unit import utils as test_utils
from keystoneclient.tests.unit.v3 import client_fixtures
from keystoneclient.tests.unit.v3 import utils


TOKEN_RESPONSE = test_utils.test_response(
    headers=client_fixtures.AUTH_RESPONSE_HEADERS
)
UNSCOPED_TOKEN = client_fixtures.unscoped_token()
DOMAIN_SCOPED_TOKEN = client_fixtures.domain_scoped_token()
PROJECT_SCOPED_TOKEN = client_fixtures.project_scoped_token()


class AccessInfoTest(utils.TestCase):
    def test_building_unscoped_accessinfo(self):
        auth_ref = access.AccessInfo.factory(resp=TOKEN_RESPONSE,
                                             body=UNSCOPED_TOKEN)

        self.assertTrue(auth_ref)
        self.assertIn('methods', auth_ref)
        self.assertNotIn('catalog', auth_ref)

        self.assertEqual(client_fixtures.AUTH_SUBJECT_TOKEN,
                         auth_ref.auth_token)
        self.assertEqual(UNSCOPED_TOKEN.user_name, auth_ref.username)
        self.assertEqual(UNSCOPED_TOKEN.user_id, auth_ref.user_id)

        self.assertEqual(auth_ref.role_ids, [])
        self.assertEqual(auth_ref.role_names, [])

        self.assertIsNone(auth_ref.project_name)
        self.assertIsNone(auth_ref.project_id)

        with self.deprecations.expect_deprecations_here():
            self.assertIsNone(auth_ref.auth_url)
        with self.deprecations.expect_deprecations_here():
            self.assertIsNone(auth_ref.management_url)

        self.assertFalse(auth_ref.domain_scoped)
        self.assertFalse(auth_ref.project_scoped)

        self.assertEqual(UNSCOPED_TOKEN.user_domain_id,
                         auth_ref.user_domain_id)
        self.assertEqual(UNSCOPED_TOKEN.user_domain_name,
                         auth_ref.user_domain_name)

        self.assertIsNone(auth_ref.project_domain_id)
        self.assertIsNone(auth_ref.project_domain_name)

        self.assertEqual(auth_ref.expires, timeutils.parse_isotime(
                         UNSCOPED_TOKEN['token']['expires_at']))
        self.assertEqual(auth_ref.issued, timeutils.parse_isotime(
                         UNSCOPED_TOKEN['token']['issued_at']))

        self.assertEqual(auth_ref.expires, UNSCOPED_TOKEN.expires)
        self.assertEqual(auth_ref.issued, UNSCOPED_TOKEN.issued)

        self.assertEqual(auth_ref.audit_id, UNSCOPED_TOKEN.audit_id)
        self.assertIsNone(auth_ref.audit_chain_id)
        self.assertIsNone(UNSCOPED_TOKEN.audit_chain_id)

    def test_will_expire_soon(self):
        expires = timeutils.utcnow() + datetime.timedelta(minutes=5)
        UNSCOPED_TOKEN['token']['expires_at'] = expires.isoformat()
        auth_ref = access.AccessInfo.factory(resp=TOKEN_RESPONSE,
                                             body=UNSCOPED_TOKEN)
        self.assertFalse(auth_ref.will_expire_soon(stale_duration=120))
        self.assertTrue(auth_ref.will_expire_soon(stale_duration=301))
        self.assertFalse(auth_ref.will_expire_soon())

    def test_building_domain_scoped_accessinfo(self):
        auth_ref = access.AccessInfo.factory(resp=TOKEN_RESPONSE,
                                             body=DOMAIN_SCOPED_TOKEN)

        self.assertTrue(auth_ref)
        self.assertIn('methods', auth_ref)
        self.assertIn('catalog', auth_ref)
        self.assertTrue(auth_ref['catalog'])

        self.assertEqual(client_fixtures.AUTH_SUBJECT_TOKEN,
                         auth_ref.auth_token)
        self.assertEqual(DOMAIN_SCOPED_TOKEN.user_name, auth_ref.username)
        self.assertEqual(DOMAIN_SCOPED_TOKEN.user_id, auth_ref.user_id)

        self.assertEqual(DOMAIN_SCOPED_TOKEN.role_ids, auth_ref.role_ids)
        self.assertEqual(DOMAIN_SCOPED_TOKEN.role_names, auth_ref.role_names)

        self.assertEqual(DOMAIN_SCOPED_TOKEN.domain_name, auth_ref.domain_name)
        self.assertEqual(DOMAIN_SCOPED_TOKEN.domain_id, auth_ref.domain_id)

        self.assertIsNone(auth_ref.project_name)
        self.assertIsNone(auth_ref.project_id)

        self.assertEqual(DOMAIN_SCOPED_TOKEN.user_domain_id,
                         auth_ref.user_domain_id)
        self.assertEqual(DOMAIN_SCOPED_TOKEN.user_domain_name,
                         auth_ref.user_domain_name)

        self.assertIsNone(auth_ref.project_domain_id)
        self.assertIsNone(auth_ref.project_domain_name)

        self.assertTrue(auth_ref.domain_scoped)
        self.assertFalse(auth_ref.project_scoped)

        self.assertEqual(DOMAIN_SCOPED_TOKEN.audit_id, auth_ref.audit_id)
        self.assertEqual(DOMAIN_SCOPED_TOKEN.audit_chain_id,
                         auth_ref.audit_chain_id)

    def test_building_project_scoped_accessinfo(self):
        auth_ref = access.AccessInfo.factory(resp=TOKEN_RESPONSE,
                                             body=PROJECT_SCOPED_TOKEN)

        self.assertTrue(auth_ref)
        self.assertIn('methods', auth_ref)
        self.assertIn('catalog', auth_ref)
        self.assertTrue(auth_ref['catalog'])

        self.assertEqual(client_fixtures.AUTH_SUBJECT_TOKEN,
                         auth_ref.auth_token)
        self.assertEqual(PROJECT_SCOPED_TOKEN.user_name, auth_ref.username)
        self.assertEqual(PROJECT_SCOPED_TOKEN.user_id, auth_ref.user_id)

        self.assertEqual(PROJECT_SCOPED_TOKEN.role_ids, auth_ref.role_ids)
        self.assertEqual(PROJECT_SCOPED_TOKEN.role_names, auth_ref.role_names)

        self.assertIsNone(auth_ref.domain_name)
        self.assertIsNone(auth_ref.domain_id)

        self.assertEqual(PROJECT_SCOPED_TOKEN.project_name,
                         auth_ref.project_name)
        self.assertEqual(PROJECT_SCOPED_TOKEN.project_id, auth_ref.project_id)

        self.assertEqual(auth_ref.tenant_name, auth_ref.project_name)
        self.assertEqual(auth_ref.tenant_id, auth_ref.project_id)

        with self.deprecations.expect_deprecations_here():
            self.assertEqual(auth_ref.auth_url,
                             ('http://public.com:5000/v3',))
        with self.deprecations.expect_deprecations_here():
            self.assertEqual(auth_ref.management_url,
                             ('http://admin:35357/v3',))

        self.assertEqual(PROJECT_SCOPED_TOKEN.project_domain_id,
                         auth_ref.project_domain_id)
        self.assertEqual(PROJECT_SCOPED_TOKEN.project_domain_name,
                         auth_ref.project_domain_name)

        self.assertEqual(PROJECT_SCOPED_TOKEN.user_domain_id,
                         auth_ref.user_domain_id)
        self.assertEqual(PROJECT_SCOPED_TOKEN.user_domain_name,
                         auth_ref.user_domain_name)

        self.assertFalse(auth_ref.domain_scoped)
        self.assertTrue(auth_ref.project_scoped)

        self.assertEqual(PROJECT_SCOPED_TOKEN.audit_id, auth_ref.audit_id)
        self.assertEqual(PROJECT_SCOPED_TOKEN.audit_chain_id,
                         auth_ref.audit_chain_id)

    def test_oauth_access(self):
        consumer_id = uuid.uuid4().hex
        access_token_id = uuid.uuid4().hex

        token = fixture.V3Token()
        token.set_project_scope()
        token.set_oauth(access_token_id=access_token_id,
                        consumer_id=consumer_id)

        auth_ref = access.AccessInfo.factory(body=token)

        self.assertEqual(consumer_id, auth_ref.oauth_consumer_id)
        self.assertEqual(access_token_id, auth_ref.oauth_access_token_id)

        self.assertEqual(consumer_id, auth_ref['OS-OAUTH1']['consumer_id'])
        self.assertEqual(access_token_id,
                         auth_ref['OS-OAUTH1']['access_token_id'])

    def test_override_auth_token(self):
        token = fixture.V3Token()
        token.set_project_scope()

        new_auth_token = uuid.uuid4().hex
        auth_ref = access.AccessInfo.factory(body=token,
                                             auth_token=new_auth_token)
        self.assertEqual(new_auth_token, auth_ref.auth_token)

    def test_federated_property_standard_token(self):
        """Check if is_federated property returns expected value."""
        token = fixture.V3Token()
        token.set_project_scope()
        auth_ref = access.AccessInfo.factory(body=token)
        self.assertFalse(auth_ref.is_federated)
