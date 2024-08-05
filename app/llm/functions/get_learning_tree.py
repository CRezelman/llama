"""Function Definition for Fetching a Learning Tree"""

from llama_cpp import ChatCompletionToolFunction, ChatCompletionTool

class GetLearningTree:
    """Class definition for getting a learning tree"""
    __function: ChatCompletionToolFunction = {
        "name": "get_learning_tree",
        "description": "Retrieves a learning tree from the database",
        "parameters": {
            "type": "object",
            "title": "learning_tree_request",
            "properties": {
                "validation_key": {
                    "title": "Validation Key",
                    "type": "string"
                }
            },
            "required": [ "validation_key" ]
        }
    }
    @property
    def tool(self) -> ChatCompletionTool:
        """Returns Chat Completition Tool"""
        return {
            "type": "function",
            "function": self.__function,
        }
