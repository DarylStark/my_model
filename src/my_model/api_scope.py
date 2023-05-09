from pydantic import BaseModel, Field


class APIScope(BaseModel):
    """ Model for API scopes """

    module: str = Field(max_length=32)
    subject: str = Field(max_length=32)

    @property
    def full_scope_name(self) -> str:
        """ Method that creates a 'full API scope' object. """
        return f'{self.module}.{self.subject}'
