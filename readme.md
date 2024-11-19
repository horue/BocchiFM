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

## Setup and Configuration

### 1. **Configuration Files**

Before running the application, you need to create two configuration files for authentication and application setup.

-   **`pref.bcc`**: This file contains your Last.fm credentials.
    
    Create the file `pref.bcc` with the following content:
    
    `[user]
    u = your_lastfm_username
    k = your_lastfm_api_key` 
    
    Replace `your_lastfm_username` with your Last.fm username, and `your_lastfm_api_key` with your Last.fm API key. You can get your API key by registering your application on Last.fm's developer portal.
    
-   **`c_id`**: This file contains the Discord application ID used for Rich Presence.
    
    Create the file `c_id` with the following content:
    
    `c_id = 'your_discord_application_id'` 
    
    Replace `your_discord_application_id` with the ID of your Discord application. You can get this ID from the Discord Developer Portal.
    

### 2. **Create and Configure Batch (`.bat`) and VBS (`.vbs`) Files**

To ensure the application runs properly in the background and starts automatically with the correct environment, you need to create two additional files: a batch file (`.bat`) and a Visual Basic Script (`.vbs`).

-   **Batch File (`BocchiFM.bat`)**
    
    The `.bat` file will be used to activate your virtual environment and run the Python script that starts the application.
    
    Create a file named `BocchiFM.bat` with the following content:
    
    
    ``@echo off
    cd "C:\path\to\BocchiFM"  REM <-- Change this to the folder where your `tray.py` is located
    call "C:\path\to\BocchiFM\.venv\Scripts\activate"  REM <-- Change to the path of your virtual environment's `activate` script
    pythonw tray.py`` 
    
    -   **Explanation**:
        -   The `cd` command navigates to the folder where your `BocchiFM` project is located. Replace `C:\path\to\BocchiFM` with the actual path to your project folder.
        -   The `call` command activates the virtual environment. Make sure the path points to your virtual environment's `Scripts\activate` file. If your virtual environment is named `.venv`, the path will be `C:\path\to\BocchiFM\.venv\Scripts\activate`.
        -   The `pythonw` command ensures that the application runs without opening a command window.
-   **Visual Basic Script (`start_bocchifm.vbs`)**
    
    The `.vbs` script will execute the batch file silently in the background.
    
    Create a Visual Basic Script file named `start_bocchifm.vbs` with the following content:
    
    `Set WshShell = CreateObject("WScript.Shell")
    WshShell.Run """C:\path\to\BocchiFM\BocchiFM.bat""", 0, False` 
    
    -   **Explanation**:
        -   This script runs the batch file (`BocchiFM.bat`) without opening a command window. Replace `C:\path\to\BocchiFM` with the actual path to the folder where the `BocchiFM.bat` file is located.
        -   The `0` parameter ensures that the batch file runs in the background (no visible window).
        -   The `False` parameter allows the script to run asynchronously, so it doesn't wait for the batch file to finish.

### 3. **Install Dependencies**

Ensure you have all the necessary libraries installed by using the `requirements.txt` file. You can install them with the following command:

`pip install -r requirements.txt` 

### 4. **Running the Application**

Once you have configured the files and installed the dependencies, you can start the application by double-clicking the `start_bocchifm.vbs` file. This will:

-   Activate the virtual environment.
-   Run the application in the background, updating your Discord status with the currently playing track.

### Logging

The application logs errors related to music fetching in a file named `scrobbling_errors.log`. This log helps in diagnosing issues with API calls or network problems.