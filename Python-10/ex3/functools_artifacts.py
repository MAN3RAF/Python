import functools
from functools import lru_cache, singledispatch
import operator


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

    return reduced

def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:

    fire = functools.partial(base_enchantment, power=50, element="Fire")
    ice = functools.partial(base_enchantment, power=50, element="Ice")
    lightning = functools.partial(base_enchantment, power=50, element="Lightning")

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
        raise ValueError("n must be a non-negative integer")

    if n in (0, 1):
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

@singledispatch
def spell_dispatcher() -> callable:
    
    def dispatcher():



        pass

# def base_enchantment(target: str, power: int, element: str):
#     return f"Enchanting {target} with {element} (Power: {power})"

def main():
    # ---spell_reducer test--- #
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer([40,60], "add")}")
    print(f"Product: {spell_reducer([400,600], "multiply")}")
    print(f"Max: {spell_reducer([40,20], "max")}")

    # ---partial_enchanter test--- #
    # spells = partial_enchanter(base_enchantment)
    # print(spells['fire_enchant']("Iron Sword"))
    # print(spells['ice_enchant']("Iron Sword"))
    # print(spells['lightning_enchant']("Iron Sword"))

    # ---memoized_fibonacci test--- #
    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    # ---spell_dispatcher test--- #



    pass

if __name__ == "__main__":
    main()
