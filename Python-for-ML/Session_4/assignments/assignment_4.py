# =========================
# Task 1: Fibonacci
# =========================
class Fibonacci:
    """
    Generates Fibonacci sequence using recursion.

    Attributes:
        n (int): Number of elements to generate.
    """

    def __init__(self, n):
        self.n = n

    def generate(self):
        """Returns Fibonacci sequence of length n."""
        return self._fibonacci(self.n)

    def _fibonacci(self, n):
        if n == 0:
            return []
        if n == 1:
            return [0]

        fibs = self._fibonacci(n - 1)
        fibs.append(fibs[-1] + (fibs[-2] if len(fibs) > 1 else 1))
        return fibs


# =========================
# Task 2: Remove One Item
# =========================
class RemoveItem:
    """
    Removes a single item from a list recursively.

    Attributes:
        item: Item to remove.
        lst (list): Input list.
    """

    def __init__(self, item, lst):
        self.item = item
        self.lst = lst

    def remove(self):
        """Returns list after removing the item."""
        return self._remove(self.lst)

    def _remove(self, lst):
        if not lst:
            return []
        if lst[0] == self.item:
            return self._remove(lst[1:])
        return [lst[0]] + self._remove(lst[1:])


# =========================
# Task 3: Remove Multiple Items
# =========================
class RemoveMultipleItems:
    """
    Removes multiple items from a list recursively.

    Attributes:
        items (list): Items to remove.
        lst (list): Input list.
    """

    def __init__(self, items, lst):
        self.items = items
        self.lst = lst

    def remove(self):
        """Returns list after removing specified items."""
        return self._remove(self.lst)

    def _remove(self, lst):
        if not lst:
            return []
        if lst[0] in self.items:
            return self._remove(lst[1:])
        return [lst[0]] + self._remove(lst[1:])


# =========================
# Task 4: Find Index in Tuple
# =========================
class FindIndex:
    """
    Finds index of an item in a tuple recursively.

    Attributes:
        item: Item to find.
        tpl (tuple): Input tuple.
    """

    def __init__(self, item, tpl):
        self.item = item
        self.tpl = tpl

    def find(self):
        """Returns index of item or -1 if not found."""
        return self._find(0)

    def _find(self, index):
        if index >= len(self.tpl):
            return -1
        if self.tpl[index] == self.item:
            return index
        return self._find(index + 1)


# =========================
# Task 5: Sentence to Words
# =========================
class SentenceToWords:
    """
    Converts a sentence into a list of words.

    Attributes:
        sentence (str): Input sentence.
    """

    def __init__(self, sentence):
        self.sentence = sentence

    def convert(self):
        """Returns list of words."""
        return self.sentence.split()


# =========================
# Task 6: Palindrome Check
# =========================
class Palindrome:
    """
    Checks whether a string is a palindrome.

    Attributes:
        text (str): Input string.
    """

    def __init__(self, text):
        self.text = text.replace(" ", "").lower()

    def check(self):
        """Returns True if palindrome, else False."""
        return self._check(self.text)

    def _check(self, s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return self._check(s[1:-1])


# =========================
# Task 7: Factorial
# =========================
class Factorial:
    """
    Calculates factorial using recursion.

    Attributes:
        n (int): Input number.
    """

    def __init__(self, n):
        self.n = n

    def calculate(self):
        """Returns factorial of n."""
        return self._factorial(self.n)

    def _factorial(self, n):
        if n <= 1:
            return 1
        return n * self._factorial(n - 1)


# =========================
# Task 8: Squares List
# =========================
class Squares:
    """
    Generates list of squares from 1 to n.

    Attributes:
        n (int): Upper limit.
    """

    def __init__(self, n):
        self.n = n

    def generate(self):
        """Returns list of squares."""
        return self._generate(self.n)

    def _generate(self, n):
        if n == 0:
            return []
        return self._generate(n - 1) + [n * n]


# =========================
# Task 9: Sum of Even Numbers
# =========================
class SumEven:
    """
    Calculates sum of even numbers in a list.

    Attributes:
        lst (list): Input list.
    """

    def __init__(self, lst):
        self.lst = lst

    def calculate(self):
        """Returns sum of even numbers."""
        total = 0
        for n in self.lst:
            if n % 2 == 0:
                total += n
        return total


# =========================
# Task 10: Reverse List
# =========================
class ReverseList:
    """
    Reverses a list using recursion.

    Attributes:
        lst (list): Input list.
    """

    def __init__(self, lst):
        self.lst = lst

    def reverse(self):
        """Returns reversed list."""
        return self._reverse(self.lst)

    def _reverse(self, lst):
        if not lst:
            return []
        return [lst[-1]] + self._reverse(lst[:-1])


# =========================
# Task 11: Median
# =========================
class Median:
    """
    Calculates the median of a list.

    Attributes:
        lst (list): Input list.
    """

    def __init__(self, lst):
        self.lst = sorted(lst)

    def calculate(self):
        """Returns median value."""
        n = len(self.lst)
        mid = n // 2
        if n % 2 == 0:
            return (self.lst[mid - 1] + self.lst[mid]) / 2
        return self.lst[mid]


# =========================
# Task 12: Mode
# =========================
class Mode:
    """
    Calculates mode(s) of a list.

    Attributes:
        lst (list): Input list.
    """

    def __init__(self, lst):
        self.lst = lst

    def calculate(self):
        """Returns list of mode(s)."""
        frequency = {}
        for item in self.lst:
            frequency[item] = frequency.get(item, 0) + 1

        max_freq = max(frequency.values())
        return [k for k, v in frequency.items() if v == max_freq]


# =========================
# Task 13: Mark to Grade
# =========================
class Grade:
    """
    Converts mark to grade.

    Attributes:
        mark (int): Student mark.
    """

    def __init__(self, mark):
        self.mark = mark

    def convert(self):
        """Returns grade."""
        if 85 <= self.mark <= 100:
            return 'A'
        elif 75 <= self.mark < 85:
            return 'B'
        elif 65 <= self.mark < 75:
            return 'C'
        elif 50 <= self.mark < 65:
            return 'D'
        elif 0 <= self.mark < 50:
            return 'F'
        return 'Invalid mark'


# =========================
# Testing All Tasks
# =========================
if __name__ == "__main__":
    print(Fibonacci(10).generate())
    print(RemoveItem(2, [1, 2, 3, 2, 4, 2, 5]).remove())
    print(RemoveMultipleItems([2, 4], [1, 2, 3, 2, 4, 2, 5]).remove())
    print(FindIndex(3, (1, 2, 3, 4, 3, 5)).find())
    print(SentenceToWords("Welcome to Amit").convert())
    print(Palindrome("A man a plan a canal Panama").check())
    print(Factorial(5).calculate())
    print(Squares(10).generate())
    print(SumEven([1, 2, 3, 4, 5, 6]).calculate())
    print(ReverseList([1, 2, 3, 4, 5]).reverse())
    print(Median([3, 6, 1, 4, 2, 5]).calculate())
    print(Mode([1, 2, 2, 3, 3, 4, 4, 4, 5]).calculate())
    print(Grade(85).convert())
