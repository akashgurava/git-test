# Changelog

## 2021-04-29 23:27 - master

- COMMIT: First commit

## 2021-04-29 23:41 - feature/folder

- COMMIT: Add function get_foldername in osops file

## 2021-04-29 23:43 - master

- PR: Merge feature/folder with get_foldername to master
- LEARN: Since its just a addition, merged automatically

## 2021-04-30 00:04 - feature/change-to-pathlib

- COMMIT: Change osops to use pathlib instead of os.path

## 2021-04-30 00:08 - feature/change-to-pathlib

- COMMIT: Add pathlib to .vscode/settings.json.cSpell

## 2021-04-30 00:08 - master

- PR: Merge feature/change-to-pathlib with pathlib changes to master
- LEARN: Looks like even with modifications(not just additions) we wont get merge conflicts

## 2021-04-30 00:20 - feature/join

- COMMIT: Add function join to join a path to a folder path

## 2021-04-30 00:25 - master

- COMMIT: Add __version__ to __init__.py

## 2021-04-30 00:29 - feature/join

- PR: Merge master with added versioning to feature/join with join function
- LEARN: This time we got Merge conflicts for 2 files(init and changelog) as both were modified in different branches
- LEARN: No merge conflicts for osops though which added join function from feature branch\
- LEARN: During merge bumped version for "0.2.0" and added changelog
- LEARN: First merge master to feature branch

```sh
git fetch origin
git checkout -b feature/join origin/feature/join
git merge master
```
