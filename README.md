# ScrappyTwitch

ScrappyTwitch is a Python application that acts as a Twitch bot, gathering information about online streamers and storing it in a database.

![ScrappyTwitch Logo](https://iili.io/J0XQgFj.jpg)

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python (>=3.12)
- Poetry
- Twitch API Client ID and Secret
- MongoDB

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/dbatalha/ScrappyTwitch.git
    cd ScrappyTwitch
    ```

2. Install project dependencies using Poetry:

    ```bash
    poetry install
    ```

## Configuration

1. Obtain Twitch API credentials:

   - Register a new application on the [Twitch Developer Portal](https://dev.twitch.tv/console/apps).
   - Note the Client ID and Client Secret.

2. Configure the application:

   - Edit the file "scrappy_bot/resources/config.ini"":
   - Replace the {CLIENT_ID} with your application key and secret;

    ```config.ini
    [Twitch]
    client_id = {CLIENT_ID}
    client_secret = {CLIENT_SECRET}
    grant_type = client_credentials

    [Database]
    mongodb_connection = {CONNECTION}
   ```

## Usage

Run the ScrappyTwitch application:

```bash
python start.py