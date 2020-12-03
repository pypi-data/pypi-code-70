# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_file
from pulpcore.client.pulp_file.models.paginated_export_response_list import PaginatedExportResponseList  # noqa: E501
from pulpcore.client.pulp_file.rest import ApiException

class TestPaginatedExportResponseList(unittest.TestCase):
    """PaginatedExportResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedExportResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_file.models.paginated_export_response_list.PaginatedExportResponseList()  # noqa: E501
        if include_optional :
            return PaginatedExportResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulp_file.models.export_response.ExportResponse(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        task = '0', 
                        exported_resources = [
                            null
                            ], 
                        params = pulpcore.client.pulp_file.models.params.params(), )
                    ]
            )
        else :
            return PaginatedExportResponseList(
        )

    def testPaginatedExportResponseList(self):
        """Test PaginatedExportResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
