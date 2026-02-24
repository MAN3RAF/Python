from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class Validate(BaseModel):

	station_id: str = Field(min_length=3, max_length=10)
	name: str = Field(min_length=1, max_length=50)
	crew_size:int = Field(ge=1, le=20)
	power_level: float = Field(ge=0, le=100)
	oxygen_level: float = Field(ge=0, le=100)
	last_maintenance: datetime
	is_operational: bool = True
	notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:

	print("Space Station Data Validation")
	print("========================================")
	print("Valid station created:")
	try:
		v = Validate(station_id="ISS001", name="International Space Station",
			   crew_size=6, power_level="85.5", oxygen_level= 92.3,
			   last_maintenance= "2026-02-24T14:30:00", is_operational=True
			)
		print(
			f"ID: {v.station_id}\n"
			f"Name: {v.name}\n"
			f"Crew: {v.crew_size} people\n"	
			f"power: {v.power_level}%\n"
			f"Oxygen: {v.oxygen_level}%"
		)
		print(f"Status: {'Operational' if v.is_operational else 'Not Operational'}")
	except ValidationError as e:
		for err in e.errors(): #list of detailes of the errors that happened
			print(err['msg'])

	print("\n========================================")
	print("Expected validation error:")
	# causing error in crew_size:
	try:
		v = Validate(station_id="ISS001", name="International Space Station",
			   crew_size=21, power_level=85.5, oxygen_level= 92.3,
			   last_maintenance= "2026-02-24T14:30:00", is_operational=True
			)
	except ValidationError as e:
		for err in e.errors(): #list of detailes of the errors that happened
			print(err['msg'])


if __name__ == "__main__":
	main()
