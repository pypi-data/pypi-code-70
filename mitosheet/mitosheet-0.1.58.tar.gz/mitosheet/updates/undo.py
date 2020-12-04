#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

"""
A undo update, which removes the most recent step from
the sheet. 
"""

UNDO_EVENT = 'undo'
UNDO_PARAMS = []

def execute_undo_update(wsc):
    """
    The function responsible for updating the widget state container
    by removing the most recent step.

    If there is no most recent step, does nothing.
    """

    if len(wsc.steps) == 1:
        return 

    # Pop off the last element
    wsc.steps.pop()

    # If we need to remove from df_names (e.g. because of an undo), we remove it
    wsc.df_names = wsc.df_names[:len(wsc.dfs)]



"""
This object wraps all the information
that is needed for a undo step!
"""
UNDO_UPDATE = {
    'event_type': UNDO_EVENT,
    'params': UNDO_PARAMS,
    'execute': execute_undo_update
}





