from typing import Optional

from langflow.custom import CustomComponent
from langflow.field_typing import Text
from langchain_postgres import PostgresChatMessageHistory

class Component(CustomComponent):
    display_name = "PostgresChatMessageHistory"
    description = "Retrieves stored chat messages given a specific Session ID."
    beta: bool = True
    icon = "history"

    def build_config(self):
        return {
            "session_id": {
                "display_name": "Session ID",
                "info": "Session ID of the chat history.",
                "input_types": [Text],
            },
            "database_url": {
                "display_name": "Database Url",
                "info": "URL of the PostgreSQL database.",
                "input_types": [Text],
            },
            "table_name": {
                "display_name": "Table Name",
                "info": "Name of the table storing the chat messages.",
                "input_types": [Text],
            },
        }

    def build(
            self,
            database_url: str,
            session_id: str,
            table_name: str
    ) -> PostgresChatMessageHistory:
        # Initialize the PostgresChatMessageHistory with the provided parameters
        history = PostgresChatMessageHistory(
            session_id=session_id,
            connection_string=database_url,
            table_name=table_name
        )

        return history
