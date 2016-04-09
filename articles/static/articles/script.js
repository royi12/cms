function focusTitleInput()
{
    document.getElementById("id_title").focus();
}

function toggleArticleForm()
{
    formBox = document.getElementById("article-form-box");
    articleForm = document.getElementById("article-form");
    toggleButton = document.getElementById("write-article-button");
    formBox.style.transition = "padding 0.5s, height 1.5s";
    articleForm.addEventListener("transitionend", focusTitleInput);

    if (formBox.style.height == "580px")
    {
        formBox.style.transitionDelay = "0.5s";
        formBox.style.height = "0";
        formBox.style.padding = "0";
        articleForm.style.transition = "opacity 0.5s, visibility 0.5s";
        articleForm.style.transitionDelay = "0";
        articleForm.style.opacity = "0";
        articleForm.style.visibility = "hidden";
        toggleButton.innerHTML = "Write an article"
    }
    else
    {
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