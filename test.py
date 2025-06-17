# git_commands.py

def print_git_commands():
    """
    Prints a list of important Git commands with brief explanations, without numbering.
    """
    print("---------------------------------------")
    print("  Important Git Commands Cheat Sheet   ")
    print("---------------------------------------")
    print("\n")

    print("git init")
    print("    Description: Initializes a new Git repository in the current directory.")
    print("    Usage: git init")
    print("\n")

    print("git clone [repository_url]")
    print("    Description: Clones an existing repository from a URL.")
    print("    Usage: git clone https://github.com/user/repo.git")
    print("\n")

    print("git add [file(s)] / git add .")
    print("    Description: Adds changes to the staging area for the next commit.")
    print("    Usage: git add index.html (to add a specific file)")
    print("    Usage: git add . (to add all changes in the current directory)")
    print("\n")

    print("git commit -m \"[commit_message]\"")
    print("    Description: Records the staged changes to the repository with a message.")
    print("    Usage: git commit -m \"Initial commit of the project\"")
    print("\n")

    print("git push [remote_name] [branch_name]")
    print("    Description: Uploads local branch commits to the remote repository.")
    print("    Usage: git push origin main")
    print("\n")

    print("git pull [remote_name] [branch_name]")
    print("    Description: Fetches and integrates changes from the remote repository to the current branch.")
    print("    Usage: git pull origin main")
    print("\n")

    print("git branch")
    print("    Description: Lists, creates, or deletes branches.")
    print("    Usage: git branch (to list branches)")
    print("    Usage: git branch new-feature (to create a new branch)")
    print("    Usage: git branch -d old-branch (to delete a branch)")
    print("\n")

    print("git merge [branch_name]")
    print("    Description: Integrates changes from one branch into the current branch.")
    print("    Usage: git merge feature-branch")
    print("\n")

    print("git diff")
    print("    Description: Shows changes between commits, commit and working tree, etc.")
    print("    Usage: git diff (to see unstaged changes)")
    print("    Usage: git diff --staged (to see staged changes)")
    print("\n")

if __name__ == "__main__":
    print_git_commands()