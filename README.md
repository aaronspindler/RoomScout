# RoomScout


## Setup
1. Download repo
2. Install pip requirements using ``` pip install -r requirements.txt```
3. Setup environment variables
4. Start django local server using ``` python manage.py runserver```

## Environment Variables
    Settings for the application are now loaded from environment variables even in development environment

## Branches
#### Master
    https://roomscout.ca
    Deploys directly to production upon commit
#### Dev
    https://roomscout-dev.herokuapp.com
    Deploys directly to development server

#### All Other
    Any other branch should be a feature branch
    All feature branches should make pull requests into dev and then once approved the dev branch will be merged to master
    
## Testing
#### Forms
#### Views
#### Models