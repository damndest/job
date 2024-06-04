function moveAddFood() {
    location.href = "/foods/add/";
}

function delAreaFood() {
    const foodChkList = document.querySelectorAll("input[type='checkbox'][id^='del-food-']");
    let isFlag = false;
    let delArr = [];

    for (const chkFlag of foodChkList) {
        if (chkFlag.checked) {
            isFlag = true;

            delArr.push(chkFlag.value);
        }
    }

    if (!isFlag) {
        alert("삭제할 게시판을 체크해 주세요.");

        return;
    } else {
        if (window.confirm("정말 삭제하시겠습니까?")) {
            const request = new Request(
                'del_chk_list/',
                {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector("[name='csrfmiddlewaretoken']").value
                    },
                    mode: 'same-origin',
                    body: JSON.stringify({
                        'food_list': delArr
                    })
                }
            );
        
            fetch(request)
                .then((response) => response.json())
                .then((data) => {
                    const msg = data['msg'];
        
                    if ((msg != undefined) && (msg.trim() != "")) {
                        alert("체크한 게시판을 삭제 " + msg + "하였습니다.");

                        location.href = '/foods/area/';
                    }
                });
        }
    }
}

function toggleAllCheck(me) {
    const foodChkList = document.querySelectorAll("#food-area-tbd input[type='checkbox'][id^='del-food-']");

    if (me.checked) {
        for (const food of foodChkList) {
            food.checked = true;
        }
    } else {
        for (const food of foodChkList) {
            food.checked = false;
        }
    }
}