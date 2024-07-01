from typing import Optional


from langchain_community.chat_message_histories import PostgresChatMessageHistory
from langflow.custom import CustomComponent


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
            },
            "database_url": {
                "display_name": "Database Url",
                "input_types": [],
            },
            "table_name": {
                "display_name": "Table Name",
                "input_types": [],
            },
        }

    def build(
        self,
        database_url: str,
        session_id: str,
        table_name: str
    ) -> PostgresChatMessageHistory:
        history = PostgresChatMessageHistory(
            session_id=session_id,
            connection_string=database_url,
            table_name=table_name
        )
        # dialogue = ""
        # # 从所有的消息记录中取最近100条
        # for message in history.messages[-100:]:
        #     if message.type == "human":
        #         dialogue += f"Human: {message.content}\n"
        #     elif message.type == "ai":
        #         dialogue += f"AI: {message.content}\n"

        return history
