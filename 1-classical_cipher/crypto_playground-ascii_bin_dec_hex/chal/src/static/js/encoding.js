
hex_string = document.getElementById('hex-string');
hex_hexstring = document.getElementById('hex-hexstring');

hex_string.addEventListener('input', () => {
  var value = hex_string.value;
  hex_hexstring.value = str2hexstr(value);
})

hex_hexstring.addEventListener('input', () => {
  var value = hex_hexstring.value;
  hex_string.value = hexstr2str(value);
})

base64_string = document.getElementById('base64-string');
base64_base64string = document.getElementById('base64-base64string');

base64_string.addEventListener('input', () => {
  var value = base64_string.value;
  base64_base64string.value = btoa(value);
})

base64_base64string.addEventListener('input', () => {
  var value = base64_base64string.value;
  base64_string.value = atob(value);
})
