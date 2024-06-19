document.addEventListener('DOMContentLoaded', function() {
    const expenseForm = document.getElementById('expense-form');
    const expenseList = document.getElementById('expense-list');

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    expenseForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const category = document.getElementById('expense-category').value;
        const amount = document.getElementById('expense-amount').value;
        const csrftoken = getCookie('csrftoken');

        fetch(expenseForm.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrftoken
            },
            body: new URLSearchParams({
                'category': category,
                'amount': amount
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const listItem = document.createElement('li');
                listItem.textContent = `${data.category}: $${data.amount}`;
                expenseList.appendChild(listItem);
                expenseForm.reset();
            } else {
                alert('Error adding expense');
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
