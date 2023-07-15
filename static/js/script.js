// [Read]
$(document).ready(function () {
    show_bucket();
});
function show_bucket() {
    fetch('/bucket').then(res => res.json()).then(data => {
        console.log(data)
        alert(data["msg"]);
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