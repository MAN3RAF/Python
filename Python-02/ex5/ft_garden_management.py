#!/usr/bin/env python3


class GardenError(Exception):
    """Base class for health-related errors."""
    pass


class SunError(GardenError):
    """Error for sunlight issues."""
    pass


class PlantError(GardenError):
    """Error for plant issues."""
    pass


class WaterError(GardenError):
    """Error for water issues."""
    pass


class Plant:
    """Represents a plant."""
    def __init__(self, name, water_level,
                 sunlight_hours):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    """Manages garden operations."""
    def __init__(self):
        pass

    def add_plant(self, plants):
        """Add plants to the garden."""
        print("Adding plants to garden...")
        try:
            for plant in plants:
                if not plant.name:
                    raise PlantError(
                        "Error adding plant: Plant name cannot be empty!")
                else:
                    print(f"Added {plant.name} successfully")

        except PlantError as e:
            print(e)

    def water_plants(self, plants):
        """Water the plants."""
        print("Watering plants...")
        print("Opening watering system")
        try:
            for plant in plants:
                int(plant.water_level)
                print(f"Watering {plant.name} - success")

        except ValueError:
            print("Error watering plant: water_level not a number!")

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plants):
        """Check the health of plants."""
        print("Checking plant health...")
        try:
            for plant in plants:
                w = plant.water_level
                s = plant.sunlight_hours
                if not (1 <= w <= 10) and not (2 <= s <= 12):
                    raise GardenError(
                        f"Error checking {plant.name}: Water Level {w} "
                        f"is too high or too low and Sunlight hours {s} "
                        "is too high or too low")
                elif w > 10:
                    raise WaterError(
                        f"Error checking {plant.name}: Water level {w} "
                        "is too high (max 10)")
                elif w < 1:
                    raise WaterError(
                        f"Error checking {plant.name}: Water level {w} "
                        "is too low (min 1)")
                elif s < 2:
                    raise SunError(
                        f"Error: checking {plant.name} Sunlight hours {s} "
                        "is too low (min 2)")
                elif s > 12:
                    raise SunError(
                        f"Error: checking {plant.name} Sunlight hours {s} "
                        "is too high (max 12)")
                else:
                    print(f"{plant.name}: healthy (water: {w}, sun: {s})")

        except WaterError as e:
            print(e)

        except SunError as e:
            print(e)

        except GardenError as e:
            print(e)

    def check_watertank(self, water_tank):
        """Check the water tank level."""
        print("Testing error recovery...")
        try:
            if water_tank < 10:
                raise WaterError(
                    "Caught GardenError: Not enough water in tank")
            elif water_tank > 10:
                print("There is enough water in tank")
        except WaterError as e:
            print(e)

        finally:
            print("System recovered and continuing...")


def test_garden_management():
    """Test the garden managment"""
    print("=== Garden Management System ===")

    print("")

    tomato = Plant("tomato", 5, 8)
    lettuce = Plant("lettuce", 15, 5)
    empty_name = Plant("", 10, 10)

    plants = [tomato, lettuce, empty_name]

    manager = GardenManager()

    manager.add_plant(plants)
    plants.remove(empty_name)
    print("")

    manager.water_plants(plants)

    print("")

    manager.check_plant_health(plants)

    print("")

    manager.check_watertank(0)

    print("")

    print("Garden management system test complete!")


test_garden_management()
