$(document).ready(function() {
    $('.delete-b').click(function() {
        var row_id = $(this).data('row-id');
        $.ajax({
            url: '/delete_row_materiel',
            type: 'POST',
            data: {id: row_id},
            success: function(response) {
                console.log(response);
                // reload the page to see the updated table
                location.reload();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
