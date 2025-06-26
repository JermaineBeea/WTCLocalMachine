#!/bin/bash

# Enable debug mode - set to false in production
DEBUG=true

# Get the real script directory regardless of how it's called
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR"

# Configuration
ZIP_PATH="$PROJECT_ROOT/hidden_test_jav.zip"
EXTRACT_DIR="$PROJECT_ROOT/.hidden_test"
TEST_SCRIPT="test_consolidation_hidden.py"

# Function to display colored output
print_color() {
    COLOR_CODE=$1
    MESSAGE=$2
    echo -e "\033[${COLOR_CODE}m${MESSAGE}\033[0m"
}

# Debug print function
debug_print() {
    if [ "$DEBUG" = true ]; then
        echo -e "\033[33mDEBUG: $1\033[0m"
    fi
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

# Print debug information
debug_print "Script Directory: $SCRIPT_DIR"
debug_print "Project Root: $PROJECT_ROOT"
debug_print "Current Working Directory: $(pwd)"
debug_print "Looking for ZIP file at: $ZIP_PATH"

# Check for unzip and install if needed
check_unzip

# Check if zip file exists
if [ ! -f "$ZIP_PATH" ]; then
    print_color "31" "❌ Error: $ZIP_PATH not found."
    debug_print "Looking for .lms directory..."
    if [ -d "$PROJECT_ROOT/.lms" ]; then
        debug_print "Found .lms directory, contents:"
        ls -la "$PROJECT_ROOT/.lms"
    else
        debug_print ".lms directory not found at $PROJECT_ROOT/.lms"
        debug_print "Current directory contents:"
        ls -la "$PROJECT_ROOT"
    fi

    # Try alternate locations
    debug_print "Checking alternate locations..."
    ALT_PATH1="$SCRIPT_DIR/.lms/hidden_test_java.zip"
    ALT_PATH2="./.lms/hidden_test_java.zip"
    ALT_PATH3="$SCRIPT_DIR/.lms/hidden_test_21.zip"

    if [ -f "$ALT_PATH1" ]; then
        debug_print "Found at alternate location: $ALT_PATH1"
        ZIP_PATH="$ALT_PATH1"
        debug_print "Using this path instead"
    elif [ -f "$ALT_PATH2" ]; then
        debug_print "Found at alternate location: $ALT_PATH2"
        ZIP_PATH="$ALT_PATH2"
        debug_print "Using this path instead"
    elif [ -f "$ALT_PATH3" ]; then
        debug_print "Found at alternate location: $ALT_PATH3"
        ZIP_PATH="$ALT_PATH3"
        debug_print "Using this path instead"
    else
        exit 1
    fi
fi

# Clean up any previous test run artifacts BEFORE starting a new test
if [ -d "$EXTRACT_DIR" ]; then
    debug_print "Removing previous extraction directory"
    rm -rf "$EXTRACT_DIR"
fi
if [ -d "$PROJECT_ROOT/target" ]; then
    debug_print "Removing previous Maven target directory"
    rm -rf "$PROJECT_ROOT/target"
fi

debug_print "Creating extraction directory: $EXTRACT_DIR"

# Create extraction directory and unzip
mkdir -p "$EXTRACT_DIR"
debug_print "Extracting ZIP file to: $EXTRACT_DIR"
unzip -o "$ZIP_PATH" -d "$EXTRACT_DIR" > /dev/null
UNZIP_RESULT=$?

# Check if unzip was successful
if [ $UNZIP_RESULT -ne 0 ]; then
    print_color "31" "❌ Error: Failed to extract zip file (exit code $UNZIP_RESULT)."
    debug_print "unzip command failed. Verifying zip file:"
    file "$ZIP_PATH"
    exit 1
fi

# Check if test file exists in extracted directory
TEST_FILE="$EXTRACT_DIR/$TEST_SCRIPT"
debug_print "Looking for test script at: $TEST_FILE"

if [ ! -f "$TEST_FILE" ]; then
    print_color "31" "❌ Error: Hidden test file not found in zip."
    debug_print "Contents of extraction directory:"
    ls -la "$EXTRACT_DIR"
    debug_print "Looking for any Python files:"
    find "$EXTRACT_DIR" -name "*.py" 2>/dev/null

    # If we can't find the expected file, look for any Python file
    FOUND_PY=$(find "$EXTRACT_DIR" -name "*.py" 2>/dev/null | head -1)
    if [ -n "$FOUND_PY" ]; then
        debug_print "Found Python file: $FOUND_PY"
        TEST_FILE="$FOUND_PY"
    else
        exit 1
    fi
fi

# Run the tests
print_color "36" "🧪 Running tests..."
debug_print "Executing: python3 $TEST_FILE"
debug_print "From directory: $(pwd)"

# Change to project root if necessary
cd "$PROJECT_ROOT"
python3 "$TEST_FILE"
TEST_RESULT=$?

debug_print "Test script exited with code: $TEST_RESULT"

# Clean up AFTER tests have run
print_color "36" "🧹 Cleaning up..."
rm -rf "$EXTRACT_DIR"

# Also clean up any Maven target directories that might have been created
if [ -d "$PROJECT_ROOT/target" ]; then
    rm -rf "$PROJECT_ROOT/target"
fi

# Find and clean all .tmp files in the project root
find "$PROJECT_ROOT" -maxdepth 1 -name "*.tmp" -type f -delete

print_color "32" "✅ Done."
exit $TEST_RESULT