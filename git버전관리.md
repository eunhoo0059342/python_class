# Git

: 프로그램 등의 소스 코드 관리를 위한 **분산 버전관리 시스템** 

[Reference](https://git-scm.com/docs)

## 버전관리시스템 (VCS, Version control system)

: 파일 변화를 시간에 따라 기록하여 과거 특정 시점의 버전을 다시 불러올 수 있는 시스템

기존에는 이전 파일내용을 알기 위해서는 ctrl+z 혹은 파일명으로 버전을 나눠서 저장했는데 git을 사용하면 그럴 필요없이 파일 하나로 버전을 관리 할수 있다.

> **이전으로 돌아 갈수 있는 방법**

![](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/54ae3ba8-f2b1-4e1e-9aa2-07ac43cf5e24/_2021-05-20__1.58.48.png)

OR

![](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/318a6158-6b23-474e-9ce2-3290180b4c9b/Screen_Shot_2021-05-31_at_10.10.19_PM.png)

git을 사용하면 언제(When), 누가(Who), 어디서 (Where), 무엇을(What), 어떻게(How), 왜(Why)
 변경한 히스토리를 한번에 기록/관리가 가능하다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a49de1be-f691-4b3b-95aa-afae00a36692/Untitled.png)

Git 을 사용하면 같은 파일명의 내용이 어떤 부분이 다른지를 자동으로 비교하고, 어떤 것을 반영할지 선택이 가능하다. 이렇게 변경 히스토리를 눈에 파악이 가능하기 때문에 프로젝트를 나누어서 작업하고 하나로 합치는 협업에 편하다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/573e3b39-92b7-4c70-a7de-ac0c444c66b5/Untitled.png)

<aside>
💡 Git은 기본적으로 코드(Python, HTML, JavaScript, Java,...), text 파일, markdown파일(text 파일의 일종), CSV 파일에 대해서는 라인단위로 체크가 된다. 이미지 파일, Word 파일, PDF 파일, 엑셀 파일도 별도 설정을 해주면 가능하지만 기본적으로는 파일 크기 정도만 체크가 된다.

</aside>

## Git 저장소

: Git의 기본요소로 이력을 관리할 저장소가 필요

: 저장소는 말 그대로 파일을 저장하는 장소로, 파일 이력에 따라 저장

- 로컬 저장소 : 내 PC에 있는 git 저장소
- 원격 저장소 : 파일을 원격 저장소에 올리고 다른사람과 공유/협업하기 위한 클라우드 저장소
    
                       : 대표적으로 GitHub
    
    ![](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dff2d9f9-c1f3-44d2-89d0-0a925d391076/_2021-05-20__2.13.00.png)
    

![](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6f12b2ee-ffd2-4cc7-9ade-72e0eb468f5c/_2021-05-20__2.13.33.png)

## Git 저장 흐름

![](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9c634e34-b0be-4635-aa50-cd7d58f4ffdd/_2021-05-20__2.20.37.png)

![](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7c32f69c-f938-4bdc-92e2-a241bda6169f/Screen_Shot_2021-05-24_at_12.44.43_AM.png)

---