
asciiDecimal_ascii = document.getElementById('asciiDecimal-ascii');
asciiDecimal_decimal = document.getElementById('asciiDecimal-decimal');

asciiDecimal_ascii.addEventListener('input', () => {
  var value = asciiDecimal_ascii.value;
  asciiDecimal_decimal.value = str2numlist(value);
})

asciiDecimal_decimal.addEventListener('input', () => {
  var value = asciiDecimal_decimal.value;
  asciiDecimal_ascii.value = numlist2str(value);
})


binDecHex_dec = document.getElementById('binDecHex-dec');
binDecHex_bin = document.getElementById('binDecHex-bin');
binDecHex_hex = document.getElementById('binDecHex-hex');

binDecHex_dec.addEventListener('input', () => {
  var value = binDecHex_dec.value;
  binDecHex_bin.value = declist2binlist(value);
  binDecHex_hex.value = declist2hexlist(value);
})

binDecHex_bin.addEventListener('input', () => {
  var value = binDecHex_bin.value;
  binDecHex_dec.value = binlist2declist(value);
  binDecHex_hex.value = binlist2hexlist(value);
})

binDecHex_hex.addEventListener('input', () => {
  var value = binDecHex_hex.value;
  binDecHex_bin.value = hexlist2binlist(value);
  binDecHex_dec.value = hexlist2declist(value);
})

