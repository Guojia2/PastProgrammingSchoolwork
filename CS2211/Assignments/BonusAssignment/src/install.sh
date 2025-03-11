#!/bin/bash

# Step 1: Build the program using make
echo "Building the program..."
make

# Step 2: Create the installation directory if it doesn't exist
INSTALL_DIR="$HOME/.local/bin"
if [ ! -d "$INSTALL_DIR" ]; then
    echo "Creating installation directory: $INSTALL_DIR"
    mkdir -p "$INSTALL_DIR"
fi

# Step 3: Copy the executable to the installation directory
echo "Copying gcal to $INSTALL_DIR..."
cp gcal "$INSTALL_DIR"

# Step 4: Update the $PATH variable in .bashrc
echo "Updating .bashrc to include $INSTALL_DIR in PATH..."
echo "export PATH=\$HOME/.local/bin:\$PATH" >> "$HOME/.bashrc"

# Final step: Inform the user their installationcomplete
echo "Installation complete."
