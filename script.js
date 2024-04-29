document.addEventListener('DOMContentLoaded', function () {
    const startBtn = document.getElementById('start-btn');

    startBtn.addEventListener('click', function () {
        startBtn.style.display = 'none'; // Hide button after clicking
        // Activate Jarvis functionality
        activateJarvis();
    });

    function activateJarvis() {
        // Placeholder for sending request to Flask server to activate Jarvis
        fetch('/activate_jarvis', {
            method: 'POST'
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            console.log('Jarvis activated! Listening for voice input...');
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    }
});