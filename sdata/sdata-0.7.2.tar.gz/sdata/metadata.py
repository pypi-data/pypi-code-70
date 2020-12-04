import logging
import collections
import pandas as pd
import numpy as np
from sdata.timestamp import TimeStamp
import json
import os


class Attribute(object):
    """Attribute class"""

    DTYPES = {'float': float, 'int': int, 'str': str, 'timestamp': TimeStamp, "bool": bool}

    def __init__(self, name, value, **kwargs):
        """Attribute
        :param name
        :param value
        :param dtype ['float', 'int', 'str', 'timestamp', 'uuid?', 'unicode?']
        :param description
        :param dimension e.g. force, length, strain, count, energy
        :param unit

        """
        self._name = None
        self._value = None
        self._unit = "-"
        self._dimension = kwargs.get("dimension", "?")
        self._description = ""
        self._dtype = "str"
        self.name = name
        self.dtype = kwargs.get("dtype", "str")
        self.description = kwargs.get("description", "")
        self.unit = kwargs.get("unit", "-")
        # set dtype first!
        self.value = value

    def _get_name(self):
        return self._name

    def _set_name(self, value):
        if isinstance(value, str):
            try:
                value = value.strip()[:256]
                if len(value) > 0:
                    self._name = value
                else:
                    raise ValueError("empty Attribute.name")
            except ValueError as exp:
                logging.warning("error Attribute.name: %s" % exp)
        else:
            self._name = str(value).strip()[:256]

    name = property(fget=_get_name, fset=_set_name, doc="Attribute name")

    def _get_value(self):
        return self._value

    def _set_value(self, value):
        try:
            # dtype = self.DTYPES.get(self.dtype, str)
            dtype = self._guess_dtype(value)
            self.dtype = dtype.__name__
            # print(self.dtype, dtype.__name__)
            if value is None:
                self._value = None
            elif dtype.__name__ == "bool" and value in [0, "0", "False", "false"]:
                self._value = False
            elif dtype.__name__ == "bool" and value in [1, "1", "true", "True"]:
                self._value = True
            else:
                self._value = dtype(value)
        except ValueError as exp:
            logging.error("error Attribute.value: {}".format(exp))

    value = property(fget=_get_value, fset=_set_value, doc="Attribute value")

    def _guess_dtype(self, value):
        """returns dtype class

        :param value:
        :return: __class__
        """
        if isinstance(value, (int, np.int)):
            return value.__class__
        elif isinstance(value, (float, np.float)):
            return value.__class__
        elif isinstance(value, (str)):
            return value.__class__
        else:
            return str

    def _get_dtype(self):
        return self._dtype

    def _set_dtype(self, value):
        """set dtype str
s
        :param value:
        :return:
        """
        if value is None:
            return "str"
        elif "float" in value:
            value = "float"
        elif "int" in value:
            value = "int"
        if value in self.DTYPES.keys():
            self._dtype = value
        # todo: cast self.value to new dtype
        # if self._value is not None:
        #     try:
        #         self._value = self.DTYPES[self.dtype](self.value)
        #     except Exception as exp:
        #         logging.error("_set_dtype:{}:{}-{}".format(self.dtype, exp, exp.__class__.__name__))

    dtype = property(fget=_get_dtype, fset=_set_dtype, doc="Attribute type str")

    def _get_description(self):
        return self._description

    def _set_description(self, value):
        self._description = value

    description = property(fget=_get_description, fset=_set_description, doc="Attribute description")

    def _get_unit(self):
        return self._unit

    def _set_unit(self, value):
        self._unit = value

    unit = property(fget=_get_unit, fset=_set_unit, doc="Attribute unit")

    def to_dict(self):
        """:returns dict of attribute items"""
        return {'name': self.name,
                'value': self.value,
                'unit': self.unit,
                'dtype': self.dtype,
                'description': self.description,
                }

    def to_list(self):
        return [self.name, self.value, self.unit, self.dtype, self.description]

    def to_csv(self, prefix="", sep=",", quote=None):
        """export Attribute to csv

        :param prefix:
        :param sep:
        :param quote:
        :return:
        """
        xs = []
        for x in self.to_list():
            if x is None:
                xs.append("")
            else:
                xs.append(str(x))
        return "{}{}".format(prefix, sep.join(xs))

    def __str__(self):
        return "(Attr'%s':%s(%s))" % (self.name, self.value, self.dtype)

    __repr__ = __str__


class Metadata(object):
    """Metadata container class
    
    each Metadata entry has has a 
        * name (256)
        * value
        * unit
        * description
        * type (int, str, float, bool, timestamp)
        """

    ATTRIBUTEKEYS = ["name", "value", "dtype", "unit", "description"]

    def __init__(self, **kwargs):
        """Metadata class

        :param kwargs:
        """
        self._attributes = collections.OrderedDict()
        self._name = "N.N."

    def _get_name(self):
        return self._name

    def _set_name(self, value):
        self._name = str(value)

    name = property(fget=_get_name, fset=_set_name, doc="Name of the Metadata")

    def _get_attributes(self):
        return self._attributes

    def _set_attributes(self, value):
        self._attributes = value

    attributes = property(fget=_get_attributes, fset=_set_attributes, doc="returns Attributes")

    def set_attr(self, name="N.N.", value=None, **kwargs):
        """set Attribute"""
        if isinstance(name, Attribute):
            attr = name
        else:
            attr = self.get_attr(name) or Attribute(name, value, **kwargs)
        for key in ["dtype", "unit", "description"]:
            if key in kwargs:
                setattr(attr, key, kwargs.get(key))
        if value is not None:
            attr.value = value
        self._attributes[attr.name] = attr

    def get_attr(self, name):
        """get Attribute by name"""
        return self._attributes.get(name, None)

    def to_dict(self):
        """serialize attributes to dict"""
        d = {}
        for attr in self.attributes.values():
            d[attr.name] = attr.to_dict()
        return d

    def update_from_dict(self, d):
        """set attributes from dict"""
        for k, v in d.items():
            self.set_attr(**v)

    @classmethod
    def from_dict(cls, d):
        """setup metadata from dict"""
        metadata = cls()
        for k, v in d.items():
            metadata.set_attr(**v)
        return metadata

    def to_dataframe(self):
        """create dataframe"""
        d = self.to_dict()
        if len(d) == 0:
            df = pd.DataFrame(columns=self.ATTRIBUTEKEYS)
        else:
            df = pd.DataFrame.from_dict(d, orient="index")
        df.index.name = "key"
        return df[self.ATTRIBUTEKEYS]

    @property
    def df(self):
        """create dataframe"""
        return self.to_dataframe()

    @classmethod
    def from_dataframe(cls, df):
        """create metadata from dataframe"""
        d = df.to_dict(orient='index')
        metadata = cls.from_dict(d)
        return metadata

    def to_csv(self, filepath=None, sep=","):
        """serialize to csv"""
        try:
            df = self.to_dataframe()
            df.to_csv(filepath, index=None, sep=sep)
            return df.to_csv(filepath, index=None)
        except OSError as exp:
            logging.error("metadata.to_csv error: %s" % (exp))

    def to_csv_header(self, prefix="#", sep=",", filepath=None):
        """serialize to csv"""
        try:
            lines = []
            for attr in self.attributes.values():
                lines.append(attr.to_csv(prefix=prefix, sep=sep)+"\n")

            alines = "".join(lines)
            if filepath:
                logging.info("export '{}'".format(filepath))
                with open(filepath, "w") as fh:
                    fh.write(alines)
            return alines
        except OSError as exp:
            logging.error("metadata.to_csv error: %s" % (exp))

    @classmethod
    def from_csv(cls, filepath):
        """create metadata from dataframe"""
        df = pd.read_csv(filepath)
        metadata = cls.from_dataframe(df)
        return metadata

    def to_json(self, filepath=None):
        """create a json

        :param filepath: default None
        :return: json str
        """
        d = self.to_dict()
        if filepath:
            with open(filepath, "w") as fh:
                json.dump(d, fh)
        return json.dumps(d)

    @classmethod
    def from_json(cls,jsonstr=None, filepath=None):
        """create metadata from json file

        :param jsonstr: json str
        :param filepath: filepath to json file
        :return: Metadata
        """

        if filepath is not None and os.path.exists(filepath):
            with open(filepath, "r") as fh:
                j = json.load(fh)
            metadata = cls.from_dict(j)
        elif jsonstr is not None:
            j = json.loads(jsonstr)
            metadata = cls.from_dict(j)
        return metadata

    def to_list(self):
        """create a nested list of Attribute values

        :return: list
        """
        return self.df.values.tolist()

    @classmethod
    def from_list(cls, mlist):
        """create metadata from a list of Attribute values

        [['force_x', 1.2, 'float', 'kN', 'force in x-direction'],
         ['force_y', 3.1, 'float', 'N', 'force in y-direction']]
         """
        metadata = cls()
        for alist in mlist:
            if len(alist) < 2:
                logging.error("Metadata.from_list skip {}".format(alist))
            else:
                alist.extend([None, None, None])
                #["name", "value", "dtype", "unit", "description"]
                metadata.add(alist[0], alist[1], dtype=alist[2], unit=alist[3], description=alist[4])
        return metadata

    def __repr__(self):
        return "(Metadata'%s':%d)" % (self.name, len(self.attributes))

    def __str__(self):
        return "(Metadata'%s':%d %s)" % (self.name, len(self.attributes), [x for x in self.attributes])

    def add(self, name, value=None, **kwargs):
        """add Attribute

        :param name:
        :param value:
        :param kwargs:
        :return:
        """
        self.set_attr(name, value, **kwargs)

    def get(self, name, default=None):
        if self._attributes.get(name) is not None:
            return self._attributes.get(name)
        else:
            return default

    def keys(self):
        """

        :return: list of Attribute names
        """
        return list(self._attributes.keys())

    def values(self):
        """

        :return: list of Attribute values
        """
        return list(self._attributes.values())

    def items(self):
        """

        :return: list of Attribute items (keys, values)
        """
        return list(self._attributes.items())

    @property
    def size(self):
        """return number uf Attribute"""
        return len(self.attributes)

    def __getitem__(self, name):
        return self.get(name)