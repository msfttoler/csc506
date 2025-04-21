from collections import defaultdict
import random

class HashRecommender:

    def __init__(self, bucket_count: int = 131071):  # prime ≈ 1e5
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]

    def _hash(self, user_id: str) -> int:
        return hash(user_id) % self.bucket_count

    def add_interaction(self, user_id: str, content_id: str) -> None:
        idx = self._hash(user_id)
        self.buckets[idx].append(content_id)

    def get_recommendations(self, user_id: str, k: int = 5):
        idx = self._hash(user_id)
        # Deduplicate while preserving recency
        seen = set()
        recs = []
        for cid in reversed(self.buckets[idx]):  # iterate from most‑recent
            if cid not in seen:
                recs.append(cid)
                seen.add(cid)
            if len(recs) == k:
                break
        return list(reversed(recs))

def demo():
    rec = HashRecommender()
    users = [f"user{i}" for i in range(10)]
    contents = [f"post{j}" for j in range(50)]
    for _ in range(500):
        rec.add_interaction(random.choice(users), random.choice(contents))
    sample_user = users[0]
    return sample_user, rec.get_recommendations(sample_user)

if __name__ == "__main__":
    u, recs = demo()
    print("Sample user:", u)
    print("Recommendations:", recs)
