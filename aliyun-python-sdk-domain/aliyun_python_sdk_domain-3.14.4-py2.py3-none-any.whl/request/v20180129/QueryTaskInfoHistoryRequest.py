# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkdomain.endpoint import endpoint_data

class QueryTaskInfoHistoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'QueryTaskInfoHistory')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_EndCreateTime(self):
		return self.get_query_params().get('EndCreateTime')

	def set_EndCreateTime(self,EndCreateTime):
		self.add_query_param('EndCreateTime',EndCreateTime)

	def get_BeginCreateTime(self):
		return self.get_query_params().get('BeginCreateTime')

	def set_BeginCreateTime(self,BeginCreateTime):
		self.add_query_param('BeginCreateTime',BeginCreateTime)

	def get_TaskNoCursor(self):
		return self.get_query_params().get('TaskNoCursor')

	def set_TaskNoCursor(self,TaskNoCursor):
		self.add_query_param('TaskNoCursor',TaskNoCursor)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_CreateTimeCursor(self):
		return self.get_query_params().get('CreateTimeCursor')

	def set_CreateTimeCursor(self,CreateTimeCursor):
		self.add_query_param('CreateTimeCursor',CreateTimeCursor)