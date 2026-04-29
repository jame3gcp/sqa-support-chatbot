from __future__ import annotations

import json
import os
from typing import Annotated, Any, Literal, Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class SQAState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    intent: Literal['code_quality', 'sonarqube', 'standards', 'scope', 'unknown']
    confidence: float
    working_query: str
    retrieved_docs: list[dict[str, Any]]
    answer_candidate: str
    is_verified: bool
    verification_feedback: str
    retry_count: int
    suggested_topics: list[str]
    step_logs: list[dict[str, Any]]
