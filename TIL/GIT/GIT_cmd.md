1. 기초 문법
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

2. Remote repository 문법
```bash
# Control remote repos
git remote add {repo_name} {repo_url} # Add new remote repo
git remote remove {repo_name} # Remove remote repo
git remote set-url origin {repo_url} # Set url for remote repo
git remote -v # Checkout remote repo info.
# Pull/push
git pull {repo_name} {branch_name} # Fetch & merge from remote repo. Cannot pull branches with unrelated histories.
git push {repo_name} {branch_name} # Push local repo to remote repo. Cannot merge barnches with unrelated histories. (Cannot merge in github)
# Clone remote repo
git clone {repo_url} # Clone remote repo. Remote url is automatically updated.
```

3. .gitignore
   1. git이 추적하지 않을 파일을 지정.
      1. folder_name/
      2. file_name
   2. 단 한번이라도 commit이 된 파일은 .gitignore로 무시할 수 없음.
   3. repository의 구조/파일을 미리 정하고 개발을 시작.
   4. gitignore 폴더를 만드는 것도 하나의 방법.