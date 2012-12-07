$(function() {
    $('#mainsearch').typeahead({source: function(query, process) {
        $.getJSON('/profile/usersearch.json',{'q': query}, function (data) {
            process(data.usernames);
        });
    }, updater: function(item) {
        if (item.substr(15,6) == 'search') return this.query;
        return item;
    }, highlighter: function(item){
        return item;
    }, sorter: function(items) {
        for (var i = 0; i < items.length; i++) {
            if (items[i].substr(15,6) == 'search') {
                var t = items[0];
                items[0] = items[i];
                items[i] = t;
                break;
            }
        }
        return items;
    }});
    konami = new Konami()
    konami.load("http://ac.heldroe.org/");
});

(function(window, PhotoSwipe) {
    document.addEventListener('DOMContentLoaded', function() {
        var options = {},
            instance = PhotoSwipe.attach( window.document.querySelectorAll('#Gallery a'), options );
    }, false);
}(window, window.Code.PhotoSwipe));