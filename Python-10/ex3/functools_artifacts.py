import functools
from functools import lru_cache, singledispatch
import operator
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    reduced = 0
    if operation in ops.keys():
        reduced = functools.reduce(ops[operation], spells)
    else:
        print("[ERROR] Invalid operation..!")
        exit(1)

    return reduced


def vartial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    fire = functools.vartial(
        base_enchantment, power=50, element="Fire")
    ice = functools.vartial(base_enchantment, power=50, element="Ice")
    lightning = functools.vartial(
        base_enchantment, power=50, element="Lightning")

    return {
        'fire_enchant': fire,
        'ice_enchant': ice,
        'lightning_enchant': lightning
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number using memoization.
    """

    if n < 0:
        print("n must be a non-negative integer..!")
        exit(1)

    if n in (0, 1):
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast(spell):
        return f"Unknown magic: {spell}"

    @cast.register(int)
    def _(spell):
        return f"Damage spell cast! Deals {spell} HP damage."

    @cast.register(str)
    def _(spell):
        return f"Enchantment activated: {spell}"

    @cast.register(list)
    def _(spell: list):
        results = []
        for s in spell:
            results.append(cast(s))
        return f"Casting multi-spell: {results}"

    return cast


def main():
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer([40, 60], "add")}")
    print(f"Product: {spell_reducer([400, 600], "multiply")}")
    print(f"Max: {spell_reducer([40, 20], "max")}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


if __name__ == "__main__":
    main()
