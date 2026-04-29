import unittest
from core.state import SQAState
from core.nodes import classify_intent, verify_result

class TestSQAFlow(unittest.TestCase):
    def test_classify_intent_success(self):
        state = {'messages': [('user', 'SonarQube 사용법 알려줘')]}
        result = classify_intent(state)
        self.assertEqual(result['intent'], 'sonarqube')

    def test_verify_result_pass(self):
        state = {'is_verified': False}
        result = verify_result(state)
        self.assertTrue(result['is_verified'])

if __name__ == '__main__':
    unittest.main()
