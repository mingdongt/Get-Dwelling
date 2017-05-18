/**
 * Created by mingdongtan on 17/5/17.
 */

// Read data file by using AJAX.

$(document).ready(function() {

    $('#data_source_table').DataTable( {
        "ajax": '/static/ajax/data.json',
        "deferRender": true
    } );
} );
