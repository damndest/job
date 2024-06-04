function moveModFood(foodNo) {
    location.href = "/foods/area/" + foodNo + "/mod/";
}

function moveDelAreaFood(foodNo) {
    location.href = "/foods/area/" + foodNo + "/del/";
}

function addAreaReply(foodNo) {
    const nicknameVal = document.querySelector("input[name='nickname']").value;
    const contentVal = document.querySelector("input[name='content']").value;

    if ((nicknameVal === undefined) || (nicknameVal === null) || (nicknameVal.trim() === "")) {
        alert("댓글의 닉네임을 입력해 주세요.");

        return;
    }

    if ((contentVal === undefined) || (contentVal === null) || (contentVal.trim() === "")) {
        alert("댓글 내용을 입력해 주세요.");

        return;
    }

    const request = new Request(
        '/foods/area/reply/add/',
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector("[name='csrfmiddlewaretoken']").value
            },
            mode: 'same-origin',
            body: JSON.stringify({
                'nickname': nicknameVal,
                'content': contentVal,
                'food_no': foodNo
            })
        }
    );

    fetch(request)
        .then((response) => response.json())
        .then((data) => {
            const foodNo = data['food_no'];

            if (foodNo) {
                alert("댓글을 추가하였습니다.");

                location.href = '/foods/area/' + foodNo + '/';
            }
        });
}

function delAreaReply(foodRplNo, foodNo) {
    const request = new Request(
        '/foods/area/reply/del/',
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector("[name='csrfmiddlewaretoken']").value
            },
            mode: 'same-origin',
            body: JSON.stringify({
                'food_rpl_no': foodRplNo,
                'food_no': foodNo
            })
        }
    );

    fetch(request)
        .then((response) => response.json())
        .then((data) => {
            const foodNo = data['food_no'];

            if (foodNo) {
                alert("댓글을 삭제하였습니다.");

                location.href = '/foods/area/' + foodNo + '/';
            }
        });
}