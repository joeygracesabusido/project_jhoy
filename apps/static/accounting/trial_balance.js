$(document).ready(function () {
    // Fetch and display data when the search button is clicked
    $('#btn_search').click(function () {
        const dateFrom = $('#datefrom').val();
        const dateTo = $('#dateto').val();

        // Make an AJAX GET request to the FastAPI endpoint
        $.ajax({
            url: '/trial-balance-report/',
            type: 'GET',
            data: {
                datefrom: dateFrom,
                dateto: dateTo
            },
            success: function (response) {
                // Clear the table body before appending new data
                $('#table_trialbalance_list').empty();

                // Loop through the response data and append it to the table
                response.data.forEach(function (item) {
                    const row = `
                        <tr>
                            <td>${item.chart_of_account}</td>
                            <td>${item.debit.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                            <td>${item.credit.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                        </tr>
                    `;
                    $('#table_trialbalance_list').append(row);
                    
                });
                initializeDataTable()
            },
            error: function (xhr, status, error) {
                alert('An error occurred: ' + error);
            }
        });
    });
});

// this is for DataTable
const initializeDataTable = () => {

    new DataTable('#table_trial_balance', {
        layout: {
            topStart: 'buttons'
        },
        buttons: ['copy', 'csv']
    });
}
