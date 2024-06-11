
function aesEncrypt(hexPlain, hexKey) {
  var key = CryptoJS.enc.Hex.parse(hexKey);
  var plain = CryptoJS.enc.Hex.parse(hexPlain);
  var cipher = CryptoJS.AES.encrypt(plain, key, { mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.NoPadding });
  return cipher.ciphertext.toString(CryptoJS.enc.Hex);
}

function aesDecrypt(hexCipher, hexKey) {
  var key = CryptoJS.enc.Hex.parse(hexKey);
  var cipher = CryptoJS.enc.Hex.parse(hexCipher)
  var cipherParams = CryptoJS.lib.CipherParams.create({ ciphertext: cipher });
  var plain = CryptoJS.AES.decrypt(cipherParams, key, { 
    mode: CryptoJS.mode.ECB, 
    padding: CryptoJS.pad.NoPadding 
  });
  return plain.toString(CryptoJS.enc.Hex);
}

function generateRandomHex(length) {
  var result = '';
  var characters = '0123456789abcdef';
  var charactersLength = characters.length;
  for (var i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

var encryptPlain = document.getElementById('encrypt-plain');
var encryptKey = document.getElementById('encrypt-key');
var encryptCipher = document.getElementById('encrypt-cipher');

encryptPlain.addEventListener('input', () => {
  var hexPlain = encryptPlain.value;
  var hexKey = encryptKey.value;
  var correctKeyLength = [16 * 2, 24 * 2, 32 * 2];

  if ((hexPlain.length === 32) && correctKeyLength.includes(hexKey.length)) {
    encryptCipher.value = aesEncrypt(hexPlain, hexKey);
  } else {
    encryptCipher.value = '';
  }
})

encryptKey.addEventListener('input', () => {
  var hexPlain = encryptPlain.value;
  var hexKey = encryptKey.value;
  var correctKeyLength = [16 * 2, 24 * 2, 32 * 2];

  if ((hexPlain.length === 32) && correctKeyLength.includes(hexKey.length)) {
    encryptCipher.value = aesEncrypt(hexPlain, hexKey);
  } else {
    encryptCipher.value = '';
  }
})

document.getElementById('auto-generate-encrypt-key-btn').addEventListener('click', () => {
  encryptKey.value = generateRandomHex(32);
  encryptKey.dispatchEvent(new Event('input', { bubbles: true, cancelable: true }));
})



var decryptCipher = document.getElementById('decrypt-cipher');
var decryptKey = document.getElementById('decrypt-key');
var decryptPlain = document.getElementById('decrypt-plain');

decryptCipher.addEventListener('input', () => {
  var hexCipher = decryptCipher.value;
  var hexKey = decryptKey.value;
  var correctKeyLength = [16 * 2, 24 * 2, 32 * 2];

  if ((hexCipher.length === 32) && correctKeyLength.includes(hexKey.length)) {
    decryptPlain.value = aesDecrypt(hexCipher, hexKey);
  } else {
    decryptPlain.value = '';
  }
})

decryptKey.addEventListener('input', () => {
  var hexCipher = decryptCipher.value;
  var hexKey = decryptKey.value;
  var correctKeyLength = [16 * 2, 24 * 2, 32 * 2];

  if ((hexCipher.length === 32) && correctKeyLength.includes(hexKey.length)) {
    decryptPlain.value = aesDecrypt(hexCipher, hexKey);
  } else {
    decryptPlain.value = '';
  }
})

document.getElementById('auto-generate-decrypt-key-btn').addEventListener('click', () => {
  decryptKey.value = generateRandomHex(32);
  decryptKey.dispatchEvent(new Event('input', { bubbles: true, cancelable: true }));
})