class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        
        for email in emails:
            # Split into two parts: local and domain.
            name, domain = email.split('@')

             # Split local by '+' and replace all '.' with ''.
            local = name.split('+')[0].replace('.', '')

            # Concatenate local, '@', and domain.
            uniqueEmails.add(local + '@' + domain)
        
        return len(uniqueEmails)