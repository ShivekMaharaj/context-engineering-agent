class ContextManager:
    """Manages short-term conversation memory using a sliding window approach."""
    
    def __init__(self, token_limit=2000):
        self.history = []
        self.token_limit = token_limit

    def add_to_history(self, role, content):
        """Adds a message to history and prunes if the token limit is exceeded."""
        self.history.append({"role": role, "parts": [content]})
        
        # Pruning logic: Remove oldest messages until we are under the token limit
        while self.count_tokens() > self.token_limit:
            self.history.pop(0)

    def count_tokens(self):
        """Approximate token count (4 chars per token). Replace with tiktoken for production."""
        return len(str(self.history)) // 4