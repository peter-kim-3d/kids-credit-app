# Kids Credit Tracker

A simple and fun web app to help kids track time credits earned through activities like studying, practicing, and cleaning, and spend them on entertainment like TV and games.

## Features

- **Earn Credits**: Track time spent on productive activities
  - 📚 Study
  - 🎵 Practice
  - 🧹 Cleaning

- **Spend Credits**: Use earned credits for fun activities
  - 📺 TV/Tablet
  - 🎮 Games

- **Automatic Tracking**: Built-in timers for each activity
- **Balance Display**: See your current credit balance at a glance
- **Activity History**: View all past activities with timestamps
- **Auto-Save**: All data is saved automatically to your browser

## How to Use

### Getting Started

1. Open `index.html` in your web browser
2. You'll see your credit balance at the top (starts at 0:00)

### Earning Credits

1. Choose an activity (Study, Practice, or Cleaning)
2. Click the **Start** button to begin the timer
3. Do your activity!
4. Click the **Stop** button when done
5. Your credits will be added to your balance automatically

### Spending Credits

1. Choose an activity (TV/Tablet or Game)
2. Click the **Start** button
3. Enjoy your earned screen time!
4. Click the **Stop** button when done
5. Your credits will be deducted from your balance

### Important Notes

- You need to have credits in your balance before you can spend them
- All data is saved automatically in your browser
- If you close the browser and come back, your balance and history will still be there
- Click "Clear History" to remove all past activities (balance remains unchanged)

## Technical Details

### Files

- `index.html` - Main app structure
- `style.css` - Styling and design
- `app.js` - Timer logic and credit management

### Technologies Used

- HTML5
- CSS3
- Vanilla JavaScript
- LocalStorage for data persistence

### Browser Compatibility

Works in all modern browsers:
- Chrome
- Firefox
- Safari
- Edge

## Tips for Parents

1. **Set Goals**: Help your kids understand how much time they need to earn for their desired activities
2. **Fair Exchange**: Consider a 1:1 ratio (1 minute earned = 1 minute spent) or adjust based on your preferences
3. **Regular Review**: Check the activity history together to discuss time management
4. **Reset Option**: You can clear the browser's local storage to start fresh if needed

## Customization

To modify activities or add new ones, edit the `ACTIVITIES` object in `app.js`:

```javascript
const ACTIVITIES = {
    study: { type: 'earn', label: 'Study', emoji: '📚' },
    // Add your custom activities here
};
```

## Privacy

All data is stored locally in your browser. No information is sent to any server.

## License

Free to use and modify for personal use.
