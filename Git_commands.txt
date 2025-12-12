# Git Commands Reference Guide

*A clear and organized guide for rewriting history, editing commits,
changing authors, changing dates, resetting branches, and removing
commits.*

## 🔍 Finding Commits by Author

``` bash
git log --oneline --author="jebeeajhb024@gmail.com"
```

## ✏️ Rewrite Author Information (Full History)

``` bash
git rebase -i --root
git commit --amend --author="Jermaine Beea <jebeeajhb024@student.wethinkcode.co.za>" --no-edit
git rebase --continue
git push --force-with-lease
```

# ✅ Fixing or Editing Commits

## 1. Revert or Undo the Latest Commit

``` bash
git revert HEAD
git reset HEAD~1
```

# 🕒 Changing Commit Dates

## 1. Change the Date of the Most Recent Commit

``` bash
GIT_COMMITTER_DATE="2025-12-07 10:30:00 +0200" \
git commit --date="2025-12-07 10:30:00 +0200" -m "commit message"
git push --force-with-lease
```

## 2. Change the Date of an Older Commit

``` bash
git rebase -i HEAD~5
# change pick to edit
GIT_COMMITTER_DATE="Fri Dec 5 10:30:00 2025" git commit --amend --no-edit --date "Fri Dec 5 10:30:00 2025"
git rebase --continue
git push --force-with-lease
```

## 3. Commit With a Specific Date

``` bash
GIT_COMMITTER_DATE="2025-12-05 10:30:00 +0200" \
git commit --date="2025-12-05 10:30:00 +0200" -m "Your message"
```

# 🔄 Resetting and Cleaning Changes

``` bash
git reset --hard
git reset --hard origin/main
git push --force-with-lease
```

# ❌ Removing Commits

## 1. Remove the Latest Commit

``` bash
git reset --soft HEAD~1
git reset --hard HEAD~1
git push origin main --force
```

## 2. Remove an Older Commit

``` bash
git rebase -i <commit-hash>^
# mark commit as drop
git push origin main --force
```
