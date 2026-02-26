from pydantic import BaseModel, ValidationError, model_validator, Field
from datetime import datetime
from enum import Enum


class CrewRanks(Enum):

    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=3, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def validate(self):
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        if not any(
            c.rank.value in ["captain", "commander"] for c in self.crew
        ):
            raise ValueError(
                "Must have at least one Commander or Captain")

        avg_exp = sum(
            c.years_experience for c in self.crew) / len(self.crew)
        if self.duration_days > 365 and avg_exp < 5:
            raise ValueError(
                "Long missions (> 365 days) need 50% experienced crew "
                "(5+ years)")

        if not all(c.is_active for c in self.crew):
            raise ValueError("All crew members must be active")
        else:
            return self


def main():

    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")

    try:
        crew_member1 = CrewMember(
            member_id="001",
            name="Sarah Connor",
            rank=CrewRanks.commander,
            age=47,
            specialization="Mission Command",
            years_experience=20,
            is_active=True
        )
        crew_member2 = CrewMember(
            member_id="002",
            name="John Smith",
            rank=CrewRanks.lieutenant,
            age=41,
            specialization="Navigation",
            years_experience=15,
            is_active=True
        )
        crew_member3 = CrewMember(
            member_id="003",
            name="Alice Johnson",
            rank=CrewRanks.officer,
            age=38,
            specialization="Engineering",
            years_experience=10,
            is_active=True
        )

        space_crew = [crew_member1, crew_member2, crew_member3]

        s = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-02-24T14:30:00",
            duration_days=900,
            crew=space_crew,
            mission_status="planned",
            budget_millions=2500.0
        )

        print(f"Mission: {s.mission_name}")
        print(f"ID: {s.mission_id}")
        print(f"Destination: {s.destination}")
        print(f"Duration: {s.duration_days} days")
        print(f"Budget: ${s.budget_millions}M")
        print(f"Crew size: {len(space_crew)}")
        print("Crew members:")

        for m in space_crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

        print("\n=========================================")
        print("Expected validation error:")

        crew_member1 = CrewMember(
            member_id="001",
            name="Sarah Connor",
            rank=CrewRanks.cadet,
            age=47,
            specialization="Mission Command",
            years_experience=20,
            is_active=True
        )
        crew_member2 = CrewMember(
            member_id="002",
            name="John Smith",
            rank=CrewRanks.lieutenant,
            age=41,
            specialization="Navigation",
            years_experience=15,
            is_active=True
        )
        crew_member3 = CrewMember(
            member_id="003",
            name="Alice Johnson",
            rank=CrewRanks.officer,
            age=38,
            specialization="Engineering",
            years_experience=10,
            is_active=True
        )

        space_crew = [crew_member1, crew_member2, crew_member3]

        s = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-02-24T14:30:00",
            duration_days=900,
            crew=space_crew,
            mission_status="planned",
            budget_millions=2500.0
        )

        print("")

    except ValidationError as e:
        # list of detailes of the errors that happened
        for err in e.errors():
            msg = err['msg']
            # Strip "Value error, " prefix if present
            if msg.startswith("Value error, "):
                msg = msg[13:]  # Remove "Value error, " (13 characters)
            print(msg)


if __name__ == "__main__":
    main()
