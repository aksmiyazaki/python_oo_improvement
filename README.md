# Python - Improving OO Skills with Language

# Python 2 vs Python 3
* Python 2 will stop to receive security upgrades in early 2020
* All useful packages are available for Python 3
* Python 3 is the future of the language.

## Dynamic Typing
PROS:
  - Easy to work with
  - Faster dev. time

Cons:
  - May result in bugs of unexpected data types
  - Need to be aware of type()

## Strings
  - Ordered sequences.
  - Can be treated as Arrays.
  - Strings are immutable objects

## String printing
  - .format()
    - print("This is a string {}".format("INSERTED"))
    - print("The {2} {1} {0}".format('fox', 'brown', 'quick'))
    - print("The {q} {b} {f}".format(f='fox' ,b='brown', q='quick'))
    - Float Formating:
      - print("The result was {r:2.5f}".format(r=result))
  - f-strings (formatted string literals)
    - print(f"Hello, his name is {name}")

  - https://pyformat.info/

## Tuples
  - Immutables, like strings

## Modes of file treatment
  - 'r' - Read only
  - 'w' - write only (ovewrite files or create new)
  - 'a' - append only
  - 'r+' - reading and writing
  - 'w+' - writing and reading (ovewrites existing files)

## Useful Operators
  - enumerate - solves the problem of having an integer iterator when iterating through a list/tuple/dictionary
  - zip - Concatenates items from two lists.
  - randint - Returns a random integer
  - Shuffle - shuffles lists


## Arbitrary no. of arguments
  - \*args - unlimited params no. as a tuple
  - \*\*kwargs - keyword arguments, ulimited pairs of key:value params - dictionary.
  - both can be used combined

## Map Function
  - Applies a function in every element of an array
  - To use the result, must be created a list on its return (returns a map address)

## Filter
  - Applies a boolean function in every element of an array
  - Filters the ones which the function returns true when applied to the element.

## Scope
  - LEGB rule
    - First serches Local
    - Then goes to the enclosing function
    - Then goes global
    - Then goes Built In.
  - global keyword gets variables directly from the global scope. Beware with it.

## General
  - A Function can be declared inside another function.
