# -*- coding: utf-8 -*-
#
# File: testCustomMeeting.py
#
# Copyright (c) 2007-2012 by CommunesPlone.org
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

from Products.MeetingIDEA.tests.MeetingIDEATestCase import MeetingIDEATestCase
from collective.contact.plonegroup.utils import get_organization
from Products.PloneMeeting.utils import org_id_to_uid

class testCustomMeeting(MeetingIDEATestCase):
    """Tests the MeetingItem adapted methods."""

    def test_idea_getIDEAPrintableItems(self):
        self.changeUser('admin')
        group = get_organization(org_id_to_uid('developers'))
        group.Title = u"Développeurs - DSI"
        self.changeUser('pmManager')
        meeting = self.create('Meeting', date='2007/12/11 09:00:00')
        item1 = self.create('MeetingItem', title='The first item')
        self.presentItem(item1)
        item2 = self.create('MeetingItem', title='The second item')
        self.presentItem(item2)
        meeting.adapted().getIDEAPrintableItemsByCategory()
