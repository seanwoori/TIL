# Git advanced

## Git undoing
### 개요
- Git 작업 되돌리기(Undoing)
- Git에서 되돌리기는 작업 상태에 따라 크게 세 가지로 분류
  - Working directory 작업단계
  - Staging area 작업단계
  - Repository 작업단계

## Git branch
### 개요
- 브랜치는 나뭇가지라는 뜻으로, 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 기구

### 장점
1. 브랜치는 독립 공간을 형성하기 때문에 원본(master)에 대해 안전함
2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능함
3. Git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함

### git branch
- 브랜치의 조회, 생성, 삭제와 관련한 Git 명령어
- 조회
  - git branch
  - git branch -r
- 생성
  - git branch {브랜치 이름}
  - git branch {브랜치 이름} {커밋 ID}
- 삭제
  - git branch -d {브랜치 이름}
  - git branch -D {브랜치 이름}

### git switch
- 현재 브랜치에서 다른 브랜치로 이동하는 명령어
- git switch {브랜치 이름}
- git switch -c {브랜치 이름}
- git switch -c {브랜치 이름} {커밋 ID}
- **switch 하기 전에, 해당 브랜치의 변경 사항을 반드시 커밋해야함을 주의**
  - 다른 브랜치에서 파일을 만들고 커밋하지 않은 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아있게 됨

### HEAD
- "This is a pointer to the local branch you're currently on"
- HEAD는 현재 브랜치를 가리키고, 각 브랜치는 자신의 최신 커밋을 가리키므로 결국 HEAD가 현재 브랜치의 최신 커밋을 가리킨다고 할 수 있음
- git log 혹은 cat.git/HEAD를 통해서 현재 HEAD가 어떤 브랜치를 가리키는지 알 수 있음
- **결과적으로 git switch는 현재 브랜치에서 다른 브랜치로 HEAD를 이동시키는 명령어**

## Git merge
### git merge
- 분기된 브랜치(Branch)들을 하나로 합치는 명령어
- master 브랜치가 상용이므로, 주로 master 브랜치에 병합
- git merge {합칠 브랜치 이름}
  - 병합하기 전에 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야함
  - 병합에는 세 종류가 존재
    1. Fast-Forward
    2. 3-way Merge
    3. Merge Conflict

### 1. Fast forward
- 마치 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법

### 2. 3-way merge
- 각 브랜치의 커밋 두 개와 공통 조상 하나를 사용하여 병합하는 방법

### 3. Merge conflict
- 두 브랜치에서 같은 부분을 수정한 경우, Git이 어느 브랜치의 내용으로 작성해야 하는지 판단하지 못하여 충돌(Conflict)이 발생했을 때 이를 해결하며 병합하는 방법
- 보통 같은 파일의 같은 부분을 수정했을 때 자주 발생함.
- 충졸이 발생한 부분은 작성자가 직접 해결해야함
- 충돌 해결 후, 병합된 내용을 기록한 Merge commit 생성
- 즉, 두 브랜치에서 **같은 파일의 같은 부분**을 수정 후 병합하는 경우 => 충돌(Conflict)

## Git workflow
### 개요
- Branch와 원격 저장소를 이용해 협업을 하는 두 가지 방법
  1. 원격 저장소 소유권이 있는 경우 => Shared repository model
  2. 원격 저장소 소유권이 없는 경우 => Fork & Pull model 

## Shared repository model
## 개요
- 원격 저장소가 자신의 소유이거나 Collaborator로 등록되어 있는 경우
- mater 브랜치에 직접 개발하는 것이 아니라, 기능별로 브랜치를 따로 만들어 개발
- Pull Requset를 사용하여 팀원 간 변경 내용에 대한 소통 진행

### 따라하기
1. 소유권이 있는 원격 저장소를 로컬 저장소로 clone 받기
2. 사용자는 자신이 작업할 기능에 대한 브랜치를 생성하고, 그 안에서 기능을 구현
3. 기능 구현이 완료되면, 원격 저장소에 해당 브랜치를 Push
4. 원격 저장소에 각 기능의 브랜치가 반영됨
5. Pull request를 통해 브랜치를 master에 반영해달라는 요청을 보냄
6. 병합이 완료된 브랜치는 불필요하므로 원격 저장소에서 삭제
7. 원격 저장소에서 병합이 완료되면, 사용자는 로컬에서 master 브랜치로 switch
8. 병합으로 인해 변경된 원격 저장소의 master내용을 로컬에 Pull
9. 원격 저장소 master의 내용을 받았으므로, 기존 로컬 브랜치 삭제 (한 사이클 종료)

## Fork & Pull model
### 개요
- 오픈소스 프로젝트와 같이, 자신의 소유가 아닌 원격 저장소인 경우
- 원본 원격 저장소를 그대로 내 원격 저장소에 복제 (이러한 행위를 Fork라고 함)
- 기능 완성 후 복제한 내 원격 저장소에 Push
- 이후 Pull request를 통해 원본 원격 저장소에 반영될 수 있도록 요청함

### 따라하기
1. 소유권이 없는 원격 저장소를 fork를 통해 내 원격 저장소로 복제
2. fork이후, 복제된 내 원격 저장소를 로컬 저장소에 clone
3. 이후에 로컬 저장소와 원본 원격 저장소를 동기화 하기위해 연결
4. 사용자는 자신이 작업할 기능에 대한 브랜치를 생성하고, 그 안에서 기능을 구현
5. 기능 구현이 완료되면, 복제 원격 저장소(origin)에 해당 브랜치를 Push
6. 복제 원격 저장소(origin)에 브랜치가 반영됨
7. Pull request를 통해 origin의 브랜치를 upstream에 반영해달라는 요청을 보냄
8. upstream에 브랜치가 병합되면 origin의 브랜치는 삭제
9. 이후 사용자는 로컬에서 master 브랜치로 switch
10. 병합으로 인해 변경된 upstream의 master 내용을 로컬에 Pull
11. upstream의 master 내용을 받았으므로, 기존 로컬 브랜치 삭