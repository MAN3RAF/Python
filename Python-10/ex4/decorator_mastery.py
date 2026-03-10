import functools
import time
from typing import Callable


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Validate if current_power >= min_power"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # In a class method (self, spell_name, power),
            # power is at index 2
            # We check if 'power' was passed as keyword or positional arg
            current_power = (
                kwargs.get('power') or (args[2] if len(args) > 2 else None)
            )

            if current_power is not None and current_power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    func_res = func(*args, **kwargs)
                    print(f"Attempt {i} → seccess")
                    return func_res
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {i}/{max_attempts})"
                    )
            return "Spell casting failed after max_attempts attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        name_len = len(name)
        if name_len < 3:
            return False
        for i in name:
            if not (i.isalpha() or i == " "):
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def main():

    @spell_timer
    def fireball():
        return "Fireball cast!"

    print("\nTesting spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting MageGuild...")
    m = MageGuild()
    print(m.validate_mage_name("Good "))
    print(m.validate_mage_name("Bad..!"))

    print(m.cast_spell("Fire_Ball", 15))
    print(m.cast_spell("Fire_Ball", 1))


if __name__ == "__main__":
    main()
