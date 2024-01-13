# VitalGuard: Advanced Health Management Powered by Google's Gemini Pro-Vision

## Introduction

VitalGuard is a cutting-edge health management tool powered by Google's Gemini Pro-Vision, designed to transform nutritional awareness and personal health tracking. This innovative application uses advanced AI to analyze food items in images, accurately estimating total calorie intake. It then tailors dietary recommendations based on the user's age, promoting informed and healthier eating habits. Whether you're seeking to maintain a balanced diet, monitor calorie consumption, or receive personalized nutrition advice, VitalGuard offers a smart, intuitive solution to meet your dietary needs.

## Requirements

To run the Health Management App, you'll need the following dependencies:

1. streamlit - for the web application framework.
2. google-generativeai - for leveraging AI capabilities.
3. python-dotenv - for managing environment variables.

## Configuration

To configure the app, set up the `.env` file with the necessary environment variables such as API keys and database configurations.

## Installation

To install the Health Management App, follow these steps:

1. Clone the repository from GitHub.
2. Navigate to the app's directory.
3. Run `pip install -r requirements.txt` to install the required dependencies.

## Steps to Setup and Run

### Step 1: Create a Virtual Environment

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated environments for them.

To create a virtual environment, navigate to the directory where you want to create your environment and run the following command in your terminal:

```bash
python -m venv myenv
```

This will create a new directory named `myenv` in your current directory. This is your new virtual environment.

### Step 2: Activate the Virtual Environment

After you've created a virtual environment, you'll need to activate it.

If you're using Windows, you can do this by running the following command in cmd.exe:

```bash
myenv\Scripts\activate.bat
```

### Step 3: Navigate to the Project Directory

Navigate to the project directory using the `cd` command:

```bash
cd path_of_project_directory
```

Replace `path_of_project_directory` with the actual path to your project directory.

### Step 4: Install Required Dependencies

This project comes with a `requirements.txt` file, which contains a list of all the Python dependencies needed to run the project.

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

The project can be run using Streamlit. If you've installed all the dependencies correctly, you can start the project by running the following command:

```bash
streamlit run main.py
```

This will start the server, and you can navigate to the URL provided in the console to view the application.

## Usage

Here's how to use the app:

1. Start the app by running `streamlit run main.py`.
2. Follow the on-screen instructions to navigate through the app.
3. Utilize the various features for health tracking and management.

## Contributing

Contributions to the Health Management App are welcome. Please follow the standard fork-pull request workflow for contributions.

## Troubleshooting

If you encounter any problems during setup or running of the project, please check that you've correctly followed all the steps above.
If you're still experiencing problems, feel free to reach out or open an issue.

## DEMO

https://github.com/debjyotirshi2303/
