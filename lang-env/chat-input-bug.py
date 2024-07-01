# from langflow.field_typing import Data
from langchain_core.tools import Tool, tool
from langflow.custom import CustomComponent
from langflow.schema import Record


class Component(CustomComponent):
    """
    Custom component that takes a parameter and prints it to the console.

    The component is defined as a class and inherits from `CustomComponent`.

    The `build_config` method returns a dictionary with the configuration parameters for the component.

    The `build` method takes the configuration parameter and returns a `Tool` object. The `Tool` object is a function that takes no arguments and prints the parameter to the console.

    The `icon` attribute is optional and can be used to specify an icon for the component in the UI.

    """
    display_name = "Custom Component"
    description = "Use as a template to create your own component."
    documentation: str = "http://docs.langflow.org/components/custom"
    icon = "custom_components"

    def build_config(self):
        return {"param": {"display_name": "Parameter"}}

    def build(self, param: str) -> Tool:
        @tool
        def print_what_input():
            print(">>>results", param)
            self.repr_value = param

        return print_what_input
