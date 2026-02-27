
def spell_combiner(spell1, spell2):
    """Creates a new function that runs two spells at once."""
    def combined_spell(*args, **kwargs):

        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return f"{res1} {res2}"
    
    return combined_spell

def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    
    def amplified_power(*args, **kwargs):

        base_res = base_spell(*args, **kwargs)
        res = base_res * multiplier
        return res

    return amplified_power

def conditional_caster(condition: callable, spell: callable) -> callable:

    def cast_spell(*args, **kwargs):

        if condition(*args, **kwargs):
            spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    
    return cast_spell


def spell_sequence(spells: list[callable]) -> callable:
    
    def cast_spells(*args, **kwargs):
        spells_casted = []

        for spell in spells:
            res = spell(*args, **kwargs)
            spells_casted.append(res)
        
        return spells_casted
    
    return cast_spells


def main():

   # Setup for your specific image output
    def fireball(target): return f"Fireball hits {target}"
    def heal(target): return f"Heals {target}"
    def original(x): return x

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon')}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(original, 3)
    print(f"Original: 10, Amplified: {amplified(10)}")

if __name__ == "__main__":
    main()
