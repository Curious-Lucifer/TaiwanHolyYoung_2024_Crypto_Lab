
async function sha256(message) {
  const msgBuffer = new TextEncoder().encode(message);
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  return hashHex;
}

hashflag_msg = document.getElementById('hashflag-msg');
hashflag_flag = document.getElementById('hashflag-flag');

hashflag_msg.addEventListener('input', async function() {
  var value =hashflag_msg.value;
  var hashValue = await sha256(value);
  hashflag_flag.value = `FLAG{${hashValue}}`
})
