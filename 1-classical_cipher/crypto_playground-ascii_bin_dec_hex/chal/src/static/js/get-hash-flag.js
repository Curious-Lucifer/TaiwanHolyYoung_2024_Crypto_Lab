
hashflag_msg = document.getElementById('hashflag-msg');
hashflag_flag = document.getElementById('hashflag-flag');

hashflag_msg.addEventListener('input', () => {
  var value = hashflag_msg.value;

  fetch('/calc-sha256', {
    method: 'POST', 
    headers: { 'Content-Type': 'application/json' }, 
    body: JSON.stringify({ msg: value })
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network Error');
    }
    return response.json();
  })
  .then(data => {
    if (data['status'] !== 'success') {
      throw new Error(data['msg']);
    }
    return data;
  })
  .then(data => {
    hashflag_flag.value = `FLAG{${data['msg']}}`
  })
  .catch(error => {
    console.error('Get Flag Error : ', error);
  });
})
