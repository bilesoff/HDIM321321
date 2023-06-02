const addToCart = (type, id) => {
    let csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value
    let data = new FormData()
    data.append('type', type)
    data.append('entity', id)
    data.append('csrfmiddlewaretoken', csrf_token)

    fetch('/cart/', {
        method: 'post',
        body: data,
        headers: {'X-CSRFToken': csrf_token}
    })
}

const updatePositionAmount = (type, id, amount, action) => {
    let csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value

    let data = new FormData()
    data.append('action', 'update')
    data.append('type', type)
    data.append('entity', id)
    data.append('csrfmiddlewaretoken', csrf_token)

    if (action == "+")
        data.append('amount', parseInt(amount) + 1)
    else if (action == "-")
        data.append('amount', parseInt(amount) - 1)
    else if (action == "del")
        data.append('amount', 0)

    fetch('/cart/', {
        method: 'post',
        body: data,
        headers: {'X-CSRFToken': csrf_token},
    }).then(() => {
        location.reload()
    })
}