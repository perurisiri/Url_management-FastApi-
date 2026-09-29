from pydantic import BaseModel, model_validator


class BaseRequestModel(BaseModel):

    @model_validator(mode="after")
    def validate_required_string_fields(self):
        for field_name, field_info in self.__class__.model_fields.items():

            if not field_info.is_required():
                continue

            value = getattr(self, field_name, None)

            if isinstance(value, str):

                if not value.strip():
                    raise ValueError(
                        f"{field_name} cannot be empty"
                    )

                if value.strip().lower() == "string":
                    raise ValueError(
                        f"Please provide a valid {field_name}"
                    )

        return self