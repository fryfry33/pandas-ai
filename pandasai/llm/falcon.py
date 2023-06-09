""" Falcon LLM
This module is to run the Falcon API hosted and maintained by HuggingFace.co.
To generate HF_TOKEN go to https://huggingface.co/settings/tokens after creating Account
on the platform.

Example:
    Use below example to call Falcon Model

    >>> from pandasai.llm.falcon import Falcon
"""


import os
from typing import Optional

from dotenv import load_dotenv

from ..exceptions import APIKeyNotFoundError
from .base import HuggingFaceLLM

load_dotenv()


class Falcon(HuggingFaceLLM):

    """Falcon LLM API

    A base HuggingFaceLLM class is extended to use Falcon model.

    """


    def __init__(self):
        """
        __init__ method of Falcon Class
        Args:
            api_token (str): API token from Huggingface platform
        """
        return None

    @property
    def type(self) -> str:
        return "falcon"
