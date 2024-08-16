 // jQuery to open the modal
 $('#insert_invt_items_btn').click(function() {
    $('#insert_invt_items_modal').modal('show');
});



// this function is for inserting inventory list item
$(document).ready(function() {
    $('#btn_save_inventory').click(function() {
        var inventoryData = {
            inventory_company: $('#jo_offices').val(),
            inventory_item: $('#inventory_item').val(),
            inventory_purchase_date: $('#inventory_purchase_date').val(),
            inventory_si_no: $('#inventory_si_no').val(),
            inventory_quantity: $('#inventory_quantity').val(),
            inventory_brand: $('#inventory_brand').val(),
            inventory_amount: parseFloat($('#inventory_amount').val()),
            inventory_serial_no: $('#inventory_serial_no').val(),
            inventory_user: $('#inventory_user').val(),
            inventory_department: $('#inventory_department').val(),
            inventory_date_issue: $('#inventory_date_issue').val(),
            inventory_description: $('#inventory_description').val()
        };

        console.log(inventoryData)
        $.ajax({
            url: '/api-insert-inventory-item',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(inventoryData),
            success: function(response) {
                alert('Data has been saved');
                window.location.href = "/inventory-list/"; // Redirect to the inventory list page
            },
            error: function(xhr, status, error) {
                alert('Error: ' + error);
            }
        });
    });
});





// $(document).ready(function() {
//     // Initialize DataTables on the table
//     var table = $('#table_inventory').DataTable();
//     // initializeDataTable()
//     function fetchInventoryData() {
//         $.ajax({
//             url: '/api-get-inventory-list',
//             type: 'GET',
//             success: function(data) {
//                 table.clear(); // Clear any existing data

//                 data.forEach(function(item) {
//                     table.row.add([

//                         item.inventory_company,
//                         item.inventory_item,
//                         item.inventory_purchase_date,
//                         item.inventory_si_no,
//                         item.inventory_quantity,
//                         item.inventory_brand,
//                         item.inventory_serial_no,
//                         item.inventory_date_issue,
//                         item.inventory_user,
//                         item.inventory_department,
//                         `<td>
//                             <a href="/inventory-update/${item.id}">
//                                 <button type="button" class="btn btn-primary">
//                                     <i class="fas fa-database"></i> Edit
//                                 </button>
//                             </a>
//                         </td>`
//                     ]).draw(false);
                   
//                 });
//                 // initializeDataTable()
//             },
            

//             error: function(xhr, status, error) {
//                 alert('Error: ' + error);
//             }
//         });
//     }

//     // Fetch inventory data on page load
//     fetchInventoryData();
// });


$(document).ready(function() {
   
    function fetchAndDisplayInventoryList() {
        $.ajax({
            url: '/api-get-inventory-list',  // API endpoint
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                var tableBody = $('#table_inventory_list');
                tableBody.empty();  // Clear existing table rows
                
                // Iterate over each item in the data
                data.forEach(function(item) {
                    // Create a new row
                    var newRow = $('<tr></tr>');

                    // Append cells to the row
                    newRow.append('<td>' + item.inventory_company + '</td>');
                    newRow.append('<td>' + item.inventory_item + '</td>');
                    newRow.append('<td>' + item.inventory_purchase_date + '</td>');
                    newRow.append('<td>' + item.inventory_si_no + '</td>');
                    newRow.append('<td>' + item.inventory_quantity + '</td>');
                    newRow.append('<td>' + item.inventory_brand + '</td>');
                    newRow.append('<td>' + item.inventory_serial_no + '</td>');
                    newRow.append('<td>' + item.inventory_date_issue + '</td>');
                    newRow.append('<td>' + item.inventory_user + '</td>');
                    newRow.append('<td>' + item.inventory_department + '</td>');
                    
                    newRow.append('<td><a href="/job-order/' + item.id + '"> \
                        <button type="button" class="btn btn-primary"> \
                        <i class="fas fa-database"></i> Edit</button></a></td>');

                    // Append the new row to the table body
                    tableBody.append(newRow);
                    
                    // Apply red color if jo_turn_overtime is empty
                    if (!item.inventory_item) {
                        newRow.css('background-color', 'green');
                    }

                   
                });
                initializeDataTable()
            },
            error: function(xhr, status, error) {
                console.error('Error fetching job orders:', error);
                alert('Error fetching job orders. Please try again later.');
            }
        });
    }

    // Fetch job orders on page load
    fetchAndDisplayInventoryList();
});



const initializeDataTable = () => {
    $('#table_inventory').DataTable();
};

// let table = new DataTable('#table_inventory_list');