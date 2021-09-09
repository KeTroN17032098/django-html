// Basic example
$(document).ready(function () {
	$('#dtBasicExample').DataTable({
	  "pagingType": 'first_last_numbers',
	  "paging": false,// false to disable pagination (or any other option)
	});
	$('.dataTables_length').addClass('bs-select');
  });