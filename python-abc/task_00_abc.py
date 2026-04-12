#!/usr/bin/python3
"""Abstract Animal class with Dog and Cat implementations."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        raise NotImplementedError


class Dog(Animal):
    """Dog class."""

    def sound(self):
        """Return the dog sound."""
        return "Bark"


class Cat(Animal):
    """Cat class."""

    def sound(self):
        """Return the cat sound."""
        return "Meow"
