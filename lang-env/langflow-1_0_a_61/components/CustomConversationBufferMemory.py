from typing import Optional

from langflow.custom import CustomComponent
from langflow.field_typing import Text
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import PostgresChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.memory import BaseMemory


class Component(CustomComponent):
    display_name = "ConversationBufferMemory"
    description = "Buffer for storing conversation memory.Create a new model by parsing and validating input data from keyword arguments.Raises ValidationError if the input data cannot be parsed to form a valid model."
    beta: bool = True
    icon = "history"

    def build_config(self):
        return {
            "chat_memory": {
                "display_name": "Chat Memory",
                "info": "Session ID of the chat history.",
                "input_types": ["Text"],
            },
            "input_key": {
                "display_name": "Input Key",
                "info": "The variable to be used as Chat Input when more than one variable is available.",
                "input_types": [],
            },
            "output_key": {
                "display_name": "Output Key",
                "info": "The variable to be used as Chat Output (e.g. answer in a ConversationalRetrievalChain)",
                "input_types": [],
            },
            "memory_key": {
                "display_name": "Memory Key",
                "input_types": [],
            },
        }

    def build(
            self,
            chat_memory: BaseChatMessageHistory,
            # input_key: Optional[str] = None,
            # output_key: Optional[str] = None,
            # memory_key: Optional[str] = None,
            return_messages: Optional[bool] = False,
    ) -> BaseMemory:
        memory = ConversationBufferMemory(
            chat_memory=chat_memory,
            # input_key=input_key,
            # output_key=output_key,
            # memory_key=memory_key,
            return_messages=return_messages
        )
        return memory
