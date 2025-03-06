"""Example pydantic models."""

import enum
import json
from typing import Annotated
import pydantic

Name = Annotated[
    str,
    pydantic.Field(
        title="Project name",
        description="A name for this docscraft project. (This text shows up in the JSON schema)",
        examples=["snapcraft", "charmcraft", "rockcraft"],
        max_length=79,
    )
]

class DocType(enum.Enum):
    """The type of documentation in this project."""

    END_USER = "end-user"
    """End user documentation.

    This is documentation for people who are using the product. For example, the end
    user of snapcraft's documentation is someone who's building or maintaining a snap.
    """
    DEVELOPER = "developer"
    """Developer documentation.

    This is documentation for someone who wants to contribute to the product's source
    code. It will often contain things like how to set up your development environment
    and linting rules.
    """
    DOCUMENTER = "documenter"
    """Documenter documentation.

    This is documentation aimed at someone who wants to work on the documentation for
    a product. It should contain things like how to set up a documentation environment,
    a style guide, etc. Examples include:

    - `The Ubuntu style guide <https://docs.ubuntu.com/styleguide/en/>`_
    - https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/
    """


class Docscraft(pydantic.BaseModel):
    """``docscraft.yaml``

    This file describes how Docscraft will build your documentation.
    Because this model is the top level for the file, this docstring will only show up
    in :doc:`the documentation <index>`, ~~not in the JSON schema~~.
    You can use any rst or Sphinx directives you want! Yay!
    """

    name: Name
    """The name of this docsraft project.

    This text shows up on the documentation page.
    """

    type: DocType


with open("schema.json", "w+") as f:
    print(json.dumps(Docscraft.model_json_schema(), indent=2), file=f)
