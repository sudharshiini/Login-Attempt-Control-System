# Login Attempt Control System

## VirtualWorks Cyber Security Internship – Task 5

### Project Description
A Python-based login authentication demonstration that temporarily restricts access after repeated incorrect login attempts.

### Features
- Username and password verification
- Maximum of 3 failed login attempts
- Automatic account lockout for 30 seconds
- Login access restored after the lockout period
- Successful login resets the failed-attempt counter
- Password input hidden using `getpass`
- Password hash comparison using `hmac.compare_digest`

### Technologies Used
- Python 3
- hashlib
- hmac
- time
- getpass
- Visual Studio Code

### How to Run

Open the project folder in VS Code and execute:

`python login_control.py`

### Demo Credentials

Username: `admin`

Password: `Admin@123`

These credentials are for demonstration purposes only.

### Testing

**Test 1 – Failed Login**

Enter an incorrect password three times.

Expected: Account locked for 30 seconds.

**Test 2 – Account Lockout**

Attempt another login before the lockout expires.

Expected: Login temporarily blocked.

**Test 3 – Successful Login**

Wait until the lockout expires and enter the correct credentials.

Expected: Login successful.

### Screenshots

Test evidence is available in the `screenshots` folder.

### Limitations

This is an educational demonstration, not a production authentication system. The account lockout is stored only in memory and resets when the program restarts. The fixed SHA-256 password hash is not suitable for real password storage. Production systems require secure password hashing, persistent lockout controls, and additional authentication safeguards.

### Internship Details

VirtualWorks Cyber Security Internship

Task ID: task5