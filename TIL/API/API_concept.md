# API
## 개요
Application Programming Interface.</br>
말 그대로 Application 사이의 통신을 위한 메커니즘.</br>
약속된 방식의 인터페이스로 데이터를 Request, Response하는 규칙을 제공.</br>
Social login service가 대표적인 예시.</br>
## API key
Request를 무분별하게 수용하면 보안상/비용상 문제가 발생.</br>
따라서 사용자 별로 API key를 발급하고 올바른 API key인 경우에만 response.</br>
```
Client -> Request(login) -> Server
Server -> Response( + API key) -> Client
Client -> Request( + API key) -> Server
Server -> Response -> Client
```
1. 장점
    1. 보안 강화 : 무단 접근을 막고, 승인된 사용자의 요청에만 응답.
    2. 데이터 관리 : API 호출 횟수, 사용량을 모니터링하여 사용제한 및 과금 정책에 사용.
2. 보안 사항
    1. 노출 금지 및 정기 갱신
    2. 서버-클라이언트 구조에서 키를 안전하게 보관
    