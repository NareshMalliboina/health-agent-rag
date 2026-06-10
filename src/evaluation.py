from src.agent import run_health_agent

def evaluate_agent():
    test_cases = [
        {"query": "What is the claim filing deadline?", "expected_keyword": "30 days"},
        {"query": "Are cosmetic surgeries covered?", "expected_keyword": "excluded"}
    ]
    
    passed = 0
    for i, test in enumerate(test_cases, 1):
        response = run_health_agent(test["query"])
        if test["expected_keyword"].lower() in response.lower():
            print(f"Test {i} Passed ✅")
            passed += 1
        else:
            print(f"Test {i} Failed ❌")
            
    print(f"\nEvaluation Complete: {passed}/{len(test_cases)} tests passed.")

if __name__ == "__main__":
    evaluate_agent()