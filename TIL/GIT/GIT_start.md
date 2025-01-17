## Tortoise svn - 중앙 버전 관리 시스템
- 서버 다운이나 여러 문제에 대응하기 어려움.

## GIT - 분산 버전 관리 시스템
1. 강점
   1. 백업이 용이
   2. 개발 과정을 파악, 이전 버전과의 비교가 용이.
2. 구성
   1. Working directory
      1. 실제 작업이 이뤄지는 곳.
   2. Staging are
      1. Commit 전 변경사항을 확인하고 선별할 수 있음.
      2. Commit을 목적에 따라서 나눠서 할 수 있게 해줌. (bug fix와 new file을 나눠서 commit할 수 있다.)
   3. Repository
      1. 버전(Version, snapshot) 이력과 파일이 영구적으로 저장되는 영역.
   4. Work flow를 특정 File에서 보면 : Untracked files (W.D) -> New files (Staging are) -> Tracked files (Repository)