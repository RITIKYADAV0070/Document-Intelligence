import json

def evaluate():
    with open("outputs/final_output.json") as f:
        data = json.load(f)
    print("Overall Confidence:", data["overall_confidence_score"])

if __name__ == "__main__":
    evaluate()
