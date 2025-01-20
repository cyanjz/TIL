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
# Fetch remote repo and reset with hard option -> ignore conflicts
git fetch origin
git reset --hard origin/master
```

3. Revert / Reset 문법
- 공통 사항 : branch가 하나일 경우에는 문제가 없지만, branch가 많아지면 문제 발생.
    1. git revert는 해당 버전으로 돌아가도록 새로운 commit을 수행.
        - 버전을 되돌리면서 무결성/협업 신뢰도를 유지하는 방법.
    2. git reset은 해당 버전 이후의 기록을 삭제하고 해당 버전으로 돌아감.
        1. --soft : WD, Staging Area는 그대로.
        2. --mixed(default) : WD는 그대로.
        3. --hard : 남기는 기록 없이.

```bash
# git revert
git revert {commit_id1} {commit_id2} ... # multiple commits
git revert --no-edit {commit_id} # commit message is 'Revert {commit_message}'
git revert --no-commit {commit_id} # commit 없이 staging area에만.
# git reset, --hard, --soft, --mixed
git reset [option] {commit_id}
```

4. git reflog를 활용한 복구.
```bash
# reflog
git reflog # reset으로 인해 git log에서 확인 불가능한 id 확인 가능
git reset --hard {reflog_commit_id} # 해당하는 id로 하드 리셋.
```