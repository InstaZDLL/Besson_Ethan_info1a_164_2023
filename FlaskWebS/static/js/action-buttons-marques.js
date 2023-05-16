// Delete button
document.addEventListener("DOMContentLoaded", function() {
    // select all of the .delete-btn elements
    let deleteBtns = document.querySelectorAll(".delete-btn");
    // attach the click event listener to each .delete-btn element
    for (let i = 0; i < deleteBtns.length; i++) {
        deleteBtns[i].addEventListener("click", function() {
            if (confirm("Are you sure you want to delete this row?")) {
                // find the index of the id_marque column
                let headers = document.querySelectorAll("th");
                let idMarqueIndex;
                for (let i = 0; i < headers.length; i++) {
                    if (headers[i].textContent === "id_marque") {
                        idMarqueIndex = i;
                        break;
                    }
                }

                // grab the id of the row from the id_marque cell
                let row = this.closest("tr");
                let idMarqueCell = row.cells[idMarqueIndex];
                let id = idMarqueCell.textContent;

                // send a POST request to the /delete_row_marque route
                let xhr = new XMLHttpRequest();
                xhr.open("POST", "/delete_row_marque");
                xhr.setRequestHeader(
                    "Content-Type",
                    "application/x-www-form-urlencoded"
                );
                xhr.onload = function() {
                    if (xhr.status === 200) {
                        // handle successful deletion
                        location.reload();
                    } else {
                        // handle error
                        alert("Error: " + xhr.status);
                    }
                };
                xhr.send(encodeURI("id=" + id));
            }
        });
    }
});

// Add button
document.addEventListener("DOMContentLoaded", function() {
    // add click event listener to all add buttons
    let addBtns = document.querySelectorAll(".add-btn");
    addBtns.forEach(function(btn) {
        btn.addEventListener("click", function() {
            // redirect to the add page
            window.location.href = "/add_marque_form";
        });
    });
});

// Modify button
document.addEventListener("DOMContentLoaded", function() {
    // select all of the .modify-btn elements
    let modifyBtns = document.querySelectorAll(".modify-btn");
    // attach the click event listener to each .modify-btn element
    for (let i = 0; i < modifyBtns.length; i++) {
        modifyBtns[i].addEventListener("click", function() {
            if (confirm("Are you sure you want to modify this row?")) {
                // find the index of the id_marque column
                let headers = document.querySelectorAll("th");
                let idMarqueIndex;
                for (let i = 0; i < headers.length; i++) {
                    if (headers[i].textContent === "id_marque") {
                        idMarqueIndex = i;
                        break;
                    }
                }

                // grab the id of the row from the id_marque cell
                let row = this.closest("tr");
                let idMarqueCell = row.cells[idMarqueIndex];
                let id = idMarqueCell.textContent;

                // redirect to the modify page with the id as a query parameter
                window.location.href = "/modify_marque?id=" + id;
            }
        });
    }
});