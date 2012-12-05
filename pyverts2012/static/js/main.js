$(function() {
    $('#mainsearch').typeahead({source: function(query, process) {
        $.getJSON('/profile/usersearch.json',{'q': query}, function (data) {
            process(data.usernames);
        });
    }});
});

(function(window, PhotoSwipe) {
    document.addEventListener('DOMContentLoaded', function() {
        var options = {},
            instance = PhotoSwipe.attach( window.document.querySelectorAll('#Gallery a'), options );
    }, false);
}(window, window.Code.PhotoSwipe));