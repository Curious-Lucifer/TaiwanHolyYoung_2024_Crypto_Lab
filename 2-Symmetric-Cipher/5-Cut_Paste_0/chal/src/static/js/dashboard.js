var liveToast = document.getElementById('liveToast')
const toast = new bootstrap.Toast(liveToast, { autohide: false })

liveToast.querySelector('.btn-close').addEventListener('click', () => {
  toast.hide()
})

document.getElementById('get-flag-btn').addEventListener('click', () => {
  fetch('/get-flag')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network Error')
      }
      return response.json()
    })
    .then(data => {
      if (data['status'] !== 'success') {
        throw new Error(data['msg'])
      }
      return data
    })
    .then(data => {
      document.getElementById('get-flag-result').innerHTML = data['msg']
      toast.show()
    })
    .catch(error => {
      console.error(error)
    })
})
