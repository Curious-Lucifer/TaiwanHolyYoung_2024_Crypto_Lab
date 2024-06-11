
function xorArrays(arr1, arr2) {
  length = min(arr1.length, arr2.length);

  arr1 = arr1.slice(0, length);
  arr2 = arr2.slice(0, length);

  return arr1.map((num, index) => num ^ arr2[index]);
}

function hexstr2numlist(hexstr) {
  var numlist = [];
  for (let i = 0; i < hexstr.length; i += 2) {
    var num = parseInt(hexstr.slice(i, i + 2), 16);
    numlist.push(num);
  }

  return numlist
    .filter(num => num !== NaN);
}

function numlist2hexstr(numlist) {
  return numlist
    .map(num => num.toString(16).padStart(2, '0'))
    .join('');
}

var message1Input = document.getElementById('message1');
var message2Input = document.getElementById('message2');
var resultInput = document.getElementById('result');

message1Input.addEventListener('input', () => {
  var message1Numlist = hexstr2numlist(message1Input.value);
  var message2Numlist = hexstr2numlist(message2Input.value);

  var resultNumlist = xorArrays(message1Numlist, message2Numlist);
  resultInput.value = numlist2hexstr(resultNumlist);
})

message2Input.addEventListener('input', () => {
  var message1Numlist = hexstr2numlist(message1Input.value);
  var message2Numlist = hexstr2numlist(message2Input.value);

  var resultNumlist = xorArrays(message1Numlist, message2Numlist);
  resultInput.value = numlist2hexstr(resultNumlist);
})

