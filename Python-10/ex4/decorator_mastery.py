from functools import wraps
import functools
import time


def spell_timer(func: callable) -> callable:
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Spell Completed in {end - start:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # In a class method (self, spell_name, power), power is at index 2
            # We check if 'power' was passed as a keyword or positional argument
            current_power = kwargs.get('power') or (args[2] if len(args) > 2 else None)

            if current_power is not None and current_power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator

def retry_spell(max_attempts: int) -> callable:
    pass


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass
    
    def cast_spell(self, spell_name: str, power: int) -> str:
        pass

def func():
    return "GG!"

def main():

    # ---spell_timer test--- #
    # s = spell_timer(func)
    # s()

    # ---power_validator test--- #

    p = power_validator(5)

    print(p(func))


if __name__ == "__main__":
    main()