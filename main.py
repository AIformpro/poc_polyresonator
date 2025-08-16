#!/usr/bin/env python3
"""
POC 095 — XRL-05 · Auto-entraînement cross-réel (capteurs simulés)
Description: Boucle capteur-action simulée avec bruit; apprentissage de seuil par recherche naïve.
Usage: python main.py
"""

import json, random
def simulate(n=20, threshold=0.5, noise=0.1):
    hits = 0
    for i in range(n):
        sensor = random.random()
        s = sensor + random.uniform(-noise, noise)
        action = 1 if s > threshold else 0
        hits += action
    return hits/n
def search():
    best=(0,0)
    for thr in [i/20 for i in range(5,16)]:
        acc = simulate(n=30, threshold=thr, noise=0.12)
        if acc>best[1]: best=(thr,acc)
    return {"best_thr": round(best[0],2), "acc": round(best[1],3)}
if __name__ == "__main__":
    print(json.dumps(search(), ensure_ascii=False))