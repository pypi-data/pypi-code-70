# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AppBasedLinkQuery
    from ._models_py3 import ChannelInfo
    from ._models_py3 import ConversationList
    from ._models_py3 import FileConsentCard
    from ._models_py3 import FileConsentCardResponse
    from ._models_py3 import FileDownloadInfo
    from ._models_py3 import FileInfoCard
    from ._models_py3 import FileUploadInfo
    from ._models_py3 import MessageActionsPayload
    from ._models_py3 import MessageActionsPayloadApp
    from ._models_py3 import MessageActionsPayloadAttachment
    from ._models_py3 import MessageActionsPayloadBody
    from ._models_py3 import MessageActionsPayloadConversation
    from ._models_py3 import MessageActionsPayloadFrom
    from ._models_py3 import MessageActionsPayloadMention
    from ._models_py3 import MessageActionsPayloadReaction
    from ._models_py3 import MessageActionsPayloadUser
    from ._models_py3 import MessagingExtensionAction
    from ._models_py3 import MessagingExtensionActionResponse
    from ._models_py3 import MessagingExtensionAttachment
    from ._models_py3 import MessagingExtensionParameter
    from ._models_py3 import MessagingExtensionQuery
    from ._models_py3 import MessagingExtensionQueryOptions
    from ._models_py3 import MessagingExtensionResponse
    from ._models_py3 import MessagingExtensionResult
    from ._models_py3 import MessagingExtensionSuggestedAction
    from ._models_py3 import NotificationInfo
    from ._models_py3 import O365ConnectorCard
    from ._models_py3 import O365ConnectorCardActionBase
    from ._models_py3 import O365ConnectorCardActionCard
    from ._models_py3 import O365ConnectorCardActionQuery
    from ._models_py3 import O365ConnectorCardDateInput
    from ._models_py3 import O365ConnectorCardFact
    from ._models_py3 import O365ConnectorCardHttpPOST
    from ._models_py3 import O365ConnectorCardImage
    from ._models_py3 import O365ConnectorCardInputBase
    from ._models_py3 import O365ConnectorCardMultichoiceInput
    from ._models_py3 import O365ConnectorCardMultichoiceInputChoice
    from ._models_py3 import O365ConnectorCardOpenUri
    from ._models_py3 import O365ConnectorCardOpenUriTarget
    from ._models_py3 import O365ConnectorCardSection
    from ._models_py3 import O365ConnectorCardTextInput
    from ._models_py3 import O365ConnectorCardViewAction
    from ._models_py3 import SigninStateVerificationQuery
    from ._models_py3 import TaskModuleContinueResponse
    from ._models_py3 import TaskModuleMessageResponse
    from ._models_py3 import TaskModuleRequest
    from ._models_py3 import TaskModuleRequestContext
    from ._models_py3 import TaskModuleResponse
    from ._models_py3 import TaskModuleResponseBase
    from ._models_py3 import TaskModuleTaskInfo
    from ._models_py3 import TeamDetails
    from ._models_py3 import TeamInfo
    from ._models_py3 import TeamsChannelAccount
    from ._models_py3 import TeamsChannelData
    from ._models_py3 import TeamsPagedMembersResult
    from ._models_py3 import TenantInfo
except (SyntaxError, ImportError):
    from ._models import AppBasedLinkQuery
    from ._models import ChannelInfo
    from ._models import ConversationList
    from ._models import FileConsentCard
    from ._models import FileConsentCardResponse
    from ._models import FileDownloadInfo
    from ._models import FileInfoCard
    from ._models import FileUploadInfo
    from ._models import MessageActionsPayload
    from ._models import MessageActionsPayloadApp
    from ._models import MessageActionsPayloadAttachment
    from ._models import MessageActionsPayloadBody
    from ._models import MessageActionsPayloadConversation
    from ._models import MessageActionsPayloadFrom
    from ._models import MessageActionsPayloadMention
    from ._models import MessageActionsPayloadReaction
    from ._models import MessageActionsPayloadUser
    from ._models import MessagingExtensionAction
    from ._models import MessagingExtensionActionResponse
    from ._models import MessagingExtensionAttachment
    from ._models import MessagingExtensionParameter
    from ._models import MessagingExtensionQuery
    from ._models import MessagingExtensionQueryOptions
    from ._models import MessagingExtensionResponse
    from ._models import MessagingExtensionResult
    from ._models import MessagingExtensionSuggestedAction
    from ._models import NotificationInfo
    from ._models import O365ConnectorCard
    from ._models import O365ConnectorCardActionBase
    from ._models import O365ConnectorCardActionCard
    from ._models import O365ConnectorCardActionQuery
    from ._models import O365ConnectorCardDateInput
    from ._models import O365ConnectorCardFact
    from ._models import O365ConnectorCardHttpPOST
    from ._models import O365ConnectorCardImage
    from ._models import O365ConnectorCardInputBase
    from ._models import O365ConnectorCardMultichoiceInput
    from ._models import O365ConnectorCardMultichoiceInputChoice
    from ._models import O365ConnectorCardOpenUri
    from ._models import O365ConnectorCardOpenUriTarget
    from ._models import O365ConnectorCardSection
    from ._models import O365ConnectorCardTextInput
    from ._models import O365ConnectorCardViewAction
    from ._models import SigninStateVerificationQuery
    from ._models import TaskModuleContinueResponse
    from ._models import TaskModuleMessageResponse
    from ._models import TaskModuleRequest
    from ._models import TaskModuleRequestContext
    from ._models import TaskModuleResponse
    from ._models import TaskModuleResponseBase
    from ._models import TaskModuleTaskInfo
    from ._models import TeamDetails
    from ._models import TeamInfo
    from ._models import TeamsChannelAccount
    from ._models import TeamsChannelData
    from ._models import TeamsPagedMembersResult
    from ._models import TenantInfo

__all__ = [
    "AppBasedLinkQuery",
    "ChannelInfo",
    "ConversationList",
    "FileConsentCard",
    "FileConsentCardResponse",
    "FileDownloadInfo",
    "FileInfoCard",
    "FileUploadInfo",
    "MessageActionsPayload",
    "MessageActionsPayloadApp",
    "MessageActionsPayloadAttachment",
    "MessageActionsPayloadBody",
    "MessageActionsPayloadConversation",
    "MessageActionsPayloadFrom",
    "MessageActionsPayloadMention",
    "MessageActionsPayloadReaction",
    "MessageActionsPayloadUser",
    "MessagingExtensionAction",
    "MessagingExtensionActionResponse",
    "MessagingExtensionAttachment",
    "MessagingExtensionParameter",
    "MessagingExtensionQuery",
    "MessagingExtensionQueryOptions",
    "MessagingExtensionResponse",
    "MessagingExtensionResult",
    "MessagingExtensionSuggestedAction",
    "NotificationInfo",
    "O365ConnectorCard",
    "O365ConnectorCardActionBase",
    "O365ConnectorCardActionCard",
    "O365ConnectorCardActionQuery",
    "O365ConnectorCardDateInput",
    "O365ConnectorCardFact",
    "O365ConnectorCardHttpPOST",
    "O365ConnectorCardImage",
    "O365ConnectorCardInputBase",
    "O365ConnectorCardMultichoiceInput",
    "O365ConnectorCardMultichoiceInputChoice",
    "O365ConnectorCardOpenUri",
    "O365ConnectorCardOpenUriTarget",
    "O365ConnectorCardSection",
    "O365ConnectorCardTextInput",
    "O365ConnectorCardViewAction",
    "SigninStateVerificationQuery",
    "TaskModuleContinueResponse",
    "TaskModuleMessageResponse",
    "TaskModuleRequest",
    "TaskModuleRequestContext",
    "TaskModuleResponse",
    "TaskModuleResponseBase",
    "TaskModuleTaskInfo",
    "TeamDetails",
    "TeamInfo",
    "TeamsChannelAccount",
    "TeamsChannelData",
    "TeamsPagedMembersResult",
    "TenantInfo",
]
