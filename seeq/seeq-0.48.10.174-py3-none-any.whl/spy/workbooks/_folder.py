from seeq.sdk import *

from ._item import Item
from ._user import ItemWithOwnerAndAcl

from .. import _common
from .. import _login


class Folder(ItemWithOwnerAndAcl):
    def _pull(self, item_id):
        folders_api = FoldersApi(_login.client)
        folder_output = folders_api.get_folder(folder_id=item_id)  # type: FolderOutputV1
        self._pull_owner_and_acl(folder_output.owner.id)
        self._pull_ancestors(folder_output.ancestors)
        self.provenance = Item.PULL

    def _find_by_name(self, folder_id):
        folders_api = FoldersApi(_login.client)

        if folder_id and folder_id != _common.PATH_ROOT:
            folders = folders_api.get_folders(filter='owner',
                                              folder_id=folder_id,
                                              limit=10000)  # type: FolderOutputListV1
        else:
            folders = folders_api.get_folders(filter='owner',
                                              limit=10000)  # type: FolderOutputListV1

        content_dict = {content.name.lower(): content for content in folders.content}
        if self.name.lower() in content_dict and content_dict[self.name.lower()].type == 'Folder':
            return content_dict[self.name.lower()]

        return None

    def push(self, parent_folder_id, datasource_maps, datasource_output, item_map, *, owner=None, label=None,
             access_control=None):
        items_api = ItemsApi(_login.client)
        folders_api = FoldersApi(_login.client)
        folder_item = self.find_me(label, datasource_output)

        if folder_item is None and self.provenance == Item.CONSTRUCTOR:
            folder_item = self._find_by_name(parent_folder_id)

        if not folder_item:
            folder_input = FolderInputV1()
            folder_input.name = self['Name']
            if 'Description' in self:
                folder_input.description = self['Description']
            folder_input.owner_id = self.decide_owner(datasource_maps, item_map, owner=owner)
            folder_input.parent_folder_id = parent_folder_id if parent_folder_id != _common.PATH_ROOT else None

            folder_output = folders_api.create_folder(body=folder_input)

            items_api.set_properties(id=folder_output.id, body=[
                ScalarPropertyV1(name='Datasource Class', value=datasource_output.datasource_class),
                ScalarPropertyV1(name='Datasource ID', value=datasource_output.datasource_id),
                ScalarPropertyV1(name='Data ID', value=self._construct_data_id(label))])
        else:
            folder_output = folders_api.get_folder(folder_id=folder_item.id)  # type: FolderOutputV1

            props = [ScalarPropertyV1(name='Name', value=self['Name'])]
            if 'Description' in self:
                props.append(ScalarPropertyV1(name='Description', value=self['Description']))

            # If the folder happens to be archived, un-archive it. If you're pushing a new copy it seems likely
            # you're intending to revive it.
            props.append(ScalarPropertyV1(name='Archived', value=False))

            items_api.set_properties(id=folder_output.id, body=props)

            owner_id = self.decide_owner(
                datasource_maps, item_map, owner=owner, current_owner_id=folder_output.owner.id)

            self._push_owner_and_location(folder_output, owner_id, parent_folder_id)

        item_map[self.id.upper()] = folder_output.id.upper()

        if access_control:
            self._push_acl(folder_output.id, datasource_maps, item_map, access_control)

        return folder_output
