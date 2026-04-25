from typing import Generic, TypeVar, Type
from pydantic import BaseModel, Field
from langchain.agents import create_agent

SchemaT = TypeVar("SchemaT")

class ProviderStrategy(Generic[SchemaT]):
    schema: type[SchemaT]
    strict: bool | None = None

    def __init__(self, schema: type[SchemaT] | dict, strict: bool | None = None):
        """Initialize the provider strategy with a schema and optional strict flag.

        Args:
            schema: A Pydantic model class or a JSON-schema-like dict describing the output.
            strict: If provided, indicates whether to enforce strict validation.
        """
        self.schema = schema
        self.strict = strict
        
class ContactInfo(BaseModel):
    """Contact information for a person."""
    name: str = Field(description="The name of the person")
    email: str = Field(description="The email address of the person")
    phone: str = Field(description="The phone number of the person")