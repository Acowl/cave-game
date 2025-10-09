#!/bin/bash
# Quick snapshot capture script for Linux/Mac

echo "========================================"
echo "SHABUYA Cave Adventure"
echo "Snapshot Capture Tool"
echo "========================================"
echo ""

while true; do
    echo "Select an option:"
    echo ""
    echo "1. Generate snapshots (Warrior only - FAST)"
    echo "2. Generate snapshots (All classes - COMPLETE)"
    echo "3. Analyze existing snapshots"
    echo "4. View snapshot report"
    echo "5. Exit"
    echo ""
    
    read -p "Enter your choice (1-5): " choice
    
    case $choice in
        1)
            echo ""
            echo "Generating snapshots (Warrior only)..."
            python3 utilities/capture_player_gui_snapshots.py
            echo ""
            echo "Done! Snapshots saved to: player_gui_snapshots/"
            read -p "Press Enter to continue..."
            ;;
        2)
            echo ""
            echo "Generating snapshots (All classes)..."
            echo "This may take a minute..."
            python3 utilities/capture_player_gui_snapshots.py --full
            echo ""
            echo "Done! Snapshots saved to: player_gui_snapshots/"
            read -p "Press Enter to continue..."
            ;;
        3)
            echo ""
            python3 utilities/analyze_snapshots.py
            echo ""
            read -p "Press Enter to continue..."
            ;;
        4)
            echo ""
            echo "Opening snapshot report..."
            if command -v xdg-open > /dev/null; then
                xdg-open player_gui_snapshots/player_gui_snapshots.md
            elif command -v open > /dev/null; then
                open player_gui_snapshots/player_gui_snapshots.md
            else
                echo "Please open: player_gui_snapshots/player_gui_snapshots.md"
            fi
            ;;
        5)
            echo ""
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please try again."
            echo ""
            ;;
    esac
done

