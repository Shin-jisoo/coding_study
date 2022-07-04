## 사전 안내 사항

PR을 보내려면 git을 사용할 수 있어야 합니다.
**Git 이나 깃헙(GitHub)을 한 번도 사용해 본 적이 없다면, 다음 사이트를 참고해 git을 익혀주세요.**

* [초심자를 위한 Github 협업 튜토리얼 (with 토끼와 거북이) by 진유림님](https://milooy.wordpress.com/2017/06/21/working-together-with-github-tutorial/) 완전 소프트하게 이해하고 싶을 때 추천
* [누구나 쉽게 이해할 수 있는 Git 입문 중 '원격 저장소' 파트 by backlog](https://backlog.com/git-tutorial/kr/stepup/stepup3_3.html)
* [Basic Git commands by Atlassian](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html) 기본 명령어들이 헷갈릴 때 참고하기
* [Git Tutorial by Atlassian](https://www.atlassian.com/git/tutorials) 영문이지만 정말 잘 정리되어 있음

Git 사용과 관련한 튜토리얼이나 참고자료는 워낙 많기 때문에, 사실 다른 자료를 참고해도 크게 문제는 없습니다.
본인이 읽기 좋고 따라 하기 좋은 문맥을 가진 자료를 선택하시길 바랍니다.

---

## PR 보내는 방법 - 새로운 PR을 보내는 경우

본 설명은 **새로운 PR을 보낼 때** 참고하세요.
다른 사람이 만든 PR에 있는 코드를 수정하고 다면 하단의 **PR 수정하는 방법**을 참고해주세요.

#### STEP 0. 레포 clone 하기(한 번만 진행)

우선 우리가 공유하는 프라이빗 레포를 clone 합니다. clone 할 위치는 내가 원하는 곳으로 자유롭게 지정하시면 됩니다.

`git clone <레포 주소>`

`<레포 주소>`는 본 페이지 상단의 초록색 [⬇️Code] 버튼을 누르면 나오며, 보통 `https://github.com/learn-programmers/어쩌고` 형식입니다.

#### STEP 1. 최신 버전의 main 브랜치 당겨 받기(repeat)

새 PR용 브랜치는 항상 최신 버전의 main 브랜치에서 따야 합니다.
따라서 먼저 main 브랜치를 최신으로 업데이트합시다.

1. 자신의 로컬 main 브랜치로 switch 하기
   * `git switch main`
2. 원격의 main 브랜치 당겨오기
   * `git pull`

#### STEP 2. 내 코드를 올릴 브랜치 만들기(repeat)

`git switch -c <브랜치 이름>`

브랜치 이름은 emily_week1과 같이, 슬랙/github에서 쓰는 닉네임의 영어 버전과 주차를 명시합니다.
예를 들어 슬랙 닉네임이 monmon이라면 monmon_week1와 같은 이름을 지어주세요.
(이 브랜치의 주인이 누구인지 식별할 수 있게 지으면 됩니다)

#### STEP 3. 문제를 풀고, 레포 디렉토리에 파일 만들기(repeat)

본인만의 디렉토리를 만들고 해당 디렉토리에 코드를 넣어주세요.
전체적인 디렉토리 구조는 다음과 같아야 합니다.

```
ㄴ user1(본인 이름)
    ㄴ week1
        ㄴ 최대 용량이 정해진 FIFO 큐 클래스.py
        ㄴ 기능개발.py
        ㄴ ...
    ㄴ week2
        ㄴ 운송 트럭.py
        ㄴ ...
ㄴ user2
    ㄴ week1
        ㄴ ...
```

#### STEP 4. 파일 commit & push 하기(repeat)

내 파일을 stage 하고, commit 합시다.

1. stage 하기
   * `git add <파일 경로>`
   * ex) week1 디렉토리의 기능개발.py 파일을 stage 하고 싶다면 다음 명령어를 입력합니다: `git add week1/기능개발.py`
2. commit 하기
   * `git commit -m "여기에 커밋 메시지를 입력하세요"`
   * ex) `git commit -m "1주차 문제 커밋: 기능 개발, 최대 용량이 정해진 FIFO 큐 클래스, ..."`
3. 원격 저장소에 push 하기
   * git push origin `<브랜치 이름>`


#### STEP 5. PR 보내기(repeat)

STEP 4까지 완료했다면, 본 페이지를 새로고침 했을 때 맨 위에 PR을 만드는 버튼이 생길 겁니다.
해당 버튼을 눌러 PR을 만들어주세요.

PR을 보낼 때에는 다음 양식에 맞추어 코드 설명을 적어주세요.

```
제목: [<n>기 <본인 이름>] 문제 1 이름, 문제 2 이름, ...

# {{문제 1 이름}}

* 내가 문제를 푼 방식 설명하기(문제를 못 풀었다면, 무슨 방법을 시도했고 어디서 막혔는지 설명하기)
* 시간 복잡도 분석

# {{문제 2 이름}}

... 어쩌고 저쩌고

```

예시:

```
#### 카펫

전체 격자 수(total)가 주어졌을 때 가능한 정수 가로(width), 세로(height)를 구하고, 가로와 세로에 따른 빨간 격자 수가 주어진 값과 일치하는 지를 알아보았습니다.

시간 복잡도: O(N^3)

```

## 기타 주의 사항

#### 주의 사항 1

git을 사용하다 보면 마음대로 되지 않을 때가 많습니다.
문제를 해결하기 위해 검색을 하면서 여러 시도를 하게 될 건데, 이때 **절대** force push(`git push --force`)는 하지 말아 주세요.
다른 사람의 코드가 날아갈 수 있습니다.

