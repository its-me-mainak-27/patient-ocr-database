import re
import json

def parse_data(extracted_text):
    """Parse extracted text into structured JSON format."""
    data = {
        "Patient Details": {},
        "Treatment Details": {},
        "Difficulty Ratings": {},
        "Patient Changes": {},
        "Pain Symptoms": {}
    }

    lines = extracted_text.split("\n")

    for line in lines:
        line = line.strip()
        if "Name:" in line:
            data["Patient Details"]["Name"] = line.split("Name:")[-1].strip()
        elif "DOB:" in line:
            data["Patient Details"]["DOB"] = line.split("DOB:")[-1].strip()
        elif "Injection" in line:
            data["Treatment Details"]["Injection"] = "Yes" if "Yes" in line else "No"
        elif "Exercise Therapy" in line:
            data["Treatment Details"]["Exercise Therapy"] = "Yes" if "Yes" in line else "No"
        elif "Pain Symptoms" in line:
            data["Pain Symptoms"]["Pain Level"] = line.split(":")[-1].strip()

    return data

# Example Usage
if __name__ == "__main__":
    extracted_text = """
    Name: John Doe
    DOB: 01/01/1990
    Injection: Yes
    Exercise Therapy: No
    Pain Symptoms: 7
    """
    
    structured_data = parse_data(extracted_text)

    # Save to JSON
    with open("output.json", "w") as json_file:
        json.dump(structured_data, json_file, indent=4)

