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
	message_received: Optional[str] = Field(default=None, max_length=500)
	is_verified: bool = False

	@model_validator(mode='after')
	def validate(self):
		if self.contact_type.value not in [ct.value for ct in ContactTypes]:
			raise ValueError("Contact Type not allowed")
		if not self.contact_id.startswith("AC"):
			raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
		if (self.contact_type.value == "physical") and not self.is_verified:
			raise ValueError(" Physical contact reports must be verified")
		if (self.contact_type.value == "telepathic") and not (self.witness_count >= 3):
			raise ValueError("Telepathic contact requires at least 3 witnesses")
		if self.signal_strength > 7 and not self.message_received:
			raise ValueError("Strong signals (> 7.0) should include received messages")
		return self


def main():
	
	print("Alien Contact Log Validation")
	print("======================================")
	print("Valid contact report:")
	try:
		v = Validator(
			contact_id="AC_2024_001",
			timestamp="2026-02-24T14:30:00",
			location=" Area 51, Nevada",
			contact_type="radio",
			signal_strength=8.5,
			duration_minutes="45",
			witness_count=5,
			message_received="Greetings from Zeta Reticuli",
			is_verified=True
		)
		print(
			f"ID: {v.contact_id}\n"
			f"Type: {v.contact_type.value}\n"
			f"Location: {v.location}\n"
			f"Signal: {v.signal_strength}/10\n"
			f"Witnesses: {v.witness_count}\n"
			f"Message: '{v.message_received}'\n"
		)
	except ValidationError as e:
		for err in e.errors(): #list of detailes of the errors that happened
			msg = err['msg']
			# Strip "Value error, " prefix if present
			if msg.startswith("Value error, "):
				msg = msg[13:]  # Remove "Value error, " (13 characters)
			print(msg)

	print("======================================")
	print("Expected validation error:")
	try:
		v = Validator(
			contact_id="AC_2024_001",
			timestamp="2026-02-24T14:30:00",
			location=" Area 51, Nevada",
			contact_type="telepathic",
			signal_strength=8.5,
			duration_minutes="45",
			witness_count=1,
			message_received="Greetings from Zeta Reticuli",
			is_verified=True
		)
	except ValidationError as e:
		for err in e.errors(): #list of detailes of the errors that happened
			print(err['msg'])
	except ValueError as e:
		print(e)

if __name__ == "__main__":
	main()
