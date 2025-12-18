import requests
import re
import os

class SageMathAPIClient:
    def __init__(self, base_url: str | None = None):
        """
        base_url precedence (highest to lowest):
        1. base_url argument
        2. SAGEMATH_API_BASE_URL env var (e.g. http://api:8000)
        3. SAGEMATH_API_HOST + SAGEMATH_API_PORT env vars
        4. Default: http://127.0.0.1:8000
        """
        if base_url is not None:
            self.base_url = base_url.rstrip("/")
        else:
            env_base = os.getenv("SAGEMATH_API_BASE_URL")
            if env_base:
                self.base_url = env_base.rstrip("/")
            else:
                host = os.getenv("SAGEMATH_API_HOST", "127.0.0.1")
                port = os.getenv("SAGEMATH_API_PORT", "8000")
                self.base_url = f"http://{host}:{port}"

    def get_oppermann_counts(self, input: str) -> tuple[int, int]:
        """
        Calls the /oppermann_counts/ endpoint and returns a tuple of two integers.
        Example output: (9, 11)
        """
        url = f"{self.base_url}/oppermann_counts/"
        params = {"input": input}

        # Make REST call
        response = requests.get(url, params=params, headers={"accept": "application/json"})
        response.raise_for_status()  # Raises if HTTP status is not 200

        data = response.json()

        # Validate returncode
        if data.get("returncode") != 0:
            raise RuntimeError(f"Remote process failed: returncode={data.get('returncode')} stderr={data.get('stderr')}")

        # Extract two integers from stdout -> e.g. "(9, 11)\n"
        stdout = data.get("stdout", "")

        # Use regex to extract digits or negatives
        numbers = re.findall(r"-?\d+", stdout)

        if len(numbers) != 2:
            raise ValueError(f"Expected two integers in stdout, got: {stdout}")

        a, b = map(int, numbers)
        return a, b
