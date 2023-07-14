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
    let formData = new FormData();
    formData.append("sample_give", "샘플데이터");

    fetch('/bucket', { method: "POST", body: formData, }).then((response) => response.json()).then((data) => {
        alert(data["msg"]);
        window.location.reload();
    });
}