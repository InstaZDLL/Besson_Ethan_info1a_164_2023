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
        if (confirmDelete(row_id)) {
            $.ajax({
                url: '/delete_row_materiel',
                type: 'POST',
                data: {
                    id: row_id
                },
                success: function(response) {
                    // redirect to success page
                    window.location.href = '/success_mat';
                },
                error: function(error) {
                    console.log(error);
                },
                async: false // make request synchronous
            });
        } else {
            // add code here to handle when the user clicks cancel
        }
    });
});

function confirmDelete(row_id) {
    var referencing_tables = [];
    $.ajax({
        url: '/get_referencing_tables',
        type: 'POST',
        data: {
            id: row_id
        },
        async: false,
        success: function(response) {
            referencing_tables = JSON.parse(response).referencing_tables;
        },
        error: function(error) {
            console.log(error);
        }
    });

    if (referencing_tables.length > 0) {
        return confirm("Are you sure you want to delete the row?\nThe following tables will be affected:\n\n" + referencing_tables.join("\n"));
    } else {
        return true;
    }
}


// Add button
document.addEventListener("DOMContentLoaded", function() {
    // add click event listener to all add buttons
    let addBtns = document.querySelectorAll(".add-b");
    addBtns.forEach(function(btn) {
        btn.addEventListener("click", function() {
            // redirect to the add page
            window.location.href = "/add_materiel";
        });
    });
});

// Modify buttom
document.addEventListener("DOMContentLoaded", function() {
    // select all of the .modify-b elements
    let modifyBtns = document.querySelectorAll(".modify-b");
    // attach the click event listener to each .modify-b element
    for (let i = 0; i < modifyBtns.length; i++) {
        modifyBtns[i].addEventListener("click", function() {
            if (confirm("Are you sure you want to modify this row?")) {
                // grab the id of the row from the data-row-id attribute
                let id = this.getAttribute("data-row-id");

                // redirect to the show_modify_materiel page with the id as a query parameter
                window.location.href = "/show_modify_materiel?id=" + encodeURIComponent(id);
            }
        });
    }
});