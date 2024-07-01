from typing import Optional

# from langchain.base.io.text import TextComponent
# from hyletic.field_typing import Text
from langchain.prompts import SystemMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langflow.base.io.text import TextComponent
from langflow.field_typing import Text


class TextInput(TextComponent):
    display_name = "Text Input"
    description = "Get text inputs from the Interaction Panel."
    icon = "type"

    def build_config(self):

        return {
            "input_value": {
                "display_name": "Value",
                "input_types": ["str", "Text"],
                "info": "Text or Record to be passed as input.",
                "multiline": True
            }
        }

    def build(self,input_value: Optional[Text] = "",) -> SystemMessagePromptTemplate:
        return SystemMessage(
        content=(input_value)
    )


