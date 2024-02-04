// Assuming your input element has an id of "stockSymbol"
function fetchStockPrice() {
    const symbol = document.getElementById('stockSymbol').value;
    fetch(`/price/${symbol}`)
    .then(response => response.json())
    .then(data => {
        if(data.error) {
            document.getElementById('stockPrice').innerText = 'Error: ' + data.error;
        } else {
            document.getElementById('stockPrice').innerText = 'Price: ' + data.price;
        }
    })
    .catch(error => {
        document.getElementById('stockPrice').innerText = 'Failed to fetch stock price.';
    });
}

// Make sure this function is called when the button is clicked.
