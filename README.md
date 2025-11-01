# Kids Credit Tracker

A Python/Streamlit web app to help kids track time credits earned through activities like studying, practicing, and cleaning, and spend them on entertainment like TV and games.

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
- **Auto-Save**: All data is saved automatically to a JSON file
- **Auto-Refresh**: Timers update in real-time

## How to Use

### Earning Credits

1. Choose an activity (Study, Practice, or Cleaning)
2. Click the **▶️ Start** button to begin the timer
3. Do your activity!
4. Click the **⏹️ Stop** button when done
5. Your credits will be added to your balance automatically

### Spending Credits

1. Choose an activity (TV/Tablet or Game)
2. Click the **▶️ Start** button
3. Enjoy your earned screen time!
4. Click the **⏹️ Stop** button when done
5. Your credits will be deducted from your balance

### Important Notes

- You need to have credits in your balance before you can spend them
- All data is saved automatically to `credit_data.json`
- Active timers update every second automatically
- Click "🗑️ Clear History" to remove all past activities (balance remains unchanged)

## Running Locally

### Requirements

- Python 3.7 or higher

### Installation

1. Clone this repository or download the files
2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Deploy to Streamlit Cloud (FREE)

Deploy this app for free so kids can access it from anywhere on the internet!

### Step-by-Step Deployment

1. **Push your code to GitHub**
   - Make sure your repository is public or you have Streamlit Cloud access to private repos

2. **Go to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

3. **Deploy the App**
   - Click "New app"
   - Select your repository: `peter-kim-3d/kids-credit-app`
   - Branch: `claude/kids-credit-system-011CUeQ6e6aoCoCJQBKKfUsg` (or your main branch)
   - Main file path: `app.py`
   - Click "Deploy"!

4. **Share the URL**
   - Once deployed, you'll get a URL like: `https://your-app-name.streamlit.app`
   - Kids can access it from any device with internet!

### Deployment Notes

- Streamlit Cloud is **completely free** for public apps
- The app will auto-save data to `credit_data.json`
- Data persists between sessions
- The app auto-refreshes when timers are running

## Technical Details

### Files

- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `credit_data.json` - Auto-generated data storage (not in git)
- `.gitignore` - Excludes data file from version control

### Technologies Used

- Python 3.7+
- Streamlit - Web app framework
- JSON - Data persistence

### Data Storage

- All data stored in `credit_data.json` locally
- Includes: balance, history, and active timers
- Auto-saves after every action

## Tips for Parents

1. **Set Goals**: Help your kids understand how much time they need to earn for their desired activities
2. **Fair Exchange**: The app uses a 1:1 ratio (1 second earned = 1 second spent)
3. **Regular Review**: Check the activity history together to discuss time management
4. **Multi-Device**: Once deployed to Streamlit Cloud, accessible from any device

## Customization

To add new activities, edit the `ACTIVITIES` dictionary in `app.py`:

```python
ACTIVITIES = {
    'study': {'type': 'earn', 'label': 'Study', 'emoji': '📚'},
    'homework': {'type': 'earn', 'label': 'Homework', 'emoji': '✏️'},  # Add new activity
    # Add more activities here
}
```

## Privacy

- Data is stored locally in `credit_data.json`
- When deployed, each deployment has its own data storage
- No personal information is collected or transmitted

## Troubleshooting

**Timers not updating?**
- The app auto-refreshes every second when a timer is active
- If it seems stuck, refresh the page

**Lost data?**
- Check if `credit_data.json` exists
- Data is saved after every Start/Stop action

**Can't start spending timer?**
- Make sure you have credits in your balance
- Earn credits first by doing productive activities

## License

Free to use and modify for personal use.
