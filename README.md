# 👩‍💻 관통 프로젝트 👨‍💻

👼 팀장 : 진지연

👶 팀원 : 심해영, 육승준



## 개요

> `01.` 팀 소개
>
> `02.` 목표
>
> `03.` 프로젝트 구조
>
> `04.` 기능 설명
>
> `05.` 추천 알고리즘 상세 설명
>
> `06.` 



## 01. 팀 소개



#### 🍟 팀 명 : Pickcorn

* 영화를 골라서 추천해준다는 뜻의 `Pick` 과 영화 필수템 `Popcorn` 을 합쳐서 만들었습니다.


<img src="README.assets/캡처.PNG" alt="1" style="zoom:80%;" />



#### 🍟 팀원 소개

🍊 진지연 (팀장)

	* 영화 추천 알고리즘 구현
	* movies 앱 > index 구현
	* 관리자뷰 생성
	* ajax / 배포



🍍 심해영

* accounts 앱 > 회원가입 / 로그인 / 로그아웃 구현
* navbar / font / css / 기타 레이아웃 구현
* review 생성, 수정, 디테일,  mypage 레이아웃 구현



🥑 육승준

* movies 앱 > detail / community 구현
* user profile / followers / followings 구현
* 영화 제목 & user id 검색 기능 구현
* 사용자 평점 시스템



![image-20210527181356220](README.assets/image-20210527181356220.png)





---





## 02. 목표

![image-20210527181425105](README.assets/image-20210527181425105.png)

![image-20210527181540540](README.assets/image-20210527181540540.png)





---





## 03. 프로젝트 구조

| pickcorn/                                                    | accounts/                                                    | movies/                                                      |
| ------------------------------------------------------------ | :----------------------------------------------------------- | ------------------------------------------------------------ |
| static/<br />        base.css<br />        pickcorn.jpg<br />        pickcorn2.jpg<br />        pickcorn3.jpg<br />    templates/<br />        base.html<br />    setttings.py<br />    urls.py | migrations/<br />    static/<br />        login.css<br />        profile.css<br />        signup.css<br />        signupload.css<br />    templates/<br />        accounts/<br />            followers.html<br />            followings.html<br />            login.html<br />            profile.html<br />            signup.html<br />            signupload.html<br />    forms.py<br />    models.py<br />    urls.py<br />    views.py | fixtures/<br />    migrations/<br />    static/<br />        article_create.css<br />        article_detail.css<br />        article_update.css<br />        detail.css<br />        index.css<br />        pickcorn3.png<br />    templates/<br />        movies/<br />            article_create.html<br />            article_detail.html<br />            article_update.html<br />            detail.html<br />            homepage.html<br />            index.html<br />            searchpage.html<br />    forms.py<br />    models.py<br />    serializers.py<br />    urls.py<br />    views.py |





---





## 04. 기능 설명



### 1. 회원가입

#### 🎈 1. 회원가입 하기

   <img src="README.assets/image-20210527165419359.png" alt="image-20210527165419359" style="zoom: 67%;" />



#### 🎈 2. 회원가입 중 오류가 발생하면 해당 오류 원인을 알려줍니다.

   <img src="README.assets/image-20210527165531665.png" alt="image-20210527165531665" style="zoom:67%;" />



#### 🎈 3. 회원가입 완료 후 안내 페이지

<img src="README.assets/image-20210527172502789.png" alt="image-20210527172502789" style="zoom:67%;" /> 



---



### 02. 로그인

#### 🎈 1. 로그인 하기

   <img src="README.assets/image-20210527165844667.png" alt="image-20210527165844667" style="zoom:67%;" />



#### 🎈 2. 로그인 중 오류가 발생하면 해당 오류 원인을 알려줍니다.

   <img src="README.assets/image-20210527165932712.png" alt="image-20210527165932712" style="zoom:67%;" />



---



### 03. 메인 화면

#### 🎈 1. 회원가입 / 로그인 하기 전

![image-20210527170052509](README.assets/image-20210527170052509.png)

* navbar : pickcorn 로고, sign in, login
* 상단에 회원가입을 유도하는 메세지
* 영화 추천 서비스를 받을 수 없음





#### 🎈 2. 회원가입 / 로그인 후

![image-20210527170255779](README.assets/image-20210527170255779.png)

* navbar : pickcorn 로고
  * Home : 메인 화면
  * Search : 검색 기능
  * Mypage





#### 🎈 3. 플레이 리스트에 추가한 영화와 비슷한 영화를 추천받을 수 있음

* 예를들어 디즈니의 `주토피아` 라는 영화를 좋아요 누른다면

  ![image-20210527170735625](README.assets/image-20210527170735625.png)

  

* 메인 화면에서 비슷한 영화가 추천 목록에 뜨게 됨

  <img src="README.assets/image-20210527170945789.png" alt="image-20210527170945789" style="zoom: 67%;" />  👉 <img src="README.assets/image-20210527171012133.png" alt="image-20210527171012133" style="zoom:67%;" />





#### 🎈 4. 팔로우 한 유저의 영화 목록을 추천받을 수 있음

* `search` 를 통해 유저 검색 후 `follow` 클릭

    <img src="README.assets/image-20210527171543823.png" alt="image-20210527171543823" style="zoom:67%;" /> 👉 <img src="README.assets/image-20210527171759574.png" alt="image-20210527171759574" style="zoom:80%;" /> 👉 <img src="README.assets/image-20210527171841956.png" alt="image-20210527171841956" style="zoom: 80%;" />

   

* 메인 화면에서 follow 한 유저의 영화 목록이 뜸

  <img src="README.assets/image-20210527172005438.png" alt="image-20210527172005438" style="zoom:67%;" />





#### 🎈 5. 메인 화면 기타 컨텐츠

* 순위 TOP 20 영화

  <img src="README.assets/image-20210527172128770.png" alt="image-20210527172128770" style="zoom:67%;" />



* 조회수가 높은 영화

  <img src="README.assets/image-20210527172154704.png" alt="image-20210527172154704" style="zoom:67%;" />



* Try New 랜덤 영화 추천

  <img src="README.assets/image-20210527172222430.png" alt="image-20210527172222430" style="zoom:67%;" />





---





### 04. 영화 Detail 화면

#### 🎈 1. Detail 페이지

<img src="README.assets/image-20210527172936410.png" alt="image-20210527172936410" style="zoom:67%;" />

* add to my list : 내가 찜한 콘텐츠에 추가





#### 🎈 2. 좋아요 기능

<img src="README.assets/image-20210527173027421.png" alt="image-20210527173027421"  />

* 유저들의 좋아요 퍼센트가 반영됨





#### 🎈 3. 싫어요 기능

![image-20210527173117615](README.assets/image-20210527173117615.png)

* 유저들의 싫어요 퍼센트가 반영됨



* 여러 유저들이 좋아요 / 싫어요 투표를 했을 경우

![image-20210527173353885](README.assets/image-20210527173353885.png)

![image-20210527173246939](README.assets/image-20210527173246939.png)

![image-20210527173331763](README.assets/image-20210527173331763.png)





#### 🎈 4. 리뷰 생성 & 수정

<img src="README.assets/image-20210527174403808.png" alt="image-20210527174403808" style="zoom: 67%;" /> 👉 <img src="README.assets/image-20210527174622590.png" alt="image-20210527174622590" style="zoom:67%;" />



* 리뷰가 늘어나면 pagenation 기능으로 다음 페이지를 볼 수 있음

<img src="README.assets/image-20210527174218272.png" alt="image-20210527174218272" style="zoom:67%;" />  👉  <img src="README.assets/image-20210527174809255.png" alt="image-20210527174809255" style="zoom:67%;" />





#### 🎈 5. 리뷰 Detail 페이지

<img src="README.assets/image-20210527174911159.png" alt="image-20210527174911159" style="zoom:80%;" />





#### 🎈 6. 리뷰 Detail 페이지 댓글 생성

<img src="README.assets/image-20210527175120102.png" alt="image-20210527175120102" style="zoom: 80%;" />





---





### 05. MyPage

#### 🎈 1. MyPage 메인

<img src="README.assets/image-20210527175501020.png" alt="image-20210527175501020" style="zoom:80%;" />

* Bootstrap5 > Accordion 기능으로 구현 



#### 🎈 2. 작성한 리뷰

<img src="README.assets/image-20210527175626983.png" alt="image-20210527175626983" style="zoom:80%;" />

* 클릭 시 유저가 작성한 리뷰 Detail 페이지로 이동



#### 🎈 



#### 🎈 



#### 🎈 

