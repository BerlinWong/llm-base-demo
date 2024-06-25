# from hyletic import CustomComponent

from langchain_core.tools import Tool, tool
from langflow.custom import CustomComponent


class Component(CustomComponent):
    display_name = "Custom Component"
    description = "Use as a template to create your own component."
    documentation: str = "http://docs.langflow.org/components/custom"
    icon = "custom_components"

    def build_config(self):
        return {"param": {"display_name": "Parameter"}}

    def build(self) -> Tool:
        @tool
        def return_hello():
            """当我说调用返回hello的时候，这个方法的时候执行"""
            return "hello"
        return return_hello



