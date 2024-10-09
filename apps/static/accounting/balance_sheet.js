// $(document).ready(function() {
//     $('#btn_search').on('click', function() {
//         // Get the selected dates
//         const dateFrom = $('#date_from').val();
//         const dateTo = $('#date_to').val();

//         // Define the GraphQL query
//         const query = `
//             query GetBalanceSheetDetails2($datefrom: String, $dateto: String) {
//                 getBalanceSheetDetails(datefrom: $datefrom, dateto: $dateto) {
//                     chartOfAccount
//                     amount
//                     accountType
//                 }
//             }
//         `;

//         // Set up the request
//         const requestData = JSON.stringify({
//             query: query,
//             variables: {
//                 datefrom: dateFrom,
//                 dateto: dateTo
//             }
//         });

//         // Make the AJAX request to the GraphQL endpoint
//         $.ajax({
//             url: '/graphql', // Replace with your actual GraphQL endpoint URL
//             method: 'POST',
//             contentType: 'application/json',
//             data: requestData,
//             success: function(response) {
//                 const data = response.data.getBalanceSheetDetails;

//                 // Clear the table body
//                 $('#table_balance_sheet_report_list').empty();

//                 if (data && data.length > 0) {
//                     // Populate the table with the fetched data
//                     data.forEach(item => {
//                         const row = `
//                             <tr>
//                                 <td>${item.accountType}</td>
//                                 <td>${item.chartOfAccount}</td>
//                                 <td>${item.amount.toFixed(2)}</td>
//                             </tr>
//                         `;
//                         $('#table_balance_sheet_report_list').append(row);
//                     });
//                 } else {
//                     // If no data is returned, add a row indicating no results
//                     $('#table_balance_sheet_report_list').append(`
//                         <tr>
//                             <td colspan="3">No data available for the selected date range.</td>
//                         </tr>
//                     `);
//                 }
//             },
//             error: function(error) {
//                 console.error('Error fetching data:', error);
//                 // Handle error
//                 $('#table_balance_sheet_report_list').html(`
//                     <tr>
//                         <td colspan="3">An error occurred while fetching data.</td>
//                     </tr>
//                 `);
//             }
//         });
//     });
// });


// $(document).ready(function() {
//     $('#btn_search').on('click', function() {
//         const datefrom = $('#date_from').val();
//         const dateto = $('#date_to').val();

//         $.ajax({
//             url: '/graphql', // Replace with your actual GraphQL endpoint URL
//             method: 'POST',
//             contentType: 'application/json',
//             data: JSON.stringify({
//                 query: `
//                 query {
//                     getBalanceSheetDetails2(datefrom: "${datefrom}", dateto: "${dateto}") {
//                         accountType
//                         chartOfAccount
//                         amount
//                     }
//                 }`
//             }),
//             success: function(response) {
//                 const data = response.data.getBalanceSheetDetails2;

//                 if (!data || data.length === 0) {
//                     $('#balanceSheetContainer').html('<p>No data found for the selected date range.</p>');
//                     return;
//                 }

//                 // Group data by account type
//                 const groupedData = {};
//                 data.forEach(item => {
//                     if (!groupedData[item.accountType]) {
//                         groupedData[item.accountType] = [];
//                     }
//                     groupedData[item.accountType].push(item);
//                 });

//                 // Generate HTML content
//                 let html = '';
//                 $.each(groupedData, function(accountType, details) {
//                     html += `<h3>${accountType}</h3>`;
//                     html += '<table class="balance-sheet-table" border="1" cellspacing="0" cellpadding="5">';
//                     html += '<tr><th>Chart of Account</th><th>Amount</th></tr>';
//                     details.forEach(detail => {
//                         html += `
//                             <tr>
//                                 <td>${detail.chartOfAccount}</td>
//                                 <td>${detail.amount.toFixed(2)}</td>
//                             </tr>`;
//                     });
//                     html += '</table><br>';
//                 });

//                 // Display the generated content
//                 $('#balanceSheetContainer').html(html);
//             },
//             error: function(error) {
//                 console.error('Error fetching data:', error);
//                 $('#balanceSheetContainer').html('<p>An error occurred while fetching data.</p>');
//             }
//         });
//     });
// });

// $(document).ready(function() {
//     $('#btn_search').on('click', function() {
//         const datefrom = $('#date_from').val();
//         const dateto = $('#date_to').val();

//         $.ajax({
//             url: '/graphql', // Replace this with your actual GraphQL endpoint
//             method: 'POST',
//             contentType: 'application/json',
//             data: JSON.stringify({
//                 query: `
//                 query {
//                     getBalanceSheetDetails3(datefrom: "${datefrom}", dateto: "${dateto}") {
//                         accountType
//                         chartOfAccount
//                         amount
//                     }
//                 }`
//             }),
//             success: function(response) {
//                 const data = response.data.getBalanceSheetDetails3;
//                 console.log('EHLOOOOOO', data)
//                 // Clear any previous data
//                 $('#table_balance_sheet_report_list').empty();

//                 if (!data || data.length === 0) {
//                     $('#table_balance_sheet_report_list').html('<tr><td colspan="3">No data found for the selected date range.</td></tr>');
//                     return;
//                 }

//                 const totals = {};

//                 // First pass to calculate totals
//                 data.forEach(item => {
//                     if (!totals[item.accountType]) {
//                         totals[item.accountType] = 0;
//                     }
//                     totals[item.accountType] += item.amount;
//                 });

//                 // Second pass to display the data
//                 const displayedAccountTypes = [];

//                 data.forEach(item => {
//                     const showAccountType = !displayedAccountTypes.includes(item.accountType);

//                     // Display account type and increment the displayed list
//                     if (showAccountType) {
//                         displayedAccountTypes.push(item.accountType);
//                     }

//                     $('#table_balance_sheet_report_list').append(`
//                         <tr>
//                             <td>${showAccountType ? item.accountType : ''}</td>
//                             <td>${item.chartOfAccount}</td>
//                             <td>${item.amount.toFixed(2)}</td>
//                         </tr>
//                     `);
//                 });

//                 // Append total rows for each account type
//                 for (const accountType in totals) {
//                     $('#table_balance_sheet_report_list').append(`
//                         <tr>
//                             <td><strong>Total ${accountType}</strong></td>
//                             <td></td>
//                             <td><strong>${totals[accountType].toFixed(2)}</strong></td>
//                         </tr>
//                     `);
//                 }

//             },
//             error: function(error) {
//                 console.error('Error fetching data:', error);
//                 $('#table_balance_sheet_report_list').html('<tr><td colspan="3">An error occurred while fetching data.</td></tr>');
//             }
//         });
//     });

//     function groupDataByAccountType(data) {
//         return data.reduce((acc, item) => {
//             if (!acc[item.accountType]) {
//                 acc[item.accountType] = [];
//             }
//             acc[item.accountType].push(item);
//             return acc;
//         }, {});
//     }
// });


$(document).ready(function() {
    $('#btn_search').on('click', function() {
        const datefrom = $('#date_from').val();
        const dateto = $('#date_to').val();

        $.ajax({
            url: '/graphql', // Replace this with your actual GraphQL endpoint
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                query: `
                query {
                    getBalanceSheetDetails3(datefrom: "${datefrom}", dateto: "${dateto}") {
                        accountType
                        details {
                            chartOfAccount
                            amount
                        }
                    }
                }`
            }),
            success: function(response) {
                const data = response.data.getBalanceSheetDetails3;
                $('#table_balance_sheet_report_list').empty();

                if (!data || data.length === 0) {
                    $('#table_balance_sheet_report_list').html('<tr><td colspan="3">No data found for the selected date range.</td></tr>');
                    return;
                }

                const totals = {};

                // Loop through each account type and its details
                data.forEach(item => {
                    if (!totals[item.accountType]) {
                        totals[item.accountType] = 0;
                    }

                    // Display each detail for the account type
                    item.details.forEach(detail => {
                        totals[item.accountType] += detail.amount;

                        $('#table_balance_sheet_report_list').append(`
                            <tr>
                                <td>${item.accountType}</td>
                                <td>${detail.chartOfAccount}</td>
                                <td>${detail.amount.toFixed(2)}</td>
                            </tr>
                        `);
                    });
                });

                // Append total rows for each account type
                for (const accountType in totals) {
                    $('#table_balance_sheet_report_list').append(`
                        <tr>
                            <td><strong>Total ${accountType}</strong></td>
                            <td></td>
                            <td><strong>${totals[accountType].toFixed(2)}</strong></td>
                        </tr>
                    `);
                }
            },
            error: function(error) {
                console.error('Error fetching data:', error);
                $('#table_balance_sheet_report_list').html('<tr><td colspan="3">An error occurred while fetching data.</td></tr>');
            }
        });
    });

    function groupDataByAccountType(data) {
        return data.reduce((acc, item) => {
            if (!acc[item.accountType]) {
                acc[item.accountType] = [];
            }
            acc[item.accountType].push(item);
            return acc;
        }, {});
    }
});
