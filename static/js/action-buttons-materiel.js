// Filter button
$(document).ready(function() {
    var columnsHidden = false;
    $("#hideColumns").click(function() {
        if (columnsHidden) {
            // Show the date_achat and date_expi columns
            $("th:contains('Date of Purchase'), th:contains('Expiration Date')").show();
            $("td:nth-child(5), td:nth-child(6)").show();
            $(this).text("Hide Columns");
            columnsHidden = false;
        } else {
            // Hide the date_achat and date_expi columns
            $("th:contains('Date of Purchase'), th:contains('Expiration Date')").hide();
            $("td:nth-child(5), td:nth-child(6)").hide();
            $(this).text("Unhide");
            columnsHidden = true;
        }
    });
});
// Delete Button
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
