// App State
const state = {
    balance: 0, // in seconds
    activeTimers: {},
    history: [],
    timerIntervals: {}
};

// Activity types
const ACTIVITIES = {
    study: { type: 'earn', label: 'Study', emoji: '📚' },
    practice: { type: 'earn', label: 'Practice', emoji: '🎵' },
    cleaning: { type: 'earn', label: 'Cleaning', emoji: '🧹' },
    tv: { type: 'spend', label: 'TV/Tablet', emoji: '📺' },
    game: { type: 'spend', label: 'Game', emoji: '🎮' }
};

// Initialize app
function init() {
    loadFromLocalStorage();
    updateBalanceDisplay();
    updateHistoryDisplay();
}

// Timer functions
function startTimer(activity) {
    // Don't start if already running
    if (state.activeTimers[activity]) {
        alert(`${ACTIVITIES[activity].label} timer is already running!`);
        return;
    }

    // For spending activities, check if there's enough balance
    if (ACTIVITIES[activity].type === 'spend' && state.balance <= 0) {
        alert('Not enough credits! Earn more credits first.');
        return;
    }

    // Initialize timer
    state.activeTimers[activity] = {
        startTime: Date.now(),
        elapsed: 0
    };

    // Start interval
    state.timerIntervals[activity] = setInterval(() => {
        updateTimerDisplay(activity);
    }, 1000);

    // Update UI
    updateTimerDisplay(activity);
    document.getElementById(`${activity}-timer`).classList.add('active');

    saveToLocalStorage();
}

function stopTimer(activity) {
    if (!state.activeTimers[activity]) {
        return;
    }

    // Calculate elapsed time
    const elapsed = Math.floor((Date.now() - state.activeTimers[activity].startTime) / 1000);

    if (elapsed === 0) {
        alert('Timer was running for less than a second!');
        clearTimer(activity);
        return;
    }

    // Update balance
    if (ACTIVITIES[activity].type === 'earn') {
        state.balance += elapsed;
    } else {
        state.balance -= elapsed;
        if (state.balance < 0) {
            state.balance = 0;
        }
    }

    // Add to history
    state.history.unshift({
        activity: activity,
        duration: elapsed,
        type: ACTIVITIES[activity].type,
        timestamp: Date.now()
    });

    // Clear timer
    clearTimer(activity);

    // Update displays
    updateBalanceDisplay();
    updateHistoryDisplay();
    saveToLocalStorage();
}

function clearTimer(activity) {
    // Clear interval
    if (state.timerIntervals[activity]) {
        clearInterval(state.timerIntervals[activity]);
        delete state.timerIntervals[activity];
    }

    // Remove from active timers
    delete state.activeTimers[activity];

    // Reset display
    document.getElementById(`${activity}-timer`).textContent = '00:00';
    document.getElementById(`${activity}-timer`).classList.remove('active');
}

function updateTimerDisplay(activity) {
    if (!state.activeTimers[activity]) return;

    const elapsed = Math.floor((Date.now() - state.activeTimers[activity].startTime) / 1000);
    const display = formatTime(elapsed);
    document.getElementById(`${activity}-timer`).textContent = display;

    // For spend activities, check if balance is depleted
    if (ACTIVITIES[activity].type === 'spend' && state.balance <= 0) {
        stopTimer(activity);
        alert('Credits depleted! Time to earn more.');
    }
}

// Display functions
function updateBalanceDisplay() {
    const display = formatTime(state.balance);
    document.getElementById('balance').textContent = display;
}

function updateHistoryDisplay() {
    const historyList = document.getElementById('history-list');

    if (state.history.length === 0) {
        historyList.innerHTML = '<p class="no-history">No activities yet. Start earning credits!</p>';
        return;
    }

    historyList.innerHTML = state.history.map(item => {
        const activity = ACTIVITIES[item.activity];
        const sign = item.type === 'earn' ? '+' : '-';
        const date = new Date(item.timestamp);

        return `
            <div class="history-item ${item.type}">
                <div class="history-info">
                    <div class="history-activity">
                        ${activity.emoji} ${activity.label}
                    </div>
                    <div class="history-time">
                        ${date.toLocaleDateString()} ${date.toLocaleTimeString()}
                    </div>
                </div>
                <div class="history-duration ${item.type}">
                    ${sign}${formatTime(item.duration)}
                </div>
            </div>
        `;
    }).join('');
}

function clearHistory() {
    if (confirm('Are you sure you want to clear all history? This cannot be undone.')) {
        state.history = [];
        updateHistoryDisplay();
        saveToLocalStorage();
    }
}

// Utility functions
function formatTime(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;

    if (hours > 0) {
        return `${hours}:${pad(minutes)}:${pad(secs)}`;
    } else {
        return `${minutes}:${pad(secs)}`;
    }
}

function pad(num) {
    return num.toString().padStart(2, '0');
}

// LocalStorage functions
function saveToLocalStorage() {
    try {
        const data = {
            balance: state.balance,
            history: state.history,
            activeTimers: Object.keys(state.activeTimers).map(activity => ({
                activity,
                startTime: state.activeTimers[activity].startTime
            }))
        };
        localStorage.setItem('kidsCredits', JSON.stringify(data));
    } catch (e) {
        console.error('Failed to save to localStorage:', e);
    }
}

function loadFromLocalStorage() {
    try {
        const data = localStorage.getItem('kidsCredits');
        if (data) {
            const parsed = JSON.parse(data);
            state.balance = parsed.balance || 0;
            state.history = parsed.history || [];

            // Restore active timers
            if (parsed.activeTimers && parsed.activeTimers.length > 0) {
                parsed.activeTimers.forEach(timer => {
                    // Check if timer was recently active (within last hour)
                    const timeSinceStart = Date.now() - timer.startTime;
                    if (timeSinceStart < 3600000) { // 1 hour
                        state.activeTimers[timer.activity] = {
                            startTime: timer.startTime,
                            elapsed: 0
                        };
                        startTimer(timer.activity);
                    }
                });
            }
        }
    } catch (e) {
        console.error('Failed to load from localStorage:', e);
    }
}

// Handle page visibility changes
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        saveToLocalStorage();
    } else {
        // Update timers when page becomes visible again
        Object.keys(state.activeTimers).forEach(activity => {
            updateTimerDisplay(activity);
        });
        updateBalanceDisplay();
    }
});

// Save periodically
setInterval(() => {
    if (Object.keys(state.activeTimers).length > 0) {
        saveToLocalStorage();
    }
}, 5000);

// Initialize on load
window.addEventListener('load', init);
