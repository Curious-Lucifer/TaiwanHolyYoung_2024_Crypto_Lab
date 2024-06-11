
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

function isHexKeyValid(hexKey) {
  var correctKeyLength = [16 * 2, 24 * 2, 32 * 2];
  return correctKeyLength.includes(hexKey.length);
}

var encryptKey = document.getElementById('encrypt-key');
var encryptPlains = [
  ...document.querySelectorAll('.aes-encrypt-container .plain-container input'), 
  ...document.querySelectorAll('.aes-encrypt-nokey-container .plain-container input')
];
var encryptCiphers = [
  ...document.querySelectorAll('.aes-encrypt-container .cipher-container input'), 
  ...document.querySelectorAll('.aes-encrypt-nokey-container .cipher-container input')
]

encryptPlains.forEach((encryptPlain, index) => {
  encryptPlain.addEventListener('input', () => {
    var hexPlain = encryptPlain.value;
    var hexKey = encryptKey.value;
    
    if ((hexPlain.length === 32) && isHexKeyValid(hexKey)) {
      encryptCiphers[index].value = aesEncrypt(hexPlain, hexKey);
    } else {
      encryptCiphers[index].value = '';
    }
  })
})

encryptKey.addEventListener('input', () => {
  var hexKey = encryptKey.value;

  if (isHexKeyValid(hexKey)) {
    encryptPlains.forEach((encryptPlain, index) => {
      var hexPlain = encryptPlain.value;

      if (hexPlain.length === 32) {
        encryptCiphers[index].value = aesEncrypt(hexPlain, hexKey);
      } else {
        encryptCiphers[index].value = '';
      }
    })
  } else {
    encryptCiphers.forEach(encryptCipher => {
      encryptCipher.value = '';
    })
  }
})

document.getElementById('auto-generate-encrypt-key-btn').addEventListener('click', () => {
  encryptKey.value = generateRandomHex(32);
  encryptKey.dispatchEvent(new Event('input', { bubbles: true, cancelable: true }));
})


var decryptKey = document.getElementById('decrypt-key');
var decryptCiphers = [
  ...document.querySelectorAll('.aes-decrypt-container .cipher-container input'), 
  ...document.querySelectorAll('.aes-decrypt-nokey-container .cipher-container input')
];
var decryptPlains = [
  ...document.querySelectorAll('.aes-decrypt-container .plain-container input'), 
  ...document.querySelectorAll('.aes-decrypt-nokey-container .plain-container input')
]

decryptCiphers.forEach((decryptCipher, index) => {
  decryptCipher.addEventListener('input', () => {
    var hexCipher = decryptCipher.value;
    var hexKey = decryptKey.value;
    
    if ((hexCipher.length === 32) && isHexKeyValid(hexKey)) {
      decryptPlains[index].value = aesDecrypt(hexCipher, hexKey);
    } else {
      decryptPlains[index].value = '';
    }
  })
})

decryptKey.addEventListener('input', () => {
  var hexKey = decryptKey.value;

  if (isHexKeyValid(hexKey)) {
    decryptCiphers.forEach((decryptCipher, index) => {
      var hexCipher = decryptCipher.value;

      if (hexCipher.length === 32) {
        decryptPlains[index].value = aesDecrypt(hexCipher, hexKey);
      } else {
        decryptPlains[index].value = '';
      }
    })
  } else {
    decryptCiphers.forEach(decryptCipher => {
      decryptCipher.value = '';
    })
  }
})

document.getElementById('auto-generate-decrypt-key-btn').addEventListener('click', () => {
  decryptKey.value = generateRandomHex(32);
  decryptKey.dispatchEvent(new Event('input', { bubbles: true, cancelable: true }));
})





