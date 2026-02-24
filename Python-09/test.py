from pydantic import BaseModel, Field

class adi(BaseModel):
	chihaja: int = Field(ge=1, le=10)


test = adi(chihaja="5")

print(test.chihaja)
