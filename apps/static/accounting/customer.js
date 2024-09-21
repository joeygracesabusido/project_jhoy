getBranch();
let isUpdating = false;
let customer_list = {};
let selectedCustomer = null;
let clickTimer = null;
let bussiness_name = "";
let name_of_tax_payer = "";
let tin = "";
let rdo = "";
let address = "";
let tax_type = "Vatable";
let description = "Customer";
let table_customer_list = $("#table_customer_list");

const bussiness_name_el = $("#bussiness_name");
const name_of_tax_payer_el = $("#name_of_tax_payer");
const tin_el = $("#tin");
const rdo_el = $("#rdo");
const address_el = $("#address");

const tax_type_el = $("#tax_type");
const description_el = $("#description");

bussiness_name_el.addEventListener("input", function (event) {
  bussiness_name = event.target.value;
  console.log("bussiness_name", bussiness_name);
});
name_of_tax_payer_el.addEventListener("input", function (event) {
  name_of_tax_payer = event.target.value;
  console.log(name_of_tax_payer);
});
tin_el.addEventListener("input", function (event) {
  tin = event.target.value;
  console.log(tin);
});
rdo_el.addEventListener("input", function (event) {
  rdo = event.target.value;
  console.log(rdo);
});
address_el.addEventListener("input", function (event) {
  address = event.target.value;
  console.log(address);
});

tax_type_el.addEventListener("change", function (event) {
  tax_type = event.target.value;
  console.log(tax_type);
});
description_el.addEventListener("change", function (event) {
  description = event.target.value;
  console.log(description);
});

async function getBranch() {
  try {
    const response = await fetch(`/api-get-customer-profiles/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (response.ok) {
      customer_list = await response.json();
      table_customer_list.empty(); // Clear the table before appending rows
      let i = 0;
      customer_list.forEach((element) => {
        console.log(element);
        table_customer_list.append(makeBranchRow(i++, element));
      });
    } else {
      const error = await response.json();
      alert(`Error: ${error.detail}`);
    }
  } catch (error) {
    console.error("An error occurred:", error);
    alert("An error occurred while fetching the branches.");
  }
}

function makeBranchRow(index, data) {
  return `<tr id='${"customer_row_" + index}' onClick="openToEdit(${index},'${
    "customer_row_" + index
  }')">
  <td>${data.id}</td>
  <td>${data.bussiness_name}</td>
  <td>${data.description}</td>
</tr>`;
}

function isDoubleClick() {
  if (clickTimer) {
    clearTimeout(clickTimer);
    clickTimer = null;
    return true;
  } else {
    clickTimer = setTimeout(() => {
      clickTimer = null;
    }, 250); // Delay to detect double-click
    return false;
  }
}

function openToEdit(index, customer_row_id) {
  if (isDoubleClick() === true) {
    isUpdating = true;
    $("#btn_save_branch").text("Update");
    $("#table_customer_list tr").removeClass("table-primary");
    console.log(`#${customer_row_id}`);
    // Load selected branch data into form fields
    let data = customer_list[index];
    bussiness_name_el.val(data.bussiness_name);
    name_of_tax_payer_el.val(data.name_of_tax_payer);
    tin_el.val(data.tin);
    rdo_el.val(data.rdo);
    address_el.val(data.address);
    tax_type_el.val(data.tax_type);
    description_el.val(data.description);
    $("#id").val(data.id);
    $(`#${customer_row_id}`).addClass("table-primary");
  }
}

$(document).ready(function () {
  // Initial fetch of branch data
  getBranch();

  // // Handle save (add or update) button click
  // $("#btn_save_branch").click(saveOrUpdateBranch);

  // // Handle reset button click (to cancel update and reset form)
  // $("#btn_update_branch").click(resetForm);
});
