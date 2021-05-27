# 👩‍💻 관통 프로젝트 👨‍💻

👼 팀장 : 진지연

👶 팀원 : 심해영, 육승준



## 배포 서버 URL

✨ http://18.116.36.57





## 개요

> `01.` 팀 소개
>
> `02.` 목표
>
> `03.` 프로젝트 구조
>
> `04.` 데이터베이스 모델링(ERD)
>
> `05.` 기능 설명
>
> `06.` 추천 알고리즘 상세 설명
>
> `07.` 느낀점





## 01. 팀 소개



#### 🍟 팀 명 : Pickcorn

* 영화를 골라서 추천해준다는 뜻의 `Pick` 과 영화 필수템 `Popcorn` 을 합쳐서 만들었습니다.


![image-20210527181819897](README.assets/image-20210527181819897.png)



#### 🍟 팀원 소개

🍊 진지연 (팀장)

	* 영화 추천 알고리즘 구현
	* movies 앱 > index 구현
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



#### 🍕 구현하지 못했던 서비스

##### 01. 캐러솔

이유 : 다른 기능 구현하느라 시간 부족, 난이도가 어려웠음

##### 02. 좋아요 / 싫어요 기능 ajax

이유 : 다른 함수에 있는 movie_score랑 얽혀있어서 건드리기 난해했음

##### 03. detail 페이지 > 유튜브로 트레일러영상 연결

이유 : 도전해봤으나 어려웠다...!

##### 04. pagination 페이지 넘기는 기능 ajax

이유 : vue가 아닌 django.html이라 접근을 어떻게 해야할 지 몰라 어려웠음



---





## 03. 프로젝트 구조

| pickcorn/                                                    | accounts/                                                    | movies/                                                      |
| ------------------------------------------------------------ | :----------------------------------------------------------- | ------------------------------------------------------------ |
| static/<br />        base.css<br />        pickcorn.jpg<br />        pickcorn2.jpg<br />        pickcorn3.jpg<br />    templates/<br />        base.html<br />    setttings.py<br />    urls.py | migrations/<br />    static/<br />        login.css<br />        profile.css<br />        signup.css<br />        signupload.css<br />    templates/<br />        accounts/<br />            followers.html<br />            followings.html<br />            login.html<br />            profile.html<br />            signup.html<br />            signupload.html<br />    forms.py<br />    models.py<br />    urls.py<br />    views.py | fixtures/<br />    migrations/<br />    static/<br />        article_create.css<br />        article_detail.css<br />        article_update.css<br />        detail.css<br />        index.css<br />        pickcorn3.png<br />    templates/<br />        movies/<br />            article_create.html<br />            article_detail.html<br />            article_update.html<br />            detail.html<br />            homepage.html<br />            index.html<br />            searchpage.html<br />    forms.py<br />    models.py<br />    serializers.py<br />    urls.py<br />    views.py |





---





## 04. 데이터베이스 모델링(ERD)

![image-20210527193816930](README.assets/image-20210527193816930.png)





---





## 05. 기능 설명



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
* 로그인 하기 전엔 영화 추천 서비스를 받을 수 없음





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

   

* 메인 화면에서 follow 한 유저의 영화 목록과 이를 기반으로 한 추천목록이 뜸

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



#### 🎈 2. Accordion 내용

* 클릭 시 유저가 작성한 리뷰 Detail 페이지로 이동

<img src="README.assets/image-20210527175626983.png" alt="image-20210527175626983" style="zoom:80%;" />

* 좋아요 누른 영화 목록

<img src="README.assets/image-20210527184315954.png" alt="image-20210527184315954" style="zoom:80%;" />





---





## 06. 추천 알고리즘 상세 설명
db & recommend.ipynb 참조

![추천알고리즘](README.assets/추천알고리즘.png)


api를  활용하여 tmdb에서 5000개의 데이터를 불러오고, 이 중에 poster_path가 null값이 아닌 데이터를 저장한다. 

#### 🌵 장르를 기준으로 영화 정보를 벡터로 만들기

```
movies_df['genres_literal'] = movies_df['genres'].apply(lambda x : (' ').join(map(str, x)))
count_vect = CountVectorizer(min_df=0, ngram_range=(1,2))
genre_mat = count_vect.fit_transform(movies_df['genres_literal'])
```



#### 🌵 코사인 각도를 기준으로 벡터 간 유사도 구하기

```
genre_sim = cosine_similarity(genre_mat, genre_mat)
genre_sim_sorted_ind = genre_sim.argsort()[:, ::-1]
```

영화 별로 유사도 순으로 6개 영화를 추출하고, 이 중 가중평균이 높은 3개를 추출한다. 가중평균은 평균 평점에 투표수를 가중치로 둔 점수이다.

영화별 추천 영화 테이블을 기존의 영화정보 테이블에 merge한 후, M:N 관계로 DB에 저장한다.




---





## 07. 느낀점

🍊 진지연 (팀장)

머신러닝을 실제 서비스에 연결하기, 구현한 내용 배포하기 같은 궁금했었던 기능을 직접 구현해봐서 좋았다.

또 초반에 기획을 꼼꼼히  한 덕분에 일이 수월하게 진행되었던 것 같다.

아쉬운 점은 Vue를 적극적으로 안 써봤다는 점.. 6월에 별도로 연습을 해봐야겠다.



🍍 심해영

수업 내용도 확실히 잘 이해하지 못한 상태여서 다른 팀원들에게 피해가 갈까봐 걱정이 많았다.

할 수 있는 것들은 최선을 다해서 참여했지만 스스로 부족한 점이 많아서 속상했다.

Vue는 아예 건드리지도 못해서 모르는 부분은 복습이 필요할 것 같다.

걱정이 많았지만 좋은 팀원들을 만나서 좋은 결과를 낼 수 있었던 것 같다.



🥑 육승준

웹 구현과 관련하여 배운 내용들 중에서는 그래도 django 정도만 자신이 있었다.

그래서 처음에 django로 대부분을 구현하고 나중에 필요한 부분을 vue나 javascript로 하려고 했는 데, 생각보다 django로 할 수 있는 것들이 많았다.

수업 시간에 youtube 영상을 가져오는 것을 vue로 배워서 막상 모든 걸 django로 구현해보니 vue를 시작하기가 조금 어려워 포기하였다.

후반부에 배웠던 것들을 시간 있을 때 한번 씩 더 보는 연습을 해야겠다.

