#  !/usr/bin/env python
#
#  bases.py
"""
Useful base classes.
"""
#
#  Copyright © 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  UserList based on CPython.
#  Licensed under the Python Software Foundation License Version 2.
#  Copyright © 2001-2020 Python Software Foundation. All rights reserved.
#  Copyright © 2000 BeOpen.com. All rights reserved.
#  Copyright © 1995-2000 Corporation for National Research Initiatives. All rights reserved.
#  Copyright © 1991-1995 Stichting Mathematisch Centrum. All rights reserved.
#

# stdlib
from abc import abstractmethod
from numbers import Real
from pprint import pformat
from typing import (
		Any,
		Dict,
		Iterable,
		Iterator,
		List,
		MutableSequence,
		Optional,
		SupportsFloat,
		SupportsRound,
		Tuple,
		Type,
		TypeVar,
		Union,
		overload
		)

# 3rd party
import pydash  # type: ignore
from typing_extensions import Protocol

# this package
from domdf_python_tools.doctools import prettify_docstrings

__all__ = ["Dictable", "NamedList", "namedlist", "UserList", "UserFloat"]

_V = TypeVar("_V")


@prettify_docstrings
class Dictable(Iterable[Tuple[str, _V]]):
	"""
	The basic structure of a class that can be converted into a dictionary.
	"""

	@abstractmethod
	def __init__(self, *args, **kwargs):
		pass

	def __repr__(self) -> str:
		return super().__repr__()

	def __str__(self) -> str:
		return self.__repr__()

	def __iter__(self) -> Iterator[Tuple[str, _V]]:
		"""
		Iterate over the attributes of the class.
		"""

		yield from self.__dict__.items()

	def __getstate__(self) -> Dict[str, _V]:
		return self.__dict__

	def __setstate__(self, state):
		self.__init__(**state)  # type: ignore

	def __copy__(self):
		return self.__class__(**self.__dict__)

	def __deepcopy__(self, memodict={}):
		return self.__copy__()

	@property
	@abstractmethod
	def __dict__(self):
		return dict()  # pragma: no cover (abc)

	def __eq__(self, other) -> bool:
		if isinstance(other, self.__class__):
			return pydash.predicates.is_match(other.__dict__, self.__dict__)

		return NotImplemented


_T = TypeVar("_T")
_S = TypeVar("_S", bound="UserList")


@prettify_docstrings
class UserList(MutableSequence[_T]):
	"""
	Typed version of :class:`collections.UserList`.

	Class that simulates a list. The instance’s contents are kept in a regular list,
	which is accessible via the :attr:`~.UserList.data` attribute of UserList instances.
	The instance’s contents are initially set to a copy of list, defaulting to the
	empty list ``[]``.

	:param initlist: Values to initialise the :class:`~domdf_python_tools.bases.UserList` with.
	:default initlist: ``[]``


	.. admonition:: Subclassing requirements

		Subclasses of UserList are expected to offer a constructor which can be called with
		either no arguments or one argument. List operations which return a new sequence
		attempt to create an instance of the actual implementation class. To do so,
		it assumes that the constructor can be called with a single parameter, which is a
		sequence object used as a data source.

		If a derived class does not wish to comply with this requirement, all of the special
		methods supported by this class will need to be overridden; please consult the
		sources for information about the methods which need to be provided in that case.

	.. versionadded:: 0.10.0
	"""

	#: A real list object used to store the contents of the :class:`~domdf_python_tools.bases.UserList`.
	data: List[_T]

	def __init__(self, initlist: Optional[Iterable[_T]] = None):
		self.data = []
		if initlist is not None:
			# XXX should this accept an arbitrary sequence?
			if type(initlist) is type(self.data):  # noqa E721
				self.data[:] = initlist
			elif isinstance(initlist, UserList):
				self.data[:] = initlist.data[:]
			else:
				self.data = list(initlist)

	def __repr__(self) -> str:
		return repr(self.data)

	def __lt__(self, other: object) -> bool:
		return self.data < self.__cast(other)

	def __le__(self, other: object) -> bool:
		return self.data <= self.__cast(other)

	def __eq__(self, other: object) -> bool:
		return self.data == self.__cast(other)

	def __gt__(self, other: object) -> bool:
		return self.data > self.__cast(other)

	def __ge__(self, other: object) -> bool:
		return self.data >= self.__cast(other)

	@staticmethod
	def __cast(other):
		return other.data if isinstance(other, UserList) else other

	def __contains__(self, item: object) -> bool:
		return item in self.data

	def __len__(self) -> int:
		return len(self.data)

	def __iter__(self) -> Iterator[_T]:
		yield from self.data

	@overload
	def __getitem__(self, i: int) -> _T:
		...  # pragma: no cover

	@overload
	def __getitem__(self, i: slice) -> MutableSequence[_T]:
		...  # pragma: no cover

	def __getitem__(self, i: Union[int, slice]) -> Union[_T, MutableSequence[_T]]:
		if isinstance(i, slice):
			return self.__class__(self.data[i])
		else:
			return self.data[i]

	@overload
	def __setitem__(self, i: int, o: _T) -> None:
		...  # pragma: no cover

	@overload
	def __setitem__(self, i: slice, o: Iterable[_T]) -> None:
		...  # pragma: no cover

	def __setitem__(self, i: Union[int, slice], item: Union[_T, Iterable[_T]]) -> None:
		self.data[i] = item  # type: ignore

	def __delitem__(self, i: Union[int, slice]):
		del self.data[i]

	def __add__(self: _S, other: Iterable[_T]) -> _S:
		if isinstance(other, UserList):
			return self.__class__(self.data + other.data)
		elif isinstance(other, type(self.data)):
			return self.__class__(self.data + other)
		return self.__class__(self.data + list(other))

	def __radd__(self, other):
		if isinstance(other, UserList):
			return self.__class__(other.data + self.data)
		elif isinstance(other, type(self.data)):
			return self.__class__(other + self.data)
		return self.__class__(list(other) + self.data)

	def __iadd__(self: _S, other: Iterable[_T]) -> _S:
		if isinstance(other, UserList):
			self.data += other.data
		elif isinstance(other, type(self.data)):
			self.data += other
		else:
			self.data += list(other)
		return self

	def __mul__(self: _S, n: int) -> _S:
		return self.__class__(self.data * n)

	__rmul__ = __mul__

	def __imul__(self: _S, n: int) -> _S:
		self.data *= n
		return self

	def __copy__(self):
		inst = self.__class__.__new__(self.__class__)
		inst.__dict__.update(self.__dict__)
		# Create a copy and avoid triggering descriptors
		inst.__dict__["data"] = self.__dict__["data"][:]
		return inst

	def append(self, item: _T) -> None:
		"""
		Append ``item`` to the end of the :class:`~.domdf_python_tools.bases.UserList`.
		"""

		self.data.append(item)

	def insert(self, i: int, item: _T) -> None:
		"""
		Insert ``item`` at position ``i`` in the :class:`~.domdf_python_tools.bases.UserList`.
		"""

		self.data.insert(i, item)

	def pop(self, i: int = -1) -> _T:
		"""
		Removes and returns the item at index ``i``.

		:raises IndexError: if list is empty or index is out of range.
		"""

		return self.data.pop(i)

	def remove(self, item: _T) -> None:
		"""
		Removes the first occurrence of ``item`` from the list.

		:param item:

		:raises ValueError: if the item is not present.
		"""

		self.data.remove(item)

	def clear(self) -> None:
		"""
		Remove all items from the :class:`~.domdf_python_tools.bases.UserList`.
		"""

		self.data.clear()

	def copy(self: _S) -> _S:
		"""
		Returns a copy of the :class:`~.domdf_python_tools.bases.UserList`.
		"""

		return self.__class__(self)

	def count(self, item: _T) -> int:
		"""
		Returns the number of occurrences of ``item`` in the :class:`~.domdf_python_tools.bases.UserList`.
		"""

		return self.data.count(item)

	def index(self, item: _T, *args: Any) -> int:
		"""
		Returns the index of the fist element matching ``item``.

		:param item:
		:param args:

		:raises ValueError: if the item is not present.
		"""

		return self.data.index(item, *args)

	def reverse(self) -> None:
		"""
		Reverse the list in place.
		"""

		self.data.reverse()

	def sort(self, *, key=None, reverse: bool = False) -> None:
		"""
		Sort the list in ascending order and return :py:obj:`None`.

		The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
		order of two equal elements is maintained).

		If a key function is given, apply it once to each list item and sort them,
		ascending or descending, according to their function values.

		The reverse flag can be set to sort in descending order.
		"""

		self.data.sort(key=key, reverse=reverse)

	def extend(self, other: Iterable[_T]) -> None:
		"""
		Extend the :class:`~.domdf_python_tools.bases.NamedList` by appending elements from ``other``.

		:param other:
		"""

		if isinstance(other, UserList):
			self.data.extend(other.data)
		else:
			self.data.extend(other)


class _SupportsIndex(Protocol):

	def __index__(self) -> int:
		...


_F = TypeVar("_F", bound="UserFloat")


@prettify_docstrings
class UserFloat(Real):
	"""
	Class that simulates a float.

	:param value: Values to initialise the :class:`~domdf_python_tools.bases.UserFloat` with.

	.. versionadded:: 1.6.0
	"""

	def __init__(self, value: Union[SupportsFloat, _SupportsIndex, str, bytes, bytearray] = 0.0):
		self._value = (float(value), )

	def as_integer_ratio(self) -> Tuple[int, int]:
		"""
		Returns the float as a fraction.
		"""

		return float(self).as_integer_ratio()

	def hex(self) -> str:  # noqa: A003
		"""
		Returns the hexadecimal (base 16) representation of the float.
		"""

		return float(self).hex()

	def is_integer(self) -> bool:
		"""
		Returns whether the float is an integer.
		"""

		return float(self).is_integer()

	@classmethod
	def fromhex(cls: Type[_F], string: str) -> _F:
		"""
		Create a floating-point number from a hexadecimal string.

		:param string:
		"""

		return cls(float.fromhex(string))

	def __add__(self: _F, other: float) -> _F:
		return self.__class__(float(self).__add__(other))

	def __sub__(self: _F, other: float) -> _F:
		return self.__class__(float(self).__sub__(other))

	def __mul__(self: _F, other: float) -> _F:
		return self.__class__(float(self).__mul__(other))

	def __floordiv__(self: _F, other: float) -> _F:  # type: ignore
		return self.__class__(float(self).__floordiv__(other))

	def __truediv__(self: _F, other: float) -> _F:
		return self.__class__(float(self).__truediv__(other))

	def __mod__(self: _F, other: float) -> _F:
		return self.__class__(float(self).__mod__(other))

	def __divmod__(self: _F, other: float) -> Tuple[_F, _F]:
		return tuple(self.__class__(x) for x in float(self).__divmod__(other))  # type: ignore

	def __pow__(self: _F, other: float, mod=None) -> _F:
		return self.__class__(float(self).__pow__(other, mod))

	def __radd__(self: _F, other: float) -> _F:
		return self.__class__(float(self).__radd__(other))

	def __rsub__(self: _F, other: float) -> _F:
		return self.__class__(float(self).__rsub__(other))

	def __rmul__(self: _F, other: float) -> _F:
		return self.__class__(float(self).__rmul__(other))

	def __rfloordiv__(self: _F, other: float) -> _F:  # type: ignore
		return self.__class__(float(self).__rfloordiv__(other))

	def __rtruediv__(self: _F, other: float) -> _F:
		return self.__class__(float(self).__rtruediv__(other))

	def __rmod__(self: _F, other: float) -> _F:
		return self.__class__(float(self).__rmod__(other))

	def __rdivmod__(self: _F, other: float) -> Tuple[_F, _F]:
		return tuple(self.__class__(x) for x in float(self).__rdivmod__(other))  # type: ignore

	def __rpow__(self: _F, other: float, mod=None) -> _F:
		return self.__class__(float(self).__rpow__(other, mod))

	def __getnewargs__(self) -> Tuple[float]:
		return self._value

	def __trunc__(self) -> int:
		return float(self).__trunc__()

	def __round__(self, ndigits: Optional[int] = None) -> Union[int, float]:  # type: ignore
		return float(self).__round__(ndigits)

	def __eq__(self, other: object) -> bool:
		if isinstance(other, UserFloat) and not isinstance(other, float):
			return self._value == other._value
		else:
			return float(self).__eq__(other)

	def __ne__(self, other: object) -> bool:
		if isinstance(other, UserFloat) and not isinstance(other, float):
			return self._value != other._value
		else:
			return float(self).__ne__(other)

	def __lt__(self, other: Union[float, "UserFloat"]) -> bool:
		if isinstance(other, UserFloat) and not isinstance(other, float):
			return self._value < other._value
		else:
			return float(self).__lt__(other)

	def __le__(self, other: Union[float, "UserFloat"]) -> bool:
		if isinstance(other, UserFloat) and not isinstance(other, float):
			return self._value <= other._value
		else:
			return float(self).__le__(other)

	def __gt__(self, other: Union[float, "UserFloat"]) -> bool:
		if isinstance(other, UserFloat) and not isinstance(other, float):
			return self._value > other._value
		else:
			return float(self).__gt__(other)

	def __ge__(self, other: Union[float, "UserFloat"]) -> bool:
		if isinstance(other, UserFloat) and not isinstance(other, float):
			return self._value >= other._value
		else:
			return float(self).__ge__(other)

	def __neg__(self: _F) -> _F:
		return self.__class__(float(self).__neg__())

	def __pos__(self: _F) -> _F:
		return self.__class__(float(self).__pos__())

	def __str__(self) -> str:
		return str(float(self))

	def __int__(self) -> int:
		return int(float(self))

	def __float__(self) -> float:
		return self._value[0]

	def __abs__(self: _F) -> _F:
		return self.__class__(float(self).__abs__())

	def __hash__(self) -> int:
		return float(self).__hash__()

	def __repr__(self) -> str:
		return str(self)

	def __ceil__(self):
		raise NotImplementedError

	def __floor__(self):
		raise NotImplementedError


@prettify_docstrings
class NamedList(UserList[_T]):
	"""
	A list with a name.

	The name of the list is taken from the name of the subclass.

	.. versionchanged:: 0.10.0

		:class:`~.NamedList` now subclasses :class:`.UserList` rather than :class:`collections.UserList`.
	"""

	def __repr__(self) -> str:
		return f"{super().__repr__()}"

	def __str__(self) -> str:
		return f"{self.__class__.__name__}{pformat(list(self))}"


def namedlist(name: str = "NamedList") -> Type[NamedList]:
	"""
	A factory function to return a custom list subclass with a name.

	:param name: The name of the list.
	"""

	class cls(NamedList):
		pass

	cls.__name__ = name

	return cls
