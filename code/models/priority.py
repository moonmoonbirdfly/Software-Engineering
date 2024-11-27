class Priority:
    def __init__(self, level: str):
        """
        Initializes the Priority object with a given level.
        
        :param level: A string representing the priority level ('Low', 'Medium', 'High')
        """
        self.level = level
        self._level_map = {"Low": 1, "Medium": 2, "High": 3}

        if level not in self._level_map:
            raise ValueError("Invalid priority level. Choose 'Low', 'Medium', or 'High'.")

    def __str__(self):
        """Returns a human-readable string representation of the priority level."""
        return self.level

    def __repr__(self):
        """Returns a more technical representation of the priority."""
        return f"Priority('{self.level}')"

    def __lt__(self, other):
        """Compares if this priority is less than another priority."""
        if not isinstance(other, Priority):
            return NotImplemented
        return self._level_map[self.level] < self._level_map[other.level]

    def __le__(self, other):
        """Compares if this priority is less than or equal to another priority."""
        if not isinstance(other, Priority):
            return NotImplemented
        return self._level_map[self.level] <= self._level_map[other.level]

    def __eq__(self, other):
        """Compares if this priority is equal to another priority."""
        if not isinstance(other, Priority):
            return NotImplemented
        return self._level_map[self.level] == self._level_map[other.level]

    def __gt__(self, other):
        """Compares if this priority is greater than another priority."""
        if not isinstance(other, Priority):
            return NotImplemented
        return self._level_map[self.level] > self._level_map[other.level]

    def __ge__(self, other):
        """Compares if this priority is greater than or equal to another priority."""
        if not isinstance(other, Priority):
            return NotImplemented
        return self._level_map[self.level] >= self._level_map[other.level]

    def to_numeric(self):
        """Returns a numeric representation of the priority for sorting."""
        return self._level_map[self.level]

