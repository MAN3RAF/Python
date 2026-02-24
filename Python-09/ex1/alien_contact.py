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
	signal_strength: float = Field(ge=0, le=10)
	duration_minutes: int = Field(ge=1, le=1440) #(max 24 hours)
	witness_count: int = Field(ge=1, le=100)
	message_received: Optional[str] = Field(max_length=500)
	is_verified: bool = False

	@model_validator(mode='after')
	def validate(self):
		allowed = {contact_type.value for contact_type in ContactTypes}
		if self.contact_type not in allowed:
			print("ERROR!")
		if not self.contact_id.startswith("AC"):
			print("ERROR!")
		if (self.contact_type == "physical") and not self.is_verified:
			print("ERROR!")
		if (self.contact_type == "telepathic") and not (self.witness_count >= 3):
			print("ERROR!")
		if self.signal_strength > 7 and not self.message_received:
			print("ERROR!")

def main():
	
	print("Alien Contact Log Validation")
	print("======================================")
	print("Valid contact report:")


if __name__ == "__main__":
	main()