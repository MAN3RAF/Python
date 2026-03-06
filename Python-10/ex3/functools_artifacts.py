import functools
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
    
    def enchant():
        pass

    return {
        "" : "func",
    }

def memoized_fibonacci(n: int) -> int:
    pass

def spell_dispatcher() -> callable:
    pass

def main():
    print(spell_reducer([2,5], "add"))

if __name__ == "__main__":
    main()
