def record_spell(spell_name: str, ingredients: str) -> str:
    
    from .validator import validate_ingredients as validate

    valid = validate(ingredients)
    if "INVALID" in valid:
        return f"Spell rejected: {spell_name} ({valid})"
    else:
        return f"Spell recorded: {spell_name} ({valid})"
