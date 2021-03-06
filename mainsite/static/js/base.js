document.addEventListener('DOMContentLoaded', function () {
    $('body #article-like-heart').click(function () {
        $(this)
            .toggleClass('far fa-heart fa-lg')
            .toggleClass('fas fa-heart fa-lg');
    });
    $('#article-watchers-eye-not-watched').click(function () {
        $(this)
            .toggleClass('far fa-eye fa-lg')
            .toggleClass('fas fa-eye fa-lg');
    });
});

//Like story
document.addEventListener('DOMContentLoaded', function () {
    $('a.like-button').click(function (e) {
        e.preventDefault();
        $.post ('{% url "story:like_story" %}',
            {
                id: $(this).data('id'),
                action: $(this).data('action')
            },
            function (data) {
                if (data['status'] == 'ok') {
                    var previous_action = $('a.like-button').data('action');
                    $('a.like-button').data('action', previous_action == 'like' ? 'unlike' : 'like');
                    var previous_likes = parseInt($('span.count .total').text());
                    $('span.count .total').text(previous_action == 'like' ? previous_likes + 1 : previous_likes - 1);
                }
            }
        );
    });

});


// Character count

var textarea = document.querySelector("textarea");

if (textarea != null) {
    var maxlength = textarea.getAttribute("maxlength");
    textarea.addEventListener("input", function () {
        var currentLength = this.value.length;
        if (currentLength == maxlength) {
            document.getElementById("count").innerHTML = "No more characters left";
        } else {
            document.getElementById("count").innerHTML = (maxlength - currentLength) + " characters left";
        }
    });
}


// Toggle hide

var hideAuthor = document.getElementsByClassName("article-paragraph-author-name");
var hideAuthorImage = document.getElementsByClassName("article-paragraph-author-image");
var hideStoryLike = document.getElementsByClassName('nextparagraph-like');
var hideAddParagraphForm = document.getElementById('add-paragraph-form');
var hideStoryDate = document.getElementById('story-date');
var hideStoryTags = document.getElementById('story-tags');
var hideFirstParaStorySubhead = document.getElementById('first-para-sub-head');
var hideNextParaStorySubhead = document.getElementById('next-para-sub-head');
var hideStoryWatchersIcon = document.getElementById('article-watchers-eye-not-watched');
var hideStoryWatchersNumber = document.getElementById('article-watcher-number');

var toggle = function () {
    for (var i = 0; i < hideAuthor.length; i++) {
        hideAuthor[i].classList.toggle('display-none');
        hideAuthorImage[i].classList.toggle('display-none');
    }
    for (var i = 0; i < hideStoryLike.length; i++) {
        hideStoryLike[i].classList.toggle('display-none');
    }
    hideStoryTags.classList.toggle('display-none');
    hideStoryDate.classList.toggle('display-none');
    hideFirstParaStorySubhead.classList.toggle('display-none');
    hideNextParaStorySubhead.classList.toggle('display-none');
    hideStoryWatchersIcon.classList.toggle('display-none');
    hideStoryWatchersNumber.classList.toggle('display-none');

};
document.getElementById('toggle-hide').addEventListener('click', toggle);


//CSRF token
var csrftoken = Cookies.get('csrftoken');

function csrfSafeMethod(method) {
// these HHTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});