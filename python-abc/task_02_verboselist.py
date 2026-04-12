#!/usr/bin/python3
"""VerboseList: a list subclass that prints messages on mutations."""


class VerboseList(list):
    """List subclass that logs when items are added or removed."""

    def append(self, item):
        """Append item and print a notification."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend list and print how many items were added."""
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        """Print a notification then remove item."""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Print a notification then pop and return the item."""
        item = self[index]  # may raise IndexError, matching list behavior
        print(f"Popped {item} from the list.")
        return super().pop(index)


if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])

    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)
