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

    fire = functools.partial(base_enchantment, power=50, element="Fire")
    ice = functools.partial(base_enchantment, power=50, element="Ice")
    lightning = functools.partial(base_enchantment, power=50, element="Lightning")

    return {
        'fire_enchant': fire,
        'ice_enchant': ice,
        'lightning_enchant': lightning
    }

def memoized_fibonacci(n: int) -> int:
    pass

def spell_dispatcher() -> callable:
    pass

def base_enchantment(target: str, power: int, element: str):
    return f"Enchanting {target} with {element} (Power: {power})"

def main():
    # ---spell_reducer test--- #
    # print(spell_reducer([2,5], "add"))

    # ---partial_enchanter test--- #
    # spells = partial_enchanter(base_enchantment)
    # print(spells['fire_enchant']("Iron Sword"))
    # print(spells['ice_enchant']("Iron Sword"))
    # print(spells['lightning_enchant']("Iron Sword"))

    # ---memoized_fibonacci test--- #

    pass

if __name__ == "__main__":
    main()
