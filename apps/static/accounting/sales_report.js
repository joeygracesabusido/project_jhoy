$(document).ready(function() {
    // Function to fetch and display journal entries
    
    
    function loadJournalEntries() {
        $.ajax({
            url: '/api-get-sales-report/',
            method: 'GET',
            success: function(data) {
                let rows = '';

                // Loop through the data and create table rows
                data.forEach(function(entry) {
                    rows += `
                        <tr>
                            <td>${entry.date}</td>
                            <td>${entry.branch}</td>
                            <td>${entry.customer_id}</td>
                            <td>${entry.tin}</td>
                            <td>${entry.tax_type}</td>
							<td>${entry.chart_of_account}</td>

                            <td>${entry.debit_amount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                            <td>${entry.credit_amount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>

                            
       
                        </tr>
                    `;
                });

                // Append rows to the table body
                $('#table_sales_report_list').html(rows);
                initializeDataTable()
            },
            
            error: function(xhr, status, error) {
                console.error('Error fetching journal entries:', error);
            }
        });
    }

    // Load journal entries when the page is loaded
    loadJournalEntries();
});

// this is for DataTable
const initializeDataTable = () => {

    new DataTable('#table_sales_report', {
        layout: {
            topStart: 'buttons'
        },
        buttons: [{
            extend: 'copy',
            text: 'Copy to Clipboard', // Button label
            title: 'Trial Balance Report', // Title for the copied data
            filename: 'Trial_Balance_Report', // Custom filename
            exportOptions: {
                columns: ':visible' // Export only visible columns
            }
        },
        {
            extend: 'csv',
            text: 'Export to CSV', // Button label
            title: 'Trial Balance Report', // Title in CSV file
            filename: 'Trial_Balance_Report', // Custom filename without file extension
            exportOptions: {
                columns: ':visible' // Export only visible columns
            }
        }]
    });


    };




// <td>${entry.debit.toLocaleString()}</td>
// <td>${entry.credit.toLocaleString()}

