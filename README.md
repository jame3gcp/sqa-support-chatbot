# SQA Support Chatbot

사내 업무 응대(코드 품질 정책, SonarQube 사용법, 예외 처리 표준 등)를 자동화하기 위한 LangGraph 기반 챗봇 프로젝트입니다.

## 🚀 개요
이 프로젝트는 사내 AI 플랫폼과 MD 기반 벡터 DB를 연동하여 가동됩니다. 사용자의 질문이 모호하거나 가이드에 없는 경우 담당자에게 연결하는 지능형 워크플로우를 갖추고 있습니다.

## 🛠 기술 스택
- **Framework**: LangGraph
- **Language**: Python 3.11+
- **Infrastructure**: Docker Compose, Postgres (State DB)
- **Knowledge Base**: Markdown Files (via Vector DB)

## 🏗 프로젝트 구조
- `config/`: 시스템 설정 및 프롬프트 관리
- `core/`: LangGraph 오케스트레이션 로직
- `infrastructure/`: Docker 및 인프라 설정
- `data/`: RAG를 위한 원천 MD 가이드 문서

## 📝 설계 문서
상세한 설계 사양은 [SDD.md](./SDD.md) 파일을 참조하세요.
