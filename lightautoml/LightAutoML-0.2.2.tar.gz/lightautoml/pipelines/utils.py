"""Pipeline utils."""

from typing import Sequence, List, Optional, Any

from log_calls import record_history

from lightautoml.dataset.base import LAMLDataset


@record_history(enabled=False)
def map_pipeline_names(input_names: Sequence[str], output_names: Sequence[str]) -> List[Optional[str]]:
    """Pipelines create name in the way 'prefix__feature_name'.

    Multiple pipelines will create names in the way 'prefix1__prefix2__feature_name'.
    This function maps initial features names to outputs.
    Result may be not exact in some rare cases, but it's ok for real pipelines.

    Args:
        input_names: initial feature names.
        output_names: output feature names.

    Returns:
        mapping between feature names.

    """
    # TODO: Add assert here
    mapped: List[Optional[str]] = [None] * len(output_names)
    s_in = set(input_names)

    for n, name in enumerate(output_names):
        splitted = name.split('__')

        for i in range(len(splitted)):
            name = '__'.join(splitted[i:])
            if name in s_in:
                mapped[n] = name
                break

    assert None not in mapped, 'Can not infer names. For feature selection purposes use simple pipeline (one-to-one)'

    return mapped


@record_history(enabled=False)
def get_columns_by_role(dataset: LAMLDataset, role_name: str, **kwargs: Any) -> List[str]:
    """
    Search for columns with specific role and attributes when building pipeline.

    Args:
        dataset: LAMLDataset to search.
        role_name: str name of features role.
        **kwargs: specific parameters values to search. Example: search for categories with ohe processing only.

    Returns:
        list of str features names.

    """
    features = []
    inv_roles = dataset.inverse_roles
    for role in inv_roles:
        if role.name == role_name:
            flg = True
            # TODO: maybe refactor
            for k in kwargs:
                try:
                    attr = getattr(role, k)
                except AttributeError:
                    flg = False
                    break
                if attr != kwargs[k]:
                    flg = False
                    break
            if flg:
                features.extend(inv_roles[role])

    return sorted(features)
