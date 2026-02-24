from pydantic import BaseModel, ValidationError, model_validator, Field
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactTypes(Enum):
	"""Available contact types with the aliens"""

	radio = "radio"
	visual = "visual"
	physical = "physical"
	telepathic = "telepathic"

class Validator(BaseModel):
	
	contact_id: str = Field(min_length=5, max_length=15)
	timestamp: datetime
	location: str = Field(min_length=3, max_length=100)
	contact_type: ContactTypes
	signal_strength: float = Field(ga=0, le=10)
	duration_minutes: int = Field(ga=1, le=1440) #(max 24 hours)
	witness_count: int = Field(ga=1, le=100)
	message_received: Optional[str] = Field(max_length=500)
	is_verified: bool = False

	@model_validator(mode='after')
	def validate(self):
		pass

def main():
	print()


if __name__ == "__main__":
	main