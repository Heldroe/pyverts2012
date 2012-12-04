$(function() {
	$('#mainsearch').typeahead({source: function(query, process) {
		$.getJSON('/profile/usersearch.json',{'q': query}, function (data) {
			process(data.usernames);
		});
	}});
});