#!/usr/bin/python3
"""CountedIterator: wraps an iterator and counts items returned."""


class CountedIterator:
    """Iterator wrapper that counts how many items have been fetched."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)  # raises StopIteration when exhausted
        self._count += 1
        return item

    def get_count(self):
        """Return the number of items fetched so far."""
        return self._count


if __name__ == "__main__":
    it = CountedIterator([10, 20, 30])

    for x in it:
        print(x)

    print("Count:", it.get_count())
