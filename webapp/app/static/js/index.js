

function hide() {
  document.getElementById("loader").style.display = 'none'; 
}



function api_call(folder_name, id)
{

  var result;
  var url = `/api/list-ionograms/${folder_name}/${id}`;
  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      result = this.responseText;
    }
  }

xhttp.open("GET", url, true);
xhttp.send();
return result; 
}


function displayMessage(folder_name) {

  window.open('/log', '_blank');
  var transmitter_id = document.getElementById("transmitter_id").value;
  var url = `/api/list-ionograms/${folder_name}/${transmitter_id}`;
  var redirect_url = `/list-ionograms/${folder_name}/${transmitter_id}`;

  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("loader").style.display = "none";
      window.location.href = redirect_url;
    }
  }

xhttp.open("GET", url, true);
xhttp.send();

document.getElementById("loader").innerHTML = `<div class="sr-only text-center card text-primary" style="font-size: 30px;">Processing files... <i></i><div></div>
<div></span>`; 
}


function clear_classification()
{
  var url = '/clear-classification';
  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      window.location.reload();
    }
  }

xhttp.open("GET", url, true);
xhttp.send();
}


function get_latest_log()
{
  alert('')
  window.location.reload();
}


function displaymodel()
{
  document.getElementById('exampleModalCenter').style.display = 'block'
}


// function clear_classification()
// {
//   document.getElementById('start_date').value = '';
//   document.getElementById('end_date').value = '';
//   document.getElementById('close').click();
// }
