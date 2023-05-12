from pydantic import BaseModel, Field


class WebUISetting(BaseModel):
    """ Model for Web UI settings """

    setting: str = Field(max_length=32)
    value: str = Field(max_length=32)

    class Config:
        validate_assignment = True
