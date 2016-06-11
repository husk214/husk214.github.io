# git

### github pull request プルリクエスト

#### send pull request

1. github で fork する
2. git clone `git clone https://github.com/[my_user_name]/[repository_name]`
3. 開発用ブランチを切る `git checkout -b [branch_name]`
4. そのブランチで作業
5. add
6. commit
7. push `git push -u origin [branch_name]`
8. 自分のgithubのページでプルリクエストを送る

#### receive pull request

1. テスト用ブランチを作成 `git checkout -b [test_branch_name]  master`
2. プルリクエストをpull  `git pull [URL] [repository_name]`
3. プルリクエストをテスト
4. 問題なさそうなら `git checkout master`
5. マージして `git merge [test_branch_name]`
6. push `git push origin master`
7. テスト用ブランチを削除 `git branch -d [test_branch_name]`

### stash 一時退避
- 一時退避 : `git stash save 'message'`
    (stash以降は省略可能)

- 一覧 : `git stash list`

- 差を表示 : `git stash list -p`

- 戻す(@{番号}) : `git stash apply stash@{0}`

- 戻して一覧から消す : ` git stash pop@{0}`

- 削除 : `git stash drop [stash_name]`

- すべて削除 : `git stash clear`

### submodule サブモジュール

https://git-scm.com/book/ja/v1/Git-%E3%81%AE%E3%81%95%E3%81%BE%E3%81%96%E3%81%BE%E3%81%AA%E3%83%84%E3%83%BC%E3%83%AB-%E3%82%B5%E3%83%96%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB
####

```
git submodule {add}
```

#### サブモジュールを含むプロジェクトのクローン

```
git clone {url}
git submodule init
git submodule update
```

### branch ブランチ

- 削除 : `git branch -d [branch_name]`

- ブランチを切って移動 : `git checkout -b [branch_name]`

### commit コミット

- 取り消し コミットだけを取り消す: `git reset --soft HEAD~`
- 取り消し 内容も取り消す: `git reset --head HEAD~`

### add ssh key at github (github にssh で接続)

  1. make rsa key

    ```
    $ cd ~/.ssh
    $ ssh-keygen -t rsa -C test@example.com
    $ chmod 600 id_rsa
    $ emacs ~/.ssh/config
    ```

    ```
    Host github
      HostName github.com
      IdentityFile ~/.ssh/id_rsa
      User git
    ```

  2. add SSH Key at github
    ```
    $ pbcopy < ~/.ssh/id_rsa.pub
    ```

  3. check
    ```
    $ ssh -T git@github.com
    ```

  4. change a local repository setting
    ```
    (NG) url = https://github.com/{account_name}/{repository_name}.git
    (OK) url = git@github.com:{account_name}/{repository_name}.git
    ```
