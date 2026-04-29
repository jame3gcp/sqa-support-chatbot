from langgraph.graph import StateGraph, START, END
from core.state import SQAState
from core.nodes import classify_intent, retrieve_and_generate, verify_result, finalize_or_escalate

def build_graph():
    workflow = StateGraph(SQAState)
    workflow.add_node('classify', classify_intent)
    workflow.add_node('retrieve_generate', retrieve_and_generate)
    workflow.add_node('verify', verify_result)
    workflow.add_node('finalize', finalize_or_escalate)
    workflow.add_edge(START, 'classify')

    def route_intent(state: SQAState):
        if state.get('confidence', 0) < 0.6: return 'ask_more'
        if state.get('intent') == 'unknown': return 'escalate'
        return 'retrieve'

    workflow.add_conditional_edges(
        'classify',
        route_intent,
        {
            'retrieve': 'retrieve_generate',
            'ask_more': 'finalize',
            'escalate': 'finalize'
        }
    )
    workflow.add_edge('retrieve_generate', 'verify')

    def route_verification(state: SQAState):
        if state.get("is_verified"):
            return "finish"
        if state.get("retry_count", 0) >= 2:
            return "escalate"
        if state.get("confidence", 0) < 0.4:
            return "ask_more"
        return "retry"

    workflow.add_conditional_edges(
        "verify",
        route_verification,
        {
            "finish": "finalize",
            "retry": "retrieve_generate",
            "ask_more": "finalize",
            "escalate": "finalize"
        }
    )
    workflow.add_edge('finalize', END)
    return workflow.compile()
