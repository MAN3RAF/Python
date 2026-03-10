from typing import Callable


def mage_counter() -> Callable:

    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:

    spell_power = initial_power

    def accumulate_power(power: int):
        nonlocal spell_power
        spell_power += power
        return spell_power
    return accumulate_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchant(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:

    storage = {}

    def store(key, value):
        storage[key] = value

    def recall(key):
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main():

    print("\nTesting mage counter...")
    mage = mage_counter()
    print(f"Call 1: {mage()}")
    print(f"Call 2: {mage()}")
    print(f"Call 3: {mage()}")

    print("\nTesting enchantment factory...")
    enchant = enchantment_factory("Flaming")
    print(enchant("Sword"))
    enchant = enchantment_factory("Frozen")
    print(enchant("Shield"))


if __name__ == "__main__":
    main()
