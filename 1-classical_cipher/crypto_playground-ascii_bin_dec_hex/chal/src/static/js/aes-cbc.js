
var autoGenerateContianers = document.querySelectorAll('.auto-generate-container');

autoGenerateContianers.forEach((autoGenerateContianer) => {
  autoGenerateContianer.querySelector('button').addEventListener('click', (e) => {
    autoGenerateContianer.querySelector('input').value = generateRandomHex(32);
    autoGenerateContianer.querySelector('input').dispatchEvent(new Event('input', { bubbles: true, cancelable: true }));
  })
});

function initEncrypt() {
  var keyInput = document.getElementById('encrypt-key');
  var ivInput = document.getElementById('encrypt-iv');
  var plainInputs = document.querySelectorAll('.aes-cbc-encrypt-container .plain-container input');
  var xorPlainInputs = document.querySelectorAll('.aes-cbc-encrypt-container .xor-plain-container input');
  var cipherInputs = document.querySelectorAll('.aes-cbc-encrypt-container .cipher-container input');

  function updateEncrypt(index) {
    var hexPlain = plainInputs[index].value;
    var hexIV = ivInput.value;
    var hexKey = keyInput.value;

    if (index === 0) {
      var hexIV = ivInput.value;
    } else {
      var hexIV = cipherInputs[index - 1].value;
    }

    if ((hexPlain.length === 32) && (hexIV.length === 32) && isHexKeyValid(hexKey)) {
      cipherInputs[index].value = aesCbcEncryptBlock(hexIV, hexKey, hexPlain);
    } else {
      cipherInputs[index].value = '';
    }

    if ((hexPlain.length === 32) && (hexIV.length === 32)) {
      xorPlainInputs[index].value = numlist2hexstr(xorArrays(
        hexstr2numlist(hexPlain), 
        hexstr2numlist(hexIV)
      ));
    } else {
      xorPlainInputs[index].value = '';
    }
  }

  plainInputs.forEach((plainInput, index) => {
    plainInput.addEventListener('input', () => {
      updateEncrypt(index);
    })
  })

  keyInput.addEventListener('input', () => {
    plainInputs.forEach((plainInput, index) => {
      updateEncrypt(index);
    })
  })

  ivInput.addEventListener('input', () => {
    plainInputs.forEach((plainInput, index) => {
      updateEncrypt(index);
    })
  })
}

function initDecrypt() {
  var keyInput = document.getElementById('decrypt-key');
  var ivInput = document.getElementById('decrypt-iv');
  var cipherInputs = document.querySelectorAll('.aes-cbc-decrypt-container .cipher-container input');
  var xorPlainInputs = document.querySelectorAll('.aes-cbc-decrypt-container .xor-plain-container input');
  var plainInputs = document.querySelectorAll('.aes-cbc-decrypt-container .plain-container input');

  function updateDecrypt(index) {
    var hexCipher = cipherInputs[index].value;
    var hexIV = ivInput.value;
    var hexKey = keyInput.value;

    if (index === 0) {
      var hexIV = ivInput.value;
    } else {
      var hexIV = cipherInputs[index - 1].value;
    }

    if ((hexCipher.length === 32) && (hexIV.length === 32) && isHexKeyValid(hexKey)) {
      plainInputs[index].value = aesCbcDecryptBlock(hexIV, hexKey, hexCipher);
    } else {
      plainInputs[index].value = '';
    }

    if ((hexCipher.length === 32) && isHexKeyValid(hexKey)) {
      xorPlainInputs[index].value = aesEcbDecrypt(hexCipher, hexKey);
    } else {
      xorPlainInputs[index].value = '';
    }
  }

  cipherInputs.forEach((cipherInput, index) => {
    cipherInput.addEventListener('input', () => {
      updateDecrypt(index);
    })
  })

  keyInput.addEventListener('input', () => {
    cipherInputs.forEach((cipherInput, index) => {
      updateDecrypt(index);
    })
  })

  ivInput.addEventListener('input', () => {
    cipherInputs.forEach((cipherInput, index) => {
      updateDecrypt(index);
    })
  })
}

initEncrypt();
initDecrypt();

