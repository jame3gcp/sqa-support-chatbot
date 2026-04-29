# Software Design Description (SDD) - SQA Support Chatbot

## 1. 개요 (Introduction)
본 문서는 사내 SQA 업무 자동 응대를 위한 챗봇 시스템의 기준 스펙을 정의한다.

## 2. 시스템 아키텍처 (System Architecture)
- **Runtime**: Docker Compose 기반 컨테이너 환경.
- **Orchestration**: LangGraph.
- **State Management**: Postgres DB (Checkpointing).

## 3. 기능적 요구사항 (Functional Requirements)
1. **RAG 기반 응대**: 사내 벡터 DB(MD 파일 기반)를 조회하여 답변 생성.
2. **의도 분류(Intent Classify)**: 지원 범위 외 질문 및 모호한 질문 식별.
3. **담당자 에스컬레이션**: 답변 불가 시 담당자 안내 및 미응대 로그 기록.
4. **검증 루프(Verification)**: 생성된 답변의 근거 일치 여부 자가 검증.

## 4. 데이터 인터페이스 스펙 (Data Interface)
- **Input**: User Query, Session ID.
- **Output**: Answer, Source References, Next Step Suggestion.
- **AI Platform API**: 사내 전용 AI 플랫폼 REST API (Bearer Auth).

## 5. 운영 및 확장성 (Operations & Scalability)
- **Knowledge Update**: 담당자가 답변 불가 질문을 확인 후 MD 파일을 업데이트하여 지식을 확장함.
- **Logging**: 모든 노드 실행 로그를 Postgres에 기록하여 대시보드에서 가시화.
- **Future Ready**: 향후 K8s 배포를 고려한 환경 변수 및 볼륨 바인딩 구조 준수.
