console.log("Hi there");

//mark as read
$(document).ready(function () {
    function getCSRFToken() {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Check if the cookie name starts with 'csrftoken'
                if (cookie.substring(0, 'csrftoken'.length + 1) === ('csrftoken' + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring('csrftoken'.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
//});


    $("#markAllReadBtn").on("click", function () {

         var csrfToken = getCSRFToken();
         var name = $('#sender_name').val();
         var email = $('#sender_email').val();
         var subject = $('#sender_subject').val();
         var message = $('#sender_message').val();
         console.log("Hi there");
         var spinner = $('.spinner');
         spinner.show();
        $.ajax({
            type: "POST",
            url: '/json_response',
            data: {
                name: name,
                email: email,
                subject: subject,
                message: message,
            },
            headers: {
                "X-CSRFToken": csrfToken
            },
            success: function (data) {
                console.log("All notifications marked as read");
                spinner.hide();
                $('#responseMessage').show();
            },
            error: function (error) {
                console.error("Error marking all notifications as read", error);
                                spinner.hide();
                $('#responseMessage').show();
            }
        });
    });
});
