## Forking and Cloning a Repository

1. Go to the original repository on GitHub that you want to fork.

2. Click the "Fork" button on the top right corner of the repository page.

3. You have now forked the repository, creating a personal copy under your GitHub account.

4. To clone the forked repository to your local machine, open a terminal or command prompt.

5. Navigate to the directory where you want to clone the repository.

6. Copy the URL of your forked repository from the "Clone or download" button on the repository page.

7. Run the following command to clone the repository:
   `git clone <repository-url>`
   Replace `<repository-url>` with the URL you copied.

## Modifying and Pushing Changes

1. Navigate to the cloned repository directory using the terminal or command prompt.

2. Open the file you want to modify in a text editor.

3. Make the desired changes to the file.

4. Save the file and close the text editor.

5. Run the following commands to commit and push the changes to the remote repository:

```
git add <modified-file>
git commit -m "Modify the file with descriptive commit message"
git push origin <branch-name>
```

Replace `<modified-file>` with the name of the file you modified, and `<branch-name>` with the branch you want to push the changes to (usually "main" or "master").

## Verify Changes on GitHub

1. Go to your forked repository on GitHub.

2. You should see your changes reflected in the file you modified.
