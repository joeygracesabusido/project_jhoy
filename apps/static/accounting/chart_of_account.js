$(document).ready(function() {
    // Function to fetch and display journal entries
    
    
    function loadChartofAccounts() {
        $.ajax({
            url: '/api-get-chart-of-accounts/',
            method: 'GET',
            success: function(data) {
                let rows = '';

                // Loop through the data and create table rows
                data.forEach(function(entry) {
                    rows += `
                        <tr>
                            <td>${entry.chart_of_account_code}</td>
                            <td>${entry.chart_of_account}</td>
                           
                            
                            <td>
                                <!-- Add action buttons here if needed -->
                                <!--<button class="btn btn-primary btn-sm">Edit</button>-->

                                <a href="/api-update-journal-entry-temp/${entry.reference}"> \
                                <button type="button" class="btn btn-primary btn-sm"> \
                                 Edit</button></a>

                                <!--<button class="btn btn-danger btn-sm">Delete</button> -->
                            </td>
                        </tr>
                    `;
                });

                // Append rows to the table body
                $('#table_chart_of_account_list').html(rows);
                initializeDataTable()
            },
            
            error: function(xhr, status, error) {
                console.error('Error fetching journal entries:', error);
            }
        });
    }

    // Load journal entries when the page is loaded
    loadChartofAccounts();
});

// this is for DataTable
const initializeDataTable = () => {

    new DataTable('#table_chart_of_account', {
        layout: {
            topStart: 'buttons'
        },
        buttons: ['copy',  {
            extend: 'csv',
            filename: 'Chart of Account', // Custom name for the exported CSV file
            title: 'Chart of Account' // Optional: Title for the CSV file's content
        }]
    });

    };


// this function is for autocomplete for account type
    // jQuery.noConflict();
    // jQuery(document).ready(function($) {
    //     $(document).on('focus', '[id^="accoun_type"]', function() {
    //         $(this).autocomplete({
    //             source: function(request, response) {
    //                 $.ajax({
    //                     url: "/api-autocomplete-account-type/", // Replace with your actual endpoint
    //                     data: { term: request.term },
    //                     dataType: "json",
    //                     success: function(data) {
    //                         response(data);
    //                     },
    //                     error: function(err) {
    //                         console.error("Error fetching autocomplete data:", err);
    //                     }
    //                 });
    //             },
    //             minLength: 0,
    //             select: function(event, ui) {
    //                 $(this).val(ui.item.value);
    //                 $(this).val(ui.item.id);
                    
    //                 return false;
    //             }
    //         });
    //     });
    // });

    jQuery.noConflict();
    jQuery(document).ready(function($) {
        // Autocomplete for the account type input
        $("#accoun_type").autocomplete({
            source: function(request, response) {
                $.ajax({
                    url: "/api-autocomplete-account-type/",  // Replace with your FastAPI endpoint
                    dataType: "json",
                    data: {
                        term: request.term // Pass the term as a query parameter
                    },
                    success: function(data) {
                        console.log("Autocomplete data:", data); // Debugging line to see data in console
                        // Map the response data to the format expected by jQuery UI autocomplete
                        response(data.map(function(item) {
                            return {
                                label: item.value, // Ensure the correct label is set
                                value: item.value, // Ensure the correct value is set
                                id: item.id
                            };
                        }));
                    },
                    error: function(err) {
                        console.error("Error fetching autocomplete data:", err);
                    }
                });
            },
            minLength: 0, // Minimum length of input before triggering autocomplete
            select: function(event, ui) {
                // Set the selected item values in the appropriate fields
                $("#accoun_type").val(ui.item.value); // Set the display value
                $("#account_type_id").val(ui.item.id); // Set the hidden value
                return false; // Prevent the default action
            }
        });
    });


    jQuery.noConflict();
    jQuery(document).ready(function($) {
        // Handle the click event for the "Save changes" button
        $('#insert_chart_of_account .btn-primary').on('click', function() {
            // Gather form data
            const data = {
                chart_of_account_code: $('#chart_of_account_code').val(),
                chart_of_account: $('#chart_of_account').val(),
                account_type: $('#accoun_type').val(),
                account_type_id: $('#account_type_id').val(),
                description: $('#description').val()
            };

            // Send the data to the FastAPI endpoint
            $.ajax({
                url: '/api-insert-chart-of-account/', // FastAPI endpoint
                type: 'POST',
                contentType: 'application/json', // Specify JSON content type
                data: JSON.stringify(data), // Convert data to JSON
                success: function(response) {
                    // Display success message or perform further actions
                    alert(response.message);
                    $('#insert_chart_of_account').modal('hide'); // Hide the modal
                    location.reload(); // Reload the page or update the UI as needed
                },
                error: function(xhr, status, error) {
                    // Handle any errors that occurred during the request
                    alert('Error: ' + xhr.responseText);
                    console.error('Error details:', xhr);
                }
            });
        });
    });
    