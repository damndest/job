function memberJoin() {
    location.href = "/main/join/";
}

function loginView() {
    location.href = "/main/login/";
}

function doLogout() {
    const logoutForm = document.forms['logoutForm'];

    logoutForm.action = '/main/logout/';
    logoutForm.submit();
}