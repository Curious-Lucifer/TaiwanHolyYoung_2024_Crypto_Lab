function str2hexstr(str) {
  return Array.from(str)
    .map(char => char.charCodeAt(0).toString(16))
    .join('');
}

function hexstr2str(hexstr) {
  let str = '';
  for (let i = 0; i < hexstr.length; i += 2) {
    str += String.fromCharCode(parseInt(hexstr.substr(i, 2), 16));
  }
  return str;
}

function str2numlist(str) {
  const numlist = Array.from(str).map(char => char.charCodeAt(0));
  return numlist.join(' ');
}

function numlist2str(numlist) {
  const charArray = numlist.split(' ').map(num => String.fromCharCode(parseInt(num)));
  return charArray.join('');
}

function declist2binlist(declist) {
  return declist.split(' ')
    .filter(num => num.trim() !== '')
    .map(num => parseInt(num).toString(2))
    .join(' ');
}

function declist2hexlist(declist) {
  return declist.split(' ')
    .filter(num => num.trim() !== '')
    .map(num => parseInt(num).toString(16))
    .join(' ');
}

function binlist2declist(binlist) {
  return binlist.split(' ')
    .filter(num => num.trim() !== '')
    .map(num => parseInt(num, 2).toString())
    .join(' ');
}

function binlist2hexlist(binlist) {
  return binlist.split(' ')
    .filter(num => num.trim() !== '')
    .map(num => parseInt(num, 2).toString(16))
    .join(' ');
}

function hexlist2binlist(hexlist) {
  return hexlist.split(' ')
    .filter(num => num.trim() !== '')
    .map(num => parseInt(num, 16).toString(2))
    .join(' ');
}

function hexlist2declist(hexlist) {
  return hexlist.split(' ')
    .filter(num => num.trim() !== '')
    .map(num => parseInt(num, 16).toString())
    .join(' ');
}

function min(a, b) {
  return (a < b) ? a : b;
}

function hexstrToWordArray(hexstr) {
  return CryptoJS.enc.Hex.parse(hexstr);
}

function wordArrayToHexstr(wordArray) {
  return CryptoJS.enc.Hex.stringify(wordArray);
}

function aesCbcEncryptBlock(hexIV, hexKey, hexPlainBlock) {
  var IV = hexstrToWordArray(hexIV);
  var key = hexstrToWordArray(hexKey);
  var plainBlock = hexstrToWordArray(hexPlainBlock);
  
  var cipher = CryptoJS.AES.encrypt(plainBlock, key, {
    iv: IV,
    padding: CryptoJS.pad.NoPadding,
    mode: CryptoJS.mode.CBC
  });

  return wordArrayToHexstr(cipher.ciphertext);
}

function aesCbcDecryptBlock(hexIV, hexKey, hexCipherBlock) {
  var IV = hexstrToWordArray(hexIV);
  var key = hexstrToWordArray(hexKey);
  var cipherBlock = hexstrToWordArray(hexCipherBlock);

  var cipherParams = CryptoJS.lib.CipherParams.create({ ciphertext: cipherBlock });

  var plain = CryptoJS.AES.decrypt(cipherParams, key, {
    iv: IV,
    padding: CryptoJS.pad.NoPadding,
    mode: CryptoJS.mode.CBC
  });

  return wordArrayToHexstr(plain);
}

function aesEcbEncrypt(hexPlain, hexKey) {
  var key = CryptoJS.enc.Hex.parse(hexKey);
  var plain = CryptoJS.enc.Hex.parse(hexPlain);
  var cipher = CryptoJS.AES.encrypt(plain, key, { mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.NoPadding });
  return cipher.ciphertext.toString(CryptoJS.enc.Hex);
}

function aesEcbDecrypt(hexCipher, hexKey) {
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
    .filter(num => !isNaN(num));
}

function numlist2hexstr(numlist) {
  return numlist
    .map(num => num.toString(16).padStart(2, '0'))
    .join('');
}

function isPrime(num) {
  if (num <= 1) return false;
  if (num === 2) return true;
  if (num % 2 === 0) return false;
  const sqrt = Math.sqrt(num);
  for (let i = 3; i <= sqrt; i += 2) {
    if (num % i === 0) return false;
  }
  return true;
}

function gcd(a, b) {
  if (b === 0) {
      return a;
  }
  return gcd(b, a % b);
}

function extendedGcd(a, b) {
  if (b === 0) {
    return { gcd: a, x: 1, y: 0 };
  }
  const { gcd, x, y } = extendedGcd(b, ((a % b) + b) % b);
  return { gcd: gcd, x: y, y: x - Math.floor(a / b) * y };
}

function modInverse(a, m) {
  const { gcd, x } = extendedGcd(a, m);
  if (gcd !== 1)
    return NaN;
  else
    return (x % m + m) % m;
}

function pow(base, exp, mod) {
  if (mod === 1) return 0;
  if (mod <= 0) return NaN;

  if (exp < 0) {
    base = modInverse(base, mod);
    if (isNaN(base))
      return NaN;
    exp = -exp;
  }

  var result = 1;
  base = base % mod;
  while (exp > 0) {
    if (exp % 2 === 1)
      result = result * base % mod;

    exp = Math.floor(exp / 2);
    base = base * base % mod;
  }
  return result
}