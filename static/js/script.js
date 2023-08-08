// [Read]
$(document).ready(function () {
    show_bucket();
    $('.status-container').mouseover( function() {
        $(this).find('.origin-status').fadeOut();
        $(this).find('.fix-status').fadeIn();
    });
    $('.status-container').mouseout( function() {
        $(this).find('.origin-status').fadeIn();
        $(this).find('.fix-status').fadeOut();
    });
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
            let num = a['num']
            let done = a['done']
            console.log("bucket===>"+bucket)
            let contents = ``;
            if(done == 0){
                contents =   `<li>
                                    <h2>👍 ${bucket}</h2>
                                    <button onclick="update_bucket(${num})" type="button" class="btn btn-outline-primary">완료하기?</button>
                                    <input id="content_num" type="hidden" placeholder="완료용 게시글의 번호" value="${num}"/>
                                </li>`
            }else if(done == 1){
                contents =   `
                                <li>
                                    <h2>✅ <span><del>${bucket}</del></span><div style="float:right">(완료!!)</div></h2>
                                    <div class="status-container">
                                        <button id="restore_status" onclick="restore_bucket(${num})" type="button" class="btn btn-outline-success">
                                            <span id="origin_status">축하해요!</span>
                                            <span id="fix_status">혹시 잘못 누르셨나요?!</span>
                                        </button>
                                    </div>
                                    <input id="content_num" type="hidden" placeholder="완료용 게시글의 번호" value="${num}"/>
                                </li>`
            }
            // index.html에 위 변수들이 들어가도록 백틱 내 자리표시자${variable} 작성한 내용을 temp_html에 작성
            let temp_html = contents
                                
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

// [Update]
function update_bucket(num){
    if (!confirm("정말 버킷리스트를 이루셨나요?/t 확인[예] / 취소[아니오]")) {
        alert("취소[아니오]를 누르셨습니다.");
        window.location.reload();
    } else {
        alert("확인[예]을 누르셨습니다.");
    
        // alert(num);
        // console.log(num);
        let update_num = num;
        let formData = new FormData();
        formData.append("num_give", num);

        fetch('/update', { method: "POST", body: formData, }).then((response) => response.json()).then((data) => {
            alert(data["msg"]);
            // 브라우저 새로고침 추가
            window.location.reload();
        });
            // // formData 객체를 생성하고
            // let formData = new FormData();
            // // append()통해 {key,value}를 객체에 담는다
            // formData.append("num_give", num);
    }
}

function restore_bucket(num) {
    if (!confirm("버킷리스트를 다시 복구할까요?? 확인[예] / 취소[아니오]")) {
        alert("취소[아니오]를 누르셨습니다.");
        window.location.reload();
    } else {
        alert("확인[예]을 누르셨습니다.");
        
    let formData = new FormData();
    formData.append("num_give", num);

    fetch('/restore', { method: "POST", body: formData }).then((response) => response.json()).then((data) => {
            alert(data["msg"]);
            // 브라우저 새로고침 추가
            window.location.reload();
        });
    }
}