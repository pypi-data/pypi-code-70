from abc import abstractmethod
from typing import Optional, Protocol, Type, TypeVar, cast, get_origin

A = TypeVar("A")
B = TypeVar("B")
TSource = TypeVar("TSource")
TResult = TypeVar("TResult")
Base = TypeVar("Base")
Derived = TypeVar("Derived")


class Comparable(Protocol[TSource]):
    @abstractmethod
    def __lt__(self, other: TSource) -> bool:
        pass


def downcast(type: Type[Derived], expr: Base) -> Derived:
    """Downcast expression `Derived` to `Base`

    Checks at compile time that the type of expression E is a supertype
    of T, and checks at runtime that E is in fact an instance of T.

    Note: F# `:?>` or `downcast`.
    """
    assert isinstance(expr, type), f"The type of expression {expr} is not a supertype of {type}"
    return cast(type, expr)


def upcast(type: Type[Base], expr: Derived) -> Base:
    """Upcast expression `Derived` to `Base`.

    Check that the `Derived` type is a supertype of Base.

    Note: F# `:>` or `upcast`.
    """

    assert isinstance(expr, type), f"The expression {expr} is not derived from type {type}"
    return cast(Base, expr)


def try_upcast(type_: Type[Derived], expr: Base) -> Optional[Derived]:
    """Upcast expression `Base` to `Derived`.

    Check that the `Derived` type is a supertype of `Base`.

    NOTE: Supports generic types.

    Returns:
        None if `Derived` is not a supertype of `Base`.
    """
    origin: Optional[Type[Derived]] = get_origin(type_) or type_
    if origin is not None and isinstance(expr, origin):
        derived = cast(type(type_), expr)
        return derived
    else:
        return None


__all__ = ["Comparable", "downcast", "upcast", "try_upcast"]
