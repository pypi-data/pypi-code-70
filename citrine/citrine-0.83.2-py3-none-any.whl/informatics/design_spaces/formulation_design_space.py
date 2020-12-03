from typing import Mapping, Optional, Set
from uuid import UUID

from citrine._rest.resource import Resource
from citrine._serialization import properties
from citrine._session import Session
from citrine.informatics.constraints import Constraint
from citrine.informatics.descriptors import FormulationDescriptor
from citrine.informatics.design_spaces.design_space import DesignSpace

__all__ = ['FormulationDesignSpace']


class FormulationDesignSpace(Resource['FormulationDesignSpace'], DesignSpace):
    """[ALPHA] Design space composed of mixtures of ingredients.

    Parameters
    ----------
    name: str
        the name of the design space
    description: str
        the description of the design space
    formulation_descriptor: FormulationDescriptor
        descriptor used to store formulations sampled from the design space
    ingredients: Set[str]
        set of ingredient names that can be used in a formulation
    constraints: Set[IngredientConstraint]
        set of constraints that restricts formulations sampled from the space.
        This must include an
        :class:`~io.citrine.informatics.constraints.ingredient_count_constraint.IngredientCountConstraint`
        with maximum count of 100 or fewer.
    labels: Optional[Mapping[str, Set[str]]]
        map from a label to each ingredient that should given that label
        when it's included in a formulation, e.g., ``{'solvent': {'water', 'alcohol'}}``
    resolution: float, optional
        Minimum increment used to specify ingredient quantities.
        Default is 0.01.

    """

    _response_key = None

    uid = properties.Optional(properties.UUID, 'id', serializable=False)
    name = properties.String('config.name')
    description = properties.Optional(properties.String(), 'config.description')
    formulation_descriptor = properties.Object(
        FormulationDescriptor,
        'config.formulation_descriptor'
    )
    ingredients = properties.Set(properties.String, 'config.ingredients')
    labels = properties.Optional(properties.Mapping(
        properties.String,
        properties.Set(properties.String)
    ), 'config.labels')
    constraints = properties.Set(properties.Object(Constraint), 'config.constraints')
    resolution = properties.Float('config.resolution')
    typ = properties.String(
        'config.type',
        default='FormulationDesignSpace',
        deserializable=False
    )
    status = properties.String('status', serializable=False)
    status_info = properties.Optional(
        properties.List(properties.String()),
        'status_info',
        serializable=False
    )
    archived = properties.Boolean('archived', default=False)
    experimental = properties.Boolean("experimental", serializable=False, default=True)
    experimental_reasons = properties.Optional(
        properties.List(properties.String()),
        'experimental_reasons',
        serializable=False
    )
    module_type = properties.String('module_type', default='DESIGN_SPACE', deserializable=False)
    schema_id = properties.UUID('schema_id', default=UUID('f3907a58-aa46-462c-8837-a5aa9605e79e'),
                                deserializable=False)

    def __init__(self, *,
                 name: str,
                 description: str,
                 formulation_descriptor: FormulationDescriptor,
                 ingredients: Set[str],
                 constraints: Set[Constraint],
                 labels: Optional[Mapping[str, Set[str]]] = None,
                 resolution: float = 0.01,
                 session: Session = Session()):
        self.name  = name
        self.description  = description
        self.formulation_descriptor  = formulation_descriptor
        self.ingredients  = ingredients
        self.constraints  = constraints
        self.labels   = labels
        self.resolution  = resolution
        self.session  = session

    def _post_dump(self, data: dict) -> dict:
        data['display_name'] = data['config']['name']
        return data

    def __str__(self):
        return '<FormulationDesignSpace {!r}>'.format(self.name)
