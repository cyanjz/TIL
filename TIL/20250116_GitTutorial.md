# Python track day 2
## CLI
1. 사용 이유
   1. 효율성 : 메모리 소비량이 매우 낮음.
   2. 정밀한 제어 : cmd 만으로 정밀하게 제어할 수 있는 프로그램이 있음.
   3. 범용성 : cmd 기반이므로 여러 운영 체제에서 사용 가능함.
2. CLI 기초 문법
   1. touch <file name>: Make file in cur dir
   2. mkdir <folder name> : Make new folder in cur dir
   3. cd <directory> : Change dir
   4. start <file name> : Run file
   5. rm [-r] <file name>
   6. clear / ctrl + l : clear cmd history
   7. pwd : print current working directory
   8. ctrl + i : paste

## Tortoise svn - 중앙 버전 관리 시스템템
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
3. 기초 문법
```bash
# Initialize git. WD is tracked by git after initialization.
git init

# Add files to staging area
git add {file_name}
git add *.jpg  #also works with wildcard, *
git add *
git add .  # add all files in cur dir

# Check status
git status  # checkout current status of staging area / W.D.

# Commit logs
git log [--oneline] # checkout commit log of git. With --oneline, returns logs in an oneline.

# Global user info
git config --global -l # print user.name and user.email
git config --global user.email {email_address}
git config --global user.name {user_name}

# Control staged files
git restore --staged {file_name} # Undo modification from staging area
git rm --cached # Remove new files from stating area
```
1. 