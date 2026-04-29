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
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "X-Client-ID": "SQA-Chatbot"
        }
        payload = {
            "request_id": os.urandom(8).hex(),
            "query": prompt,
            "options": {"temperature": 0.1, "top_p": 0.9}
        }
        try:
            return f"가상 답변 (API 호출 시뮬레이션): 요청한 {prompt[:20]}...에 대한 분석 결과입니다."
        except Exception as e:
            return f"API 호출 오류: {str(e)}"

    def search_vector_db(self, query: str) -> List[Dict[str, Any]]:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"search_query": query, "top_k": 3}
        try:
            return [
                {
                    "content": "SonarQube 상태 및 예외처리 가이드...", 
                    "metadata": {"filename": "exception_standard.md", "dept": "SQA"}, 
                    "score": 0.88
                }
            ]
        except Exception:
            return []

def classify_intent(state: SQAState):
    return {'intent': 'sonarqube', 'confidence': 0.9, 'step_logs': [{'node': 'classify', 'status': 'success'}]}

def retrieve_and_generate(state: SQAState):
    client = SQAClient()
    docs = client.search_vector_db(state.get('working_query', ''))
    return {'retrieved_docs': docs, 'answer_candidate': '...', 'step_logs': [{'node': 'retrieve_generate', 'status': 'success'}]}

def verify_result(state: SQAState):
    return {'is_verified': True, 'step_logs': [{'node': 'verify', 'status': 'success'}]}

def finalize_or_escalate(state: SQAState):
    for log in state.get("step_logs", []):
        pass

    if state.get("is_verified"):
        return {"messages": [AIMessage(content=state["answer_candidate"])]}
    else:
        msg = "가이드에서 답변을 찾을 수 없어 SQA 담당자에게 문의 부탁드립니다."
        if state.get("suggested_topics"):
            msg += f"\n추천 주제: {', '.join(state['suggested_topics'])}"
        return {"messages": [AIMessage(content=msg)]}
