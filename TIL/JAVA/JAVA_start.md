# JAVA 개요
본 문서에는 JAVA 언어의 특징을 기술합니다.
## JAVA의 특징
### 사용되는 분야
- 웹 프로그래밍 : 서버 사이드 (백 엔드) 개발에 강점이 있음. 서블릿, 스프링 프레임워크와 같은 기술을 사용.
- 안드로이드 어플리케이션
- 게임 개발 : LWJGL
- 데이터베이스 처리
- 빅 데이터 및 분산 처리 - Hadoop, Spark 등의 프레임워크 제공
### 할 수 없는 일
- 높은 성능을 요구하는 프로젝트. GC, JIT Compiler와 같은 시스템적 기능으로 인해 속도가 느리다.
- 시스템 프로그래밍 : 운영체제, 드라이브, 커널 등의 Low Level 시스템 개발
- IOS 어플리케이션 개발(제한적)
### JAVA의 특징
- .java -> compiler -> .class -> run
- Simple : C++에 가깝지만 훨씬 가볍다.
- Object-oriented : primitive data type을 제외하면 거의 모두 객체로 구성됨.
- Interpreted : Compile 언어인 동시에 Interpreted (코드 한줄 씩 작성하고 확인 가능)
- Robust : 포인터 연산을 지원하지 않음. 메모리 누수를 개발자가 걱정할 필요가 없다.
- Sequred : 자료형 타입에 민감. 컴파일 성공 후에 오류 발생율이 파이썬에 비해 적다.
- Platform independent : 이진 코드로 컴파일. 시스템 체계에 영항을 받지 않고 JRE만 설치되어 있으면 가능.
- Multithreaded : Thread 단위로 실행 가능.
- Dynamic : Java Interface를 사용하면 다른 모듈까지 모두 갱신할 필요가 없음.
### Main method
- 프로그램 시작과 끝을 관리
