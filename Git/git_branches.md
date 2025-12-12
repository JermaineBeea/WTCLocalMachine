# How to Use `git branch` in Practice

## 1. Create a New Branch

**Command:**

```
git checkout -b feature/some-task-name
```

**What this does:**

* Creates a new branch called `feature/some-task-name`
* Switches to that branch immediately

**Recommended naming conventions:**

* `feature/` — for new features
* `bugfix/` — for bug fixes
* `hotfix/` — for urgent patches

---

## 2. Work on Your Task

After making changes, stage and commit them:

```
git add .
git commit -m "Add initial version of feature X"
```

---

## 3. Push Your Branch to GitLab

```
git push -u origin feature/some-task-name
```

**Explanation:**
The `-u` flag sets the upstream branch, allowing future pushes with simply:

```
git push
```

---

## 4. Open a Merge Request (Pull Request on GitHub)

In GitLab:

1. Go to **Merge Requests**
2. Click **New Merge Request**
3. Choose the source branch (e.g., `feature/some-task-name`)
4. Choose the target branch (usually `main`)
5. Add a title and description
6. Assign reviewers if required

---

## 5. After the Merge (Optional Cleanup)

Once your code is merged:

```
git checkout main
git pull origin main
git branch -d feature/some-task-name
git push origin --delete feature/some-task-name
```

This removes the feature branch locally and remotely.

---

## Group Activity Suggestion for Team Kickoff

* Each team member clones the repository
* Creates and pushes their own branch (e.g., `feature/hello-name`)
* Opens a test Merge Request with a small change (e.g., adding themselves to a contributors file)
