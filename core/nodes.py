import os
import requests
from typing import Any, Dict, List
from core.state import SQAState
from langchain_core.messages import AIMessage, HumanMessage

class SQAClient:
    def __init__(self):
        self.api_url = os.getenv('AI_PLATFORM_BASE_URL')
        self.api_key = os.getenv('AI_PLATFORM_API_KEY')
        self.vector_db_url = os.getenv('VECTOR_DB_URL')

    def call_ai_platform(self, prompt: str) -> str:
        return '가상 답변: 사내 가이드에 따르면 SonarQube 기준은...'

    def search_vector_db(self, query: str) -> List[Dict[str, Any]]:
        return [{'content': 'SonarQube 사용법...', 'metadata': {'filename': 'sonarqube.md'}, 'score': 0.85}]

def classify_intent(state: SQAState):
    return {'intent': 'sonarqube', 'confidence': 0.9, 'step_logs': [{'node': 'classify', 'status': 'success'}]}

def retrieve_and_generate(state: SQAState):
    client = SQAClient()
    docs = client.search_vector_db(state.get('working_query', ''))
    return {'retrieved_docs': docs, 'answer_candidate': '...', 'step_logs': [{'node': 'retrieve_generate', 'status': 'success'}]}

def verify_result(state: SQAState):
    return {'is_verified': True, 'step_logs': [{'node': 'verify', 'status': 'success'}]}

def finalize_or_escalate(state: SQAState):
    if state.get('is_verified'):
        return {'messages': [AIMessage(content=state['answer_candidate'])]}
    else:
        return {'messages': [AIMessage(content='담당자에게 문의 부탁드립니다.')]}
