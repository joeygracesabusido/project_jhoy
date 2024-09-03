$(document).ready(function () {
    // Attach click event to the Add button
    $('#btn_save_branch').click(function () {
      // Get values from input fields
      const branchName = $('#branchName').val ();
      const branchAddress = $('#branchAddress').val();

      // Validate inputs
      if (!branchName || !branchAddress) {
        alert('Please fill in all fields.');
        return;
      }

      // Create data object to send to the API
      const branchData = {
        branch_name: branchName,
        address: branchAddress,
        user: 'current_user' // Replace with the actual user if needed
      };

      // Send AJAX request to insert branch data
      $.ajax({
        url: '/api-insert-branches/', // Adjust the URL if necessary
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(branchData),
        success: function (response) {
          // Handle success response
          alert(response.message);
          // Optionally, reset the form fields
          $('#branchForm')[0].reset();
        },
        error: function (xhr) {
          // Handle error response
          const errorDetail = xhr.responseJSON?.detail || 'An error occurred';
          alert(`Error: ${errorDetail}`);
        }
      });
    });
  });