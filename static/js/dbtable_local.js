$(document).ready( function () {
    $('#table_id').DataTable();
} );

$('#table tbody').on('dblclick', 'tr', function () {
    var data = otable.row( this ).data();
    var col1 = data.col1;
    var col2 = data.col2;
});

