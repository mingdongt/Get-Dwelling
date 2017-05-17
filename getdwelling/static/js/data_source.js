/**
 * Created by mingdongtan on 17/5/17.
 */


$(document).ready(function() {

    $('#data_source_table').DataTable( {
        "ajax": '/static/ajax/data.json',
        "deferRender": true
    } );
} );
