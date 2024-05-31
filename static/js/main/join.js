function memberIdChk() {
    const userIdVal = document.getElementById("m_user_id").value;

    if (!userIdVal) {
        alert("아이디를 입력해 주세요.");

        return;
    }
    
    /**
     * ajax 기능을 위해 fetch API 사용(구 브라우저는 지원 안 됨, 예를 들면 IE, 작동안 할 경우 axios.jsm jquery.js 등 다른 라이브러리 사용 필요)
     */
    const request = new Request(
        'member_id_check/',
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector("[name='csrfmiddlewaretoken']").value
            },
            mode: 'same-origin',
            body: JSON.stringify({
                'mbr_id': userIdVal
            })
        }
    );

    fetch(request)
        .then((response) => response.json())
        .then((data) => {
            const dupl_id_flag = data['dupl_id_flag'];

            if (dupl_id_flag) {
                alert("이미 존재하는 아이디로 사용하실 수 없습니다.");
            } else {
                alert("사용가능한 아이디 입니다.");
            }
        });
}