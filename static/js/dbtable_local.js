var otable;

$(document).ready( function () {
   otable =$('#table_id').DataTable();
} );

$('#table_id').on('dblclick', 'tr', function () {
    var data = otable.row( this ).data();
    console.log(data);
});

