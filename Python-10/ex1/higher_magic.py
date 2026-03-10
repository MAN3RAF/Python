from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combined_spell(*args, **kwargs):

        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return f"{res1} {res2}"

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amplified_power(*args, **kwargs):

        base_res = base_spell(*args, **kwargs)
        res = base_res * multiplier
        return res

    return amplified_power


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def cast_spell(*args, **kwargs):

        if condition(*args, **kwargs):
            spell(*args, **kwargs)
        else:
            return "Spell fizzled"

    return cast_spell


def spell_sequence(spells: list[Callable]) -> Callable:

    def cast_spells(*args, **kwargs):
        spells_casted = []

        for spell in spells:
            res = spell(*args, **kwargs)
            spells_casted.append(res)

        return spells_casted

    return cast_spells


def main():

    def fireball(target): return f"Fireball hits {target},"
    def heal(target): return f"Heals {target}"
    def original(x): return x

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon')}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(original, 3)
    print(f"Original: 10, Amplified: {amplified(10)}")


if __name__ == "__main__":
    main()
