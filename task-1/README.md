## Installing Git

### Windows:

1. Download the Git installer for Windows from the official Git website: [Git for Windows](https://git-scm.com/download/win)
2. Run the downloaded installer and follow the installation wizard.
3. During the installation, leave the default options unless you have specific preferences.

### Mac:

1. Git is typically pre-installed on macOS. To check if Git is installed, open the Terminal application and run the following command:
   `git --version`
2. If not, install manually using Homebrew `brew install git`

## Configuring User Name and Email

1. Open a terminal or command prompt (on Windows, you can use Git Bash).
2. Set your Git user name using the following command, replacing "Your Name" with your actual name:
   `git config --global user.name "Your Name"`
3. Set your Git email address using the following command, replacing "your.email@example.com" with your actual email address:
   `git config --global user.email "your.email@example.com"`

## Verifying the Configuration

To verify that your user name and email are configured correctly, use the following commands:

1. Check your Git user name:
   `git config --global --list`
2. Check your Git email address:
   `git config --global user.email`

To see all your Git configurations, use the following command:
`git config --global --list`
