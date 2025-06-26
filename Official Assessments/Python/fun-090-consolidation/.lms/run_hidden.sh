#!/bin/bash

# Configuration
ZIP_PATH=".lms/hidden_test_consolidation.zip"
EXTRACT_DIR=".hidden_test_consolidation"

# Function to display colored output
print_color() {
    COLOR_CODE=$1
    MESSAGE=$2
    echo -e "\033[${COLOR_CODE}m${MESSAGE}\033[0m"
}

# Function to check and install unzip if needed
check_unzip() {
    if ! command -v unzip &> /dev/null; then
        print_color "33" "📦 unzip not found. Installing..."
        
        # Try apt-get (Debian/Ubuntu)
        if command -v apt-get &> /dev/null; then
            sudo apt-get update -qq
            sudo apt-get install -y unzip
        # Try yum (Red Hat/CentOS)
        elif command -v yum &> /dev/null; then
            sudo yum install -y unzip
        # Try brew (macOS)
        elif command -v brew &> /dev/null; then
            brew install unzip
        # Try pacman (Arch Linux)
        elif command -v pacman &> /dev/null; then
            sudo pacman -S --noconfirm unzip
        else
            print_color "31" "❌ Unable to install unzip automatically. Please install it manually."
            exit 1
        fi
        
        # Verify installation
        if ! command -v unzip &> /dev/null; then
            print_color "31" "❌ Failed to install unzip. Please install it manually."
            exit 1
        fi
        
        print_color "32" "✅ unzip installed successfully."
    fi
}

# Main execution starts here
print_color "36" "🚀 Running hidden tests..."

# Check for unzip and install if needed
check_unzip

# Check if zip file exists
if [ ! -f "$ZIP_PATH" ]; then
  print_color "31" "❌ Error: $ZIP_PATH not found."
  exit 1
fi

# Create extraction directory and unzip
mkdir -p "$EXTRACT_DIR"
unzip -o "$ZIP_PATH" -d "$EXTRACT_DIR" > /dev/null

# Check if test file exists in extracted directory
TEST_FILE="$EXTRACT_DIR/test_consolidation.py"
if [ ! -f "$TEST_FILE" ]; then
  print_color "31" "❌ Error: Hidden test file not found in zip."
  exit 1
fi

# Run the tests
print_color "36" "🧪 Running tests..."
python3 "$TEST_FILE"

# Clean up
print_color "36" "🧹 Cleaning up..."
rm -rf "$EXTRACT_DIR"

print_color "32" "✅ Done."