function focusTitleInput() {
    document.getElementById("id_title").focus();
}

function toggleArticleForm() {
    formBox = document.getElementById("article-form-box");
    articleForm = document.getElementById("article-form");
    toggleButton = document.getElementById("write-article-button");
    formBox.style.transition = "padding 0.5s, height 1.5s";
    articleForm.addEventListener("transitionend", focusTitleInput);

    if (formBox.style.height == "580px") {
        formBox.style.transitionDelay = "0.5s";
        formBox.style.height = "0";
        formBox.style.padding = "0";
        articleForm.style.transition = "opacity 0.5s, visibility 0.5s";
        articleForm.style.transitionDelay = "0";
        articleForm.style.opacity = "0";
        articleForm.style.visibility = "hidden";
        toggleButton.innerHTML = "Write an article"
    } else {
        formBox.style.transitionDelay = "0";
        formBox.style.height = "580px";
        formBox.style.padding = "20px";
        articleForm.style.transition = "opacity 0.5s, visibility 0.5s";
        articleForm.style.transitionDelay = "1.5s";
        articleForm.style.opacity = "1";
        articleForm.style.visibility = "visible";
        toggleButton.innerHTML = "Hide";
    }
}

function toggleCommentForm(toggleButton) {
    commentId = toggleButton.parentElement.id;
    formBox = document.getElementById("comment-form-box-"+commentId);
    commentForm = document.getElementById("comment-form-"+commentId);
    formBox.style.transition = "padding 0.5s, height 1.5s";
    commentForm.addEventListener("transitionend", focusTitleInput);

    if (formBox.style.height == "180px") {
        formBox.style.transitionDelay = "0.5s";
        formBox.style.height = "0";
        formBox.style.padding = "0";
        commentForm.style.transition = "opacity 0.5s, visibility 0.5s";
        commentForm.style.transitionDelay = "0";
        commentForm.style.opacity = "0";
        commentForm.style.visibility = "hidden";
        toggleButton.innerHTML = "Comment"
    } else {
        formBox.style.transitionDelay = "0";
        formBox.style.height = "180px";
        formBox.style.padding = "20px";
        commentForm.style.transition = "opacity 0.5s, visibility 0.5s";
        commentForm.style.transitionDelay = "1.5s";
        commentForm.style.opacity = "1";
        commentForm.style.visibility = "visible";
        toggleButton.innerHTML = "Hide";
    }
}

function isSignupFormValid() {
    var form = document.getElementById("signup-form");
    if (form["password1"].value != form["password2"].value) {
        form["password2"].className = "input-error";
        return false;
    }
    form["password2"].className = "";
    return true;
}

function ajaxCall(url, callback) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            callback(xhttp);
        }
    }
    xhttp.open("GET", url, false);
    xhttp.send();
}

function updateUsernameInput(xhttp) {
    form = document.getElementById("signup-form");
    isUserExist = JSON.parse(xhttp.responseText);
    if (isUserExist) {
        form["username"].className = "input-error";
    } else {
        form["username"].className = "";
    }
}

function isUsernameExist(username) {
    ajaxCall("/is_user_exist/?username=" + username, updateUsernameInput);
}