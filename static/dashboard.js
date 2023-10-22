function updateAssetState() {
  fetch('/asset_state')
    .then(response => response.json())
    .then(data => {
      const assetStateElement = document.getElementById('asset-state');
      assetStateElement.innerText = data.state;
      assetStateElement.style.color = data.color;
    })
    .catch((error) => {
      console.error('Error fetching asset state:', error);
    });
}

// Fetch the asset state every 5 seconds
setInterval(updateAssetState, 5000);
