import os
from typing import *

from cognite.seismic._api.api import API
from cognite.seismic._api.utility import MaybeString, Metadata, get_identifier, get_search_spec
from cognite.seismic.data_classes.api_types import SeismicStore

if not os.getenv("READ_THE_DOCS"):
    from cognite.seismic.protos.v1.seismic_service_messages_pb2 import (
        SearchSeismicStoresRequest,
        EditSeismicStoreRequest,
    )
    from cognite.seismic.protos.v1.seismic_service_datatypes_pb2 import OptionalMap


class SeismicStoreAPI(API):
    def __init__(self, query, ingestion, metadata):
        super().__init__(query=query, ingestion=ingestion, metadata=metadata)

    def search(
        self,
        *,
        id: Union[int, None] = None,
        external_id: MaybeString = None,
        external_id_substring: MaybeString = None,
        name: MaybeString = None,
        name_substring: MaybeString = None,
        get_all: bool = False,
        include_file_info: bool = False,
        include_headers: bool = False,
        include_volume_definitions: bool = True,
    ) -> Iterable[SeismicStore]:
        """Search for seismic stores.

        Can search by id, name, or substring or name. 
        Only one search method should be specified. The behaviour when multiple are specified is undefined.

        Args:
            id (int|None): Seismic store id
            external_id (str|None): Seismic store external id. NOT IMPLEMENTED
            external_id_substring (str|None): Substring of external id to search by. NOT IMPLEMENTED
            name (str|None): Seismic store name
            name_substring (str|None): Substring of name to search by
            get_all (bool): Whether to instead retrieve all visible seismic stores. Equivalent to list().
            include_file_info (bool): If true, the response will include information on the source file.
            include_headers (bool): If true, the response will include headers.
            include_volume_definitions (bool): If false, the response will exclude getting the inline and crossline volume definitions.
        
        Returns:
            Iterable[SeismicStore]: The list of matching seismic stores
        """
        if get_all:
            req = SearchSeismicStoresRequest(
                include_file_info=include_file_info,
                include_headers=include_headers,
                include_volume_definitions=include_volume_definitions,
            )
        else:
            spec = get_search_spec(id, external_id, external_id_substring, name, name_substring)
            req = SearchSeismicStoresRequest(
                seismic_stores=spec,
                include_file_info=include_file_info,
                include_headers=include_headers,
                include_volume_definitions=include_volume_definitions,
            )
        results = self.query.SearchSeismicStores(req, metadata=self.metadata)
        return [SeismicStore.from_proto(p) for p in results]

    def list(self, *, include_file_info: bool = False) -> Iterable[SeismicStore]:
        """List all visible seismic stores.

        List all visible seismic stores. This is equivalent to calling search() with get_all=true.
        
        Args:
            include_file_info (bool): (Optional) If true, the response will include information on the source file.

        Returns:
            Iterable[SeismicStore]: The list of visible seismic stores
        """
        return self.search(get_all=True, include_file_info=include_file_info)

    def get(self, id: int) -> SeismicStore:
        """Get a seismic store by its id.

        Equivalent to search(id=id, include_file_info=True, include_headers=True).

        Args:
            id (int): The seismic store id to find
        """
        results = self.search(id=id, include_file_info=True, include_headers=True)
        if len(results) == 0:
            raise Exception(f"Could not find the seismic store {id}")
        if len(results) > 1:
            raise Exception("Found too many seismic stores. Please contact support.")
        return results[0]

    def edit(
        self,
        *,
        id: Union[int, None] = None,
        external_id: MaybeString,
        new_name: MaybeString,
        metadata: Union[Metadata, None],
    ) -> SeismicStore:
        """Edit a seismic store.

        Edit a seismic store, providing the seismic store id.
        The name and the metadata can be edited.

        Args:
            id (int | None): The id of the seismic store
            new_name (str | None): (Optional) If specified, the new name. Provide an empty string to delete the existing name.
            metadata (Dict[str, str] | None): (Optional) If specified, replaces the old metadata with the new one.
        """
        identifier = get_identifier(id, external_id)
        request = EditSeismicStoreRequest(seismic=identifier)
        if new_name is not None:
            request.name = new_name
        if metadata is not None:
            request.metadata = metadata
        return SeismicStore.from_proto(self.query.EditSeismicStore(request, metadata=self.metadata))
