// [Read]
$(document).ready(function () {
    show_bucket();
});
function show_bucket() {
    fetch('/bucket').then(res => res.json()).then(data => {
        // json 형식으로 변환, 반환된 데이터가 res 인자로 들어옴
        // res.json()에 의해 Promise 객체로 변환되어 data에 저장
        // data 내용 테스트
        console.log("data===>"+data)

        // data의 내용이 OpenAPI로부터 데이터 받는것과 동일
        // 리스트 형태의 data를 rows 변수에 담고
        let rows = data['result']
        console.log("rows===>"+rows)

        // 반복문 전에 하드코딩 부분 비워주기
        $('#bucket-list').empty();

        // forEach 반복문을 통해
        rows.forEach((a)=>{
            // 리스트에 있는 key의 value들을 각 변수에 담기
            let bucket = a['bucket']
            console.log("bucket===>"+rows)

            // index.html에 위 변수들이 들어가도록 백틱 내 자리표시자${variable} 작성한 내용을 temp_html에 작성
            let temp_html = `<li>
                                <h2>✅ ${bucket}</h2>
                            </li>`
            // 위 temp_html을 index.html의 #cards-box div에 붙여주기.
            $('#bucket-list').append(temp_html)
        })
    })
}

// [Create]
function save_bucket() {
    // index.html로부터 값 가져오기
    let bucket = $('#bucket').val()

    // formData 객체를 생성하고
    let formData = new FormData();
    // append()통해 {key,value}를 객체에 담는다
    formData.append("bucket_give", bucket);

    // POST 요청에 위 formData를 body에 담아 요청한다.
    fetch('/bucket', { method: "POST", body: formData, }).then((response) => response.json()).then((data) => {
        alert(data["msg"]);
        // 브라우저 새로고침 추가
        window.location.reload();
    });
}