# coding: utf-8

# flake8: noqa

"""
    Timeline events

    This feature allows an app to create and configure custom events that can show up in the timelines of certain CRM objects like contacts, companies, tickets, or deals. You'll find multiple use cases for this API in the sections below.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from hubspot.crm.timeline.api.events_api import EventsApi
from hubspot.crm.timeline.api.templates_api import TemplatesApi
from hubspot.crm.timeline.api.tokens_api import TokensApi

# import ApiClient
from hubspot.crm.timeline.api_client import ApiClient
from hubspot.crm.timeline.configuration import Configuration
from hubspot.crm.timeline.exceptions import OpenApiException
from hubspot.crm.timeline.exceptions import ApiTypeError
from hubspot.crm.timeline.exceptions import ApiValueError
from hubspot.crm.timeline.exceptions import ApiKeyError
from hubspot.crm.timeline.exceptions import ApiException
# import models into sdk package
from hubspot.crm.timeline.models.batch_input_timeline_event import BatchInputTimelineEvent
from hubspot.crm.timeline.models.batch_response_timeline_event_response import BatchResponseTimelineEventResponse
from hubspot.crm.timeline.models.batch_response_timeline_event_response_with_errors import BatchResponseTimelineEventResponseWithErrors
from hubspot.crm.timeline.models.collection_response_timeline_event_template import CollectionResponseTimelineEventTemplate
from hubspot.crm.timeline.models.error import Error
from hubspot.crm.timeline.models.error_category import ErrorCategory
from hubspot.crm.timeline.models.error_detail import ErrorDetail
from hubspot.crm.timeline.models.event_detail import EventDetail
from hubspot.crm.timeline.models.next_page import NextPage
from hubspot.crm.timeline.models.paging import Paging
from hubspot.crm.timeline.models.previous_page import PreviousPage
from hubspot.crm.timeline.models.standard_error import StandardError
from hubspot.crm.timeline.models.timeline_event import TimelineEvent
from hubspot.crm.timeline.models.timeline_event_i_frame import TimelineEventIFrame
from hubspot.crm.timeline.models.timeline_event_response import TimelineEventResponse
from hubspot.crm.timeline.models.timeline_event_template import TimelineEventTemplate
from hubspot.crm.timeline.models.timeline_event_template_create_request import TimelineEventTemplateCreateRequest
from hubspot.crm.timeline.models.timeline_event_template_token import TimelineEventTemplateToken
from hubspot.crm.timeline.models.timeline_event_template_token_option import TimelineEventTemplateTokenOption
from hubspot.crm.timeline.models.timeline_event_template_token_update_request import TimelineEventTemplateTokenUpdateRequest
from hubspot.crm.timeline.models.timeline_event_template_update_request import TimelineEventTemplateUpdateRequest

