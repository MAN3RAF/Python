from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Validate(BaseModel):

	station_id: str = Field(min_length=3, max_length=10)
	name: str = Field(min_length=1, max_length=50)
	crew_size:int = Field(ge=1, le=20)


def main() -> None:

	v = Validate(station_id="S-001", name="Galaxy_Center")

	print(f"{v.station_id} \n{v.name}")



if __name__ == "__main__":
	main()
