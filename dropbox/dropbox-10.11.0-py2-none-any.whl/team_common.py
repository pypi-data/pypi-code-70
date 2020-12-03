# -*- coding: utf-8 -*-
# Auto-generated by Stone, do not modify.
# @generated
# flake8: noqa
# pylint: skip-file
from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

from dropbox import common

class GroupManagementType(bb.Union):
    """
    The group type determines how a group is managed.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar team_common.GroupManagementType.user_managed: A group which is managed
        by selected users.
    :ivar team_common.GroupManagementType.company_managed: A group which is
        managed by team admins only.
    :ivar team_common.GroupManagementType.system_managed: A group which is
        managed automatically by Dropbox.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    user_managed = None
    # Attribute is overwritten below the class definition
    company_managed = None
    # Attribute is overwritten below the class definition
    system_managed = None
    # Attribute is overwritten below the class definition
    other = None

    def is_user_managed(self):
        """
        Check if the union tag is ``user_managed``.

        :rtype: bool
        """
        return self._tag == 'user_managed'

    def is_company_managed(self):
        """
        Check if the union tag is ``company_managed``.

        :rtype: bool
        """
        return self._tag == 'company_managed'

    def is_system_managed(self):
        """
        Check if the union tag is ``system_managed``.

        :rtype: bool
        """
        return self._tag == 'system_managed'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def _process_custom_annotations(self, annotation_type, field_path, processor):
        super(GroupManagementType, self)._process_custom_annotations(annotation_type, field_path, processor)

GroupManagementType_validator = bv.Union(GroupManagementType)

class GroupSummary(bb.Struct):
    """
    Information about a group.

    :ivar team_common.GroupSummary.group_external_id: External ID of group. This
        is an arbitrary ID that an admin can attach to a group.
    :ivar team_common.GroupSummary.member_count: The number of members in the
        group.
    :ivar team_common.GroupSummary.group_management_type: Who is allowed to
        manage the group.
    """

    __slots__ = [
        '_group_name_value',
        '_group_id_value',
        '_group_external_id_value',
        '_member_count_value',
        '_group_management_type_value',
    ]

    _has_required_fields = True

    def __init__(self,
                 group_name=None,
                 group_id=None,
                 group_management_type=None,
                 group_external_id=None,
                 member_count=None):
        self._group_name_value = bb.NOT_SET
        self._group_id_value = bb.NOT_SET
        self._group_external_id_value = bb.NOT_SET
        self._member_count_value = bb.NOT_SET
        self._group_management_type_value = bb.NOT_SET
        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if group_external_id is not None:
            self.group_external_id = group_external_id
        if member_count is not None:
            self.member_count = member_count
        if group_management_type is not None:
            self.group_management_type = group_management_type

    # Instance attribute type: str (validator is set below)
    group_name = bb.Attribute("group_name")

    # Instance attribute type: str (validator is set below)
    group_id = bb.Attribute("group_id")

    # Instance attribute type: str (validator is set below)
    group_external_id = bb.Attribute("group_external_id", nullable=True)

    # Instance attribute type: int (validator is set below)
    member_count = bb.Attribute("member_count", nullable=True)

    # Instance attribute type: GroupManagementType (validator is set below)
    group_management_type = bb.Attribute("group_management_type", user_defined=True)

    def _process_custom_annotations(self, annotation_type, field_path, processor):
        super(GroupSummary, self)._process_custom_annotations(annotation_type, field_path, processor)

GroupSummary_validator = bv.Struct(GroupSummary)

class GroupType(bb.Union):
    """
    The group type determines how a group is created and managed.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar team_common.GroupType.team: A group to which team members are
        automatically added. Applicable to `team folders
        <https://www.dropbox.com/help/986>`_ only.
    :ivar team_common.GroupType.user_managed: A group is created and managed by
        a user.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    team = None
    # Attribute is overwritten below the class definition
    user_managed = None
    # Attribute is overwritten below the class definition
    other = None

    def is_team(self):
        """
        Check if the union tag is ``team``.

        :rtype: bool
        """
        return self._tag == 'team'

    def is_user_managed(self):
        """
        Check if the union tag is ``user_managed``.

        :rtype: bool
        """
        return self._tag == 'user_managed'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def _process_custom_annotations(self, annotation_type, field_path, processor):
        super(GroupType, self)._process_custom_annotations(annotation_type, field_path, processor)

GroupType_validator = bv.Union(GroupType)

class MemberSpaceLimitType(bb.Union):
    """
    The type of the space limit imposed on a team member.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar team_common.MemberSpaceLimitType.off: The team member does not have
        imposed space limit.
    :ivar team_common.MemberSpaceLimitType.alert_only: The team member has soft
        imposed space limit - the limit is used for display and for
        notifications.
    :ivar team_common.MemberSpaceLimitType.stop_sync: The team member has hard
        imposed space limit - Dropbox file sync will stop after the limit is
        reached.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    off = None
    # Attribute is overwritten below the class definition
    alert_only = None
    # Attribute is overwritten below the class definition
    stop_sync = None
    # Attribute is overwritten below the class definition
    other = None

    def is_off(self):
        """
        Check if the union tag is ``off``.

        :rtype: bool
        """
        return self._tag == 'off'

    def is_alert_only(self):
        """
        Check if the union tag is ``alert_only``.

        :rtype: bool
        """
        return self._tag == 'alert_only'

    def is_stop_sync(self):
        """
        Check if the union tag is ``stop_sync``.

        :rtype: bool
        """
        return self._tag == 'stop_sync'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def _process_custom_annotations(self, annotation_type, field_path, processor):
        super(MemberSpaceLimitType, self)._process_custom_annotations(annotation_type, field_path, processor)

MemberSpaceLimitType_validator = bv.Union(MemberSpaceLimitType)

class TimeRange(bb.Struct):
    """
    Time range.

    :ivar team_common.TimeRange.start_time: Optional starting time (inclusive).
    :ivar team_common.TimeRange.end_time: Optional ending time (exclusive).
    """

    __slots__ = [
        '_start_time_value',
        '_end_time_value',
    ]

    _has_required_fields = False

    def __init__(self,
                 start_time=None,
                 end_time=None):
        self._start_time_value = bb.NOT_SET
        self._end_time_value = bb.NOT_SET
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    # Instance attribute type: datetime.datetime (validator is set below)
    start_time = bb.Attribute("start_time", nullable=True)

    # Instance attribute type: datetime.datetime (validator is set below)
    end_time = bb.Attribute("end_time", nullable=True)

    def _process_custom_annotations(self, annotation_type, field_path, processor):
        super(TimeRange, self)._process_custom_annotations(annotation_type, field_path, processor)

TimeRange_validator = bv.Struct(TimeRange)

GroupExternalId_validator = bv.String()
GroupId_validator = bv.String()
MemberExternalId_validator = bv.String(max_length=64)
ResellerId_validator = bv.String()
TeamId_validator = bv.String()
TeamMemberId_validator = bv.String()
GroupManagementType._user_managed_validator = bv.Void()
GroupManagementType._company_managed_validator = bv.Void()
GroupManagementType._system_managed_validator = bv.Void()
GroupManagementType._other_validator = bv.Void()
GroupManagementType._tagmap = {
    'user_managed': GroupManagementType._user_managed_validator,
    'company_managed': GroupManagementType._company_managed_validator,
    'system_managed': GroupManagementType._system_managed_validator,
    'other': GroupManagementType._other_validator,
}

GroupManagementType.user_managed = GroupManagementType('user_managed')
GroupManagementType.company_managed = GroupManagementType('company_managed')
GroupManagementType.system_managed = GroupManagementType('system_managed')
GroupManagementType.other = GroupManagementType('other')

GroupSummary.group_name.validator = bv.String()
GroupSummary.group_id.validator = GroupId_validator
GroupSummary.group_external_id.validator = bv.Nullable(GroupExternalId_validator)
GroupSummary.member_count.validator = bv.Nullable(bv.UInt32())
GroupSummary.group_management_type.validator = GroupManagementType_validator
GroupSummary._all_field_names_ = set([
    'group_name',
    'group_id',
    'group_external_id',
    'member_count',
    'group_management_type',
])
GroupSummary._all_fields_ = [
    ('group_name', GroupSummary.group_name.validator),
    ('group_id', GroupSummary.group_id.validator),
    ('group_external_id', GroupSummary.group_external_id.validator),
    ('member_count', GroupSummary.member_count.validator),
    ('group_management_type', GroupSummary.group_management_type.validator),
]

GroupType._team_validator = bv.Void()
GroupType._user_managed_validator = bv.Void()
GroupType._other_validator = bv.Void()
GroupType._tagmap = {
    'team': GroupType._team_validator,
    'user_managed': GroupType._user_managed_validator,
    'other': GroupType._other_validator,
}

GroupType.team = GroupType('team')
GroupType.user_managed = GroupType('user_managed')
GroupType.other = GroupType('other')

MemberSpaceLimitType._off_validator = bv.Void()
MemberSpaceLimitType._alert_only_validator = bv.Void()
MemberSpaceLimitType._stop_sync_validator = bv.Void()
MemberSpaceLimitType._other_validator = bv.Void()
MemberSpaceLimitType._tagmap = {
    'off': MemberSpaceLimitType._off_validator,
    'alert_only': MemberSpaceLimitType._alert_only_validator,
    'stop_sync': MemberSpaceLimitType._stop_sync_validator,
    'other': MemberSpaceLimitType._other_validator,
}

MemberSpaceLimitType.off = MemberSpaceLimitType('off')
MemberSpaceLimitType.alert_only = MemberSpaceLimitType('alert_only')
MemberSpaceLimitType.stop_sync = MemberSpaceLimitType('stop_sync')
MemberSpaceLimitType.other = MemberSpaceLimitType('other')

TimeRange.start_time.validator = bv.Nullable(common.DropboxTimestamp_validator)
TimeRange.end_time.validator = bv.Nullable(common.DropboxTimestamp_validator)
TimeRange._all_field_names_ = set([
    'start_time',
    'end_time',
])
TimeRange._all_fields_ = [
    ('start_time', TimeRange.start_time.validator),
    ('end_time', TimeRange.end_time.validator),
]

ROUTES = {
}

