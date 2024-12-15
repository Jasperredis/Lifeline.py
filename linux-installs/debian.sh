# NOTE!
# In the packaged release, this would be in the main project directory under the name "install.sh".

echo "Checking if dependencies are installed..."

check_dependency() {
    # Check if the package is installed using dpkg
    if dpkg -l | grep -q "$PACKAGE_NAME"; then
        echo "$PACKAGE_NAME is installed!"
    else
        echo "$PACKAGE_NAME is not installed! It is required for Lifeline.py. Install? (y/N)"
        read -p "> " answer
        answer=$(echo "$answer" | tr '[:upper:]' '[:lower:]')
        if [[ "$answer" == "y" || "$answer" == "yes" ]]; then
            echo "Installing $PACKAGE_NAME..."
            sudo apt-get install -y "$PACKAGE_NAME"
        elif [[ "$answer" == "n" || "$answer" == "no" ]]; then
            echo "Installation of $PACKAGE_NAME cancelled."
        else
            echo "Invalid input."
            exit
        fi
    fi
}

# Call the function with different package names
PACKAGE_NAME="python3"
check_dependency

PACKAGE_NAME="python3-requests"
check_dependency

PACKAGE_NAME="python3-pygame"
check_dependency

PACKAGE_NAME="python3-colorama"
check_dependency

echo "While it is not required, it is recommended to ensure that the Python library, plyer, is installed on your system. Proceed? (y/N)"
read -p "> " answer
answer=$(echo "$answer" | tr '[:upper:]' '[:lower:]')
if [[ "$answer" == "y" || "$answer" == "yes" ]]; then
    echo "Okay!"
elif [[ "$answer" == "n" || "$answer" == "no" ]]; then
    echo "Cancelled."
else
    echo "Invalid input."
    exit
fi

echo "Great! Now run the command in 'run.sh' (or run the file directly) to play Lifeline.py!"
