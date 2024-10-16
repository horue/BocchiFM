# BocchiFM

## Overview

BocchiFM is a Python application that integrates with Last.fm to display the currently playing track and artist on Discord using Rich Presence. This project combines two main components: fetching the currently playing music from Last.fm and updating Discord's Rich Presence to reflect that information.

## Components

### 1. Music Fetcher (getfm.py)

This component connects to the Last.fm API to retrieve the user's recent tracks. It checks for the currently playing song and artist and logs any errors encountered during the process. The application will continuously poll the API to ensure it always has the latest information.

-   **Key Features:**
    -   Fetches currently playing track information.
    -   Logs errors related to API requests.

### 2. Discord Rich Presence Updater (rp.py)

This component connects to Discord's Rich Presence API to update the user's status with the currently playing song and artist details. It will display the album art and provide a seamless integration into Discord.

-   **Key Features:**
    -   Connects to Discord and updates Rich Presence with track details.
    -   Clears the status when no music is playing.

### Usage

1.  **Setup**:
    
    -   Ensure you have all the necessary libraries installed. Use the `requirements.txt` file to install the required dependencies.
2.  **Configuration**:
    
    -   Update your Last.fm credentials in the `d.py` file to ensure the application can authenticate and access your account.
3.  **Running the Application**:
    
    -   Start the application by executing the main file, which will continuously fetch the current track and update the Discord status.

### Logging

The application logs errors related to music fetching in a file named `scrobbling_errors.log`. This log helps in diagnosing issues with API calls or network problems.

### License

This project is open-source and available for personal use and modification. Feel free to contribute or suggest enhancements!