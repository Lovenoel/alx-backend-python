#!/usr/bin/env python3
"""
# Safely get value function with type annotations.
# """

# from typing import Mapping, Any, TypeVar, Union

# T = TypeVar('T')

# def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
#     """
#     Safely get a value from a dictionary. If the key doesn't exist, return the default value.

#     :param dct: a dictionary mapping keys of any type to values of a generic type T
#     :param key: the key to look up in the dictionary
#     :param default: the default value to return if the key isn't found (defaults to None)
#     :return: the value associated with the key, or the default value
#     """
#     if key in dct:
#         return dct[key]
#     else:
#         return default

#!/usr/bin/env python3
# """
# Safely get value function with type annotations.
# """

# from typing import Mapping, Any, TypeVar, Optional

# T = TypeVar('T')  # Generic type variable

# def safely_get_value(dct: Mapping[Any, T], key: Any, default: Optional[T] = None) -> Optional[T]:
#     """
#     Safely get a value from a dictionary. If the key doesn't exist, return the default value.

#     :param dct: a dictionary that maps keys to values of a generic type T
#     :param key: the key to look up in the dictionary
#     :param default: the default value to return if the key is not found (default is None)
#     :return: the value associated with the key, or the default value
#     """
#     if key in dct:
#         return dct[key]
#     else:
#         return default


#!/usr/bin/env python3
"""
Safely get value function with type annotations.
"""

from typing import Mapping, Any, TypeVar, Union, Optional

T = TypeVar('T')  # Generic type variable

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary. If the key doesn't exist, return the default value.

    :param dct: a dictionary with any kind of mapping
    :param key: the key to look up in the dictionary
    :param default: the default value to return if the key is not found (default is None)
    :return: the value associated with the key, or the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default