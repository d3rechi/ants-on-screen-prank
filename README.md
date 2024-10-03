# Crawling Ants Simulation

## Description
This project creates a transparent window with animated ants that appear to crawl across the screen. It uses PyQt6 to render a frameless, transparent window with realistic ant movement.

## Features
- Transparent window that stays on top of other applications
- Realistic ant movement with smooth rotation
- Ants wrap around the edges of the screen
- Customizable number of ants, speed, and turn rate

## Requirements
- Python 3.6+
- PyQt6

## Installation
1. Ensure you have Python installed on your system.
2. Install PyQt6:
   ```
   pip install PyQt6
   ```
3. Clone this repository or download the source code.

## Usage
1. Place an `ant.png` image in the same directory as the script. This image should have a transparent background and the ant should be facing upwards.
2. Run the script:
   ```
   python main.py
   ```
3. Press the Escape key to close the application.

## Customization
You can customize the simulation by modifying the following parameters in the `main.py` file:
- Number of ants: Change the range in the list comprehension in the `TransparentWindow.__init__` method.
- Window size: Modify the `setGeometry` parameters in the `TransparentWindow.__init__` method.
- Ant size: Adjust the `scaled` parameters when loading the ant image.
- Movement speed and turn rate: Modify the `speed` and `turn_rate` variables in the `Ant.__init__` method.

## Contributing
Contributions to improve the simulation or add new features are welcome. Please feel free to submit a pull request or open an issue.
