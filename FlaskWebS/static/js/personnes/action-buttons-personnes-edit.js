// Delete button
document.addEventListener("DOMContentLoaded", function() {
    let deleteBtns = document.querySelectorAll(".delete-btn");
    for (let i = 0; i < deleteBtns.length; i++) {
        deleteBtns[i].addEventListener("click", function() {
            // find the index of the id_marque column
            let headers = document.querySelectorAll("th");
            let idMarqueIndex;
            for (let i = 0; i < headers.length; i++) {
                if (headers[i].textContent === "id_personnes") {
                    idMarqueIndex = i;
                    break;
                }
            }

            // grab the id of the row from the id_marque cell
            let row = this.closest("tr");
            let idMarqueCell = row.cells[idMarqueIndex];
            let id = idMarqueCell.textContent;

            // send a GET request to the /get_data_to_delete_personnes route
            let xhr = new XMLHttpRequest();
            xhr.open("GET", "/get_data_to_delete_personnes?id=" + id);
            xhr.onload = function() {
                if (xhr.status === 200) {
                    // handle successful retrieval of data
                    let response = JSON.parse(xhr.responseText);
                    let dataToDelete = response['data'];
                    let affectedTables = response['affected_tables'];
                    let message = "Are you sure you want to delete this row?\n\n";
                    if (affectedTables.length > 0) {
                        message += "The following tables will be affected:\n";
                        for (let i = 0; i < affectedTables.length; i++) {
                            message += affectedTables[i] + "\n";
                        }
                        message += "\nThe following data will be affected:\n";
                        for (let i = 0; i < dataToDelete.length; i++) {
                            message += "ID: " + dataToDelete[i][0] + " / Nom: " + dataToDelete[i][1] + "\n";
                        }
                    }
                    if (confirm(message)) {
                        // send a POST request to the /delete_row_personnes route
                        let xhr2 = new XMLHttpRequest();
                        xhr2.open("POST", "/delete_row_personnes");
                        xhr2.setRequestHeader(
                            "Content-Type",
                            "application/x-www-form-urlencoded"
                        );
                        xhr2.onload = function() {
                            if (xhr2.status === 200) {
                                // handle successful deletion
                                location.reload();
                            } else {
                                // handle error
                                alert("Error: " + xhr2.status);
                            }
                        };
                        xhr2.send(encodeURI("id=" + id));
                    }
                } else {
                    // handle error
                    alert("Error: " + xhr.status);
                }
            };
            xhr.send();
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
            window.location.href = "/add_personnes_edit";
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
                    if (headers[i].textContent === "id_personnes") {
                        idMarqueIndex = i;
                        break;
                    }
                }

                // grab the id of the row from the id_marque cell
                let row = this.closest("tr");
                let idMarqueCell = row.cells[idMarqueIndex];
                let id = idMarqueCell.textContent;

                // redirect to the modify page with the id as a query parameter
                window.location.href = "/modify_categorie?id=" + encodeURIComponent(id);
            }
        });
    }
});