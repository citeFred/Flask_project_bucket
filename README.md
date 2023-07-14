# Flask_project_bucket
[Flask] Flask framework 미니프로젝트(project bucket) 

## 🖥️ 프로젝트 소개 
버킷리스트를 기록하는 컨셉의 간단한 메모 게시판 형태의 게시글을 등록하는 웹 페이지 서비스

## 🕰️ 개발 기간
* 23.07.14일 - 23.07.16일

### 🧑‍🤝‍🧑 맴버구성 
 - 김인용 - 싱글 프로젝트

### ⚙️ 개발 환경 
- **MainLanguage** : `PYTHON`
- **IDE** : VisualStudio Code 1.79.2 (Universal)
- **Framework** : Flask Framework
- **Database** : MongoDB(5.0.11)
- **SERVER** : Flask

## 📌 주요 기능
#### View 구성
- top부분에 웹 페이지 정보 : 타이틀(title)

#### 버킷리스트 기록 진행
- input박스에 텍스트 입력
- '기록하기' 버튼으로 입력값 DB로 전송 및 저장 (insert)

#### 버킷리스트 목록 확인
- DB에 저장된 기록된 버킷리스트 데이터 받기(find(==read))
- 받은 데이터를 footer 부분에 한줄씩 출력