#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from mydebate.crew import Mydebate

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    inputs = {
        'motion': 'AI LLMs are a threat to humanity. There needs to be strict regulation on AI LLMs.'
    }
    
    try:
        result = Mydebate().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "motion": "AI LLMs are a threat to humanity. There needs to be strict regulation on AI LLMs."
    }
    try:
        result = Mydebate().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
        print(result.raw)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        result = Mydebate().crew().replay(task_id=sys.argv[1])
        print(result.raw)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "motion": "AI LLMs are a threat to humanity. There needs to be strict regulation on AI LLMs."
    }
    
    try:
        result = Mydebate().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
        print(result.raw)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
