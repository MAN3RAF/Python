
def spell_combiner(spell1, spell2):
    """Creates a new function that runs two spells at once."""
    def combined_spell(*args):

        res1 = spell1(*args)
        res2 = spell2(*args)
        return (res1, res2)
    
    return combined_spell

def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    pass

def conditional_caster(condition: callable, spell: callable) -> callable:
    pass

def spell_sequence(spells: list[callable]) -> callable:
    pass

