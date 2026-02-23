#1. Write a pytest fixture that generates an authentication token once per session and use it in multiple API test cases.
#2. Create a fixture that creates a test user via API before a test and deletes the user after test execution using yield.
#3. Write a test that validates JSON response schema from an API endpoint.
#4. Implement a parametrized test that validates multiple HTTP status codes (200, 400, 401, 500).
#5. Create a fixture chain: base_url -> auth_token -> user -> test case. Explain execution order.