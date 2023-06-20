"""
This type stub file was generated by pyright.
"""

from typing import Callable, List, Sequence, TYPE_CHECKING, Tuple, Union
from _typeshed import ReadableBuffer
from git import GitCmdObjectDB

"""Module with functions which are supposed to be as fast as possible"""
if TYPE_CHECKING: ...
EntryTup = Tuple[bytes, int, str]
EntryTupOrNone = Union[EntryTup, None]
__all__ = (
    "tree_to_stream",
    "tree_entries_from_data",
    "traverse_trees_recursive",
    "traverse_tree_recursive",
)

def tree_to_stream(
    entries: Sequence[EntryTup], write: Callable[[ReadableBuffer], Union[int, None]]
) -> None:
    """Write the give list of entries into a stream using its write method

    :param entries: **sorted** list of tuples with (binsha, mode, name)
    :param write: write method which takes a data string"""
    ...

def tree_entries_from_data(data: bytes) -> List[EntryTup]:
    """Reads the binary representation of a tree and returns tuples of Tree items

    :param data: data block with tree data (as bytes)
    :return: list(tuple(binsha, mode, tree_relative_path), ...)"""
    ...

def traverse_trees_recursive(
    odb: GitCmdObjectDB, tree_shas: Sequence[Union[bytes, None]], path_prefix: str
) -> List[Tuple[EntryTupOrNone, ...]]:
    """
    :return: list of list with entries according to the given binary tree-shas.
        The result is encoded in a list
        of n tuple|None per blob/commit, (n == len(tree_shas)), where
        * [0] == 20 byte sha
        * [1] == mode as int
        * [2] == path relative to working tree root
        The entry tuple is None if the respective blob/commit did not
        exist in the given tree.
    :param tree_shas: iterable of shas pointing to trees. All trees must
        be on the same level. A tree-sha may be None in which case None
    :param path_prefix: a prefix to be added to the returned paths on this level,
        set it '' for the first iteration
    :note: The ordering of the returned items will be partially lost"""
    ...

def traverse_tree_recursive(
    odb: GitCmdObjectDB, tree_sha: bytes, path_prefix: str
) -> List[EntryTup]:
    """
    :return: list of entries of the tree pointed to by the binary tree_sha. An entry
        has the following format:
        * [0] 20 byte sha
        * [1] mode as int
        * [2] path relative to the repository
    :param path_prefix: prefix to prepend to the front of all returned paths"""
    ...
