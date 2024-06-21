# from langflow.field_typing import Data
import os
from typing import Optional

from langflow.custom import CustomComponent
from langflow.schema import Record


class Component(CustomComponent):
    display_name = "LangSmith Switch Component"
    description = "Use as a template to create your own component."
    documentation: str = "http://docs.langflow.org/components/custom"
    icon = "🛠 "

    def build_config(self):
        return {"status":
            {
                "display_name": "Status",
                "options": ["off", "on"],
                "default": "off"
            },
            "langchain_api_key": {
                "display_name": "langsmith api key"
            },
            "langchain_project_name": {
                "display_name": "langsmith project name"
            }
        }

    def build(self, status: str, langchain_api_key: Optional[str], langchain_project_name: Optional[str] = "lang-env"):
        if status == "off":
            os.environ["LANGCHAIN_TRACING_V2"] = "false"
        elif status == "on":
            os.environ["LANGCHAIN_TRACING_V2"] = "true"
            os.environ["LANGCHAIN_PROJECT"] = langchain_project_name
            os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
        self.repr_value = status

        print(
            f"LangSmith status: {self.repr_value}, "
            f"now project: {os.getenv('LANGCHAIN_PROJECT')}, "
            f"key:{os.getenv('LANGCHAIN_API_KEY')}")
        # return status
