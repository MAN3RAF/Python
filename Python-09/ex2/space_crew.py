from pydantic import BaseModel, ValidationError, model_validator, Field
from datetime import datetime
from typing import Optional
from enum import Enum


class CrewRanks(Enum):

	cadet = "cadet"
	officer = "officer"
	lieutenant = "lieutenant"
	captain = "captain"
	commander = "commander"


class Validator(BaseModel):

	member_id: str = Field(min_length=3, max_length=10)
	name: str = Field(min_length=2, max_length=50)
	rank: CrewRanks
	age: int = Field(ga=18, le=80)
	specialization: str = Field(min_length=3, max_length=30)
	years_experience: int = Field(ga=0, le=50)
	is_active: bool = True




def main():
	pass


if __name__ == "__main__":
	main()
