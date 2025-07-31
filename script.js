document.addEventListener('DOMContentLoaded', () => {
    const screens = document.querySelectorAll('.screen');
    const buttons = document.querySelectorAll('button[data-target]');
    const screenContainer = document.getElementById('screen-container');

    function showScreen(screenId) {
        screens.forEach(screen => {
            screen.classList.remove('active');
        });

        const targetScreen = document.getElementById(screenId);
        if (targetScreen) {
            // A small delay to allow fade-out animation if any was added
            setTimeout(() => {
                targetScreen.classList.add('active');
            }, 50); // Keep it short
        }
    }

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const targetScreenId = button.getAttribute('data-target');
            showScreen(targetScreenId);
        });
    });

    // Initialize with the first screen
    showScreen('screen-welcome');
});

