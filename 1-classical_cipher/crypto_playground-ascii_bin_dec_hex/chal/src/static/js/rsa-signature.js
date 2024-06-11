var p = -1;
var q = -1;
var n = -1;
var phin = -1;
var e = -1;
var d = -1;
var m = -1;
var s = -1;
var mm = -1;

function check() {
  pIsprime = document.getElementById('p-is-prime')
  qIsprime = document.getElementById('q-is-prime')
  pEqualq = document.getElementById('p-equal-q')

  nCorrect = document.getElementById('n-correct')
  phinCorrect = document.getElementById('phin-correct')

  eRangeCheck = document.getElementById('e-range-check')
  eValueCheck = document.getElementById('e-value-check')
  
  dValueCheck = document.getElementById('d-value-check')

  mValueCheck = document.getElementById('m-value-check')

  sValueCheck = document.getElementById('s-value-check')

  mmValueCheck = document.getElementById('mm-value-check')

  if (isPrime(p)) 
    pIsprime.checked = true;
  else
    pIsprime.checked = false;
  if (isPrime(q)) 
    qIsprime.checked = true;
  else
    qIsprime.checked = false;
  if (p !== q)
    pEqualq.checked = true;
  else
    pEqualq.checked = false;

  if (n === p * q)
    nCorrect.checked = true;
  else
    nCorrect.checked = false;
  if (phin === (p - 1) * (q - 1))
    phinCorrect.checked = true;
  else
    phinCorrect.checked = false;

  if ((1 < e) && (e < phin))
    eRangeCheck.checked = true;
  else
    eRangeCheck.checked = false;
  if (gcd(e, phin) === 1) 
    eValueCheck.checked = true;
  else
    eValueCheck.checked = false;

  if (pow(e, -1, phin) === d)
    dValueCheck.checked = true;
  else
    dValueCheck.checked = false;

  if ((0 < m) && (m < n))
    mValueCheck.checked = true;
  else
    mValueCheck.checked = false;

  if ((pow(m, d, n) === s) && (m !== -1))
    sValueCheck.checked = true;
  else
    sValueCheck.checked = false;

  if ((pow(s, e, n) === mm) && (s !== -1))
    mmValueCheck.checked = true;
  else
    mmValueCheck.checked =false;
}

function initStep1() {
  var pInput = document.getElementById('p');
  pInput.addEventListener('input', () => {
    p = parseInt(pInput.value);
    if (isNaN(p)) p = -1;
    check();
  })

  var qInput = document.getElementById('q');
  qInput.addEventListener('input', () => {
    q = parseInt(qInput.value);
    if (isNaN(q)) q = -1;
    check();
  })
}

function initStep2() {
  var nInput = document.getElementById('n');
  nInput.addEventListener('input', () => {
    n = parseInt(nInput.value);
    if (isNaN(n)) n = -1;
    check();
  })

  var phinInput = document.getElementById('phin');
  phinInput.addEventListener('input', () => {
    phin = parseInt(phinInput.value);
    if (isNaN(phin)) phin = -1;
    check();
  })
}

function initStep3() {
  var eInput = document.getElementById('e');
  eInput.addEventListener('input', () => {
    e = parseInt(eInput.value);
    if (isNaN(e)) e = -1;
    check();
  })
}

function initStep4() {
  var dInput = document.getElementById('d');
  dInput.addEventListener('input', () => {
    d = parseInt(dInput.value);
    if (isNaN(d)) d = -1;
    check();
  })
}

function initStep5() {
  var mInput = document.getElementById('m');
  mInput.addEventListener('input', () => {
    m = parseInt(mInput.value);
    if (isNaN(m)) m = -1;
    check();
  })
}

function initStep6() {
  var sInput = document.getElementById('s');
  sInput.addEventListener('input', () => {
    s = parseInt(sInput.value);
    if (isNaN(s)) s = -1;
    check();
  })
}

function initStep7() {
  var mmInput = document.getElementById('mm');
  mmInput.addEventListener('input', () => {
    mm = parseInt(mmInput.value);
    if (isNaN(mm)) mm = -1;
    check();
  })
}

check();
initStep1();
initStep2();
initStep3();
initStep4();
initStep5();
initStep6();
initStep7();


