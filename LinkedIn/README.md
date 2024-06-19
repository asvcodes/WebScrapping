# LinkedIn Profile Scraper

This project provides a simple web scraping script to extract LinkedIn profile information from Google search results. This approach circumvents the complexities of direct LinkedIn scraping by leveraging Google search results. The script extracts names, emails, and LinkedIn profile URLs of individuals whose LinkedIn profiles appear in Google search results.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python**: Make sure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/).

2. **Google Chrome Browser**: The script uses Chrome WebDriver, so you need to have Google Chrome installed. You can download it from [Google Chrome's official website](https://www.google.com/chrome/).

3. **Chrome WebDriver**: Download the Chrome WebDriver that matches the version of your Google Chrome browser. You can find the compatible version from [ChromeDriver's official site](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Installation

1. **Clone the repository** (or download the script file):
   ```bash
   git clone https://github.com/yourusername/linkedin-profile-scraper.git
   cd linkedin-profile-scraper
   ```

2. **Install required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Chrome WebDriver**:
   - Download the Chrome WebDriver from the [official site](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Extract the WebDriver executable and place it in a directory of your choice.
   - Update the `service = Service("YOUR_DRIVER_PATH")` line in the script with the path to the WebDriver executable.

## Usage

1. **Run the script**:
   ```bash
   python linkedin_scraper.py
   ```

2. **Input the URL and iteration number** when prompted:
   - **URL**: Copy and paste the Google search URL that contains the LinkedIn profiles you want to scrape.
   - **Iteration**: Enter an iteration number to distinguish different runs of the script. This will be appended to the output filename.

3. The script will start scraping the LinkedIn profiles from the Google search results. It will automatically scroll through the search results and extract the profile information.

4. Once the scraping is completed, the script will save the extracted data to a CSV file named `linkedin_profiles<iteration>.csv` in the current directory.

## Acknowledgements

This code leverages Google search results to simplify LinkedIn profile scraping. Special thanks to [Recruitin.net](https://recruitin.net) for their x-ray search tool, which allows users to find LinkedIn profiles using Google search. By using Recruitin.net, you can generate the appropriate Google search URL and paste it into the script to perform the scraping.

## Notes

- The script is designed to extract emails ending with `@gmail.com`. If you want to extract different types of emails, modify the regex pattern in the script accordingly.
- Ensure you comply with LinkedIn's terms of service and data privacy regulations when using this script.
- This script is intended for educational and research purposes only.

## Disclaimer

This script is provided as-is without any warranty. The author is not responsible for any misuse of this script or any potential violations of terms of service of the websites involved.

## License - This project is licensed under the MIT License.
---
