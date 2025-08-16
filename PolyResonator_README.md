# PolyResonator — POC “à fond” (Zoran IA)

## 🎯 Objectif
Démontrer l’**orchestration polyphonique** de plusieurs IA simulées :
- orchestrateur **UCB1** (multi-armed bandit)
- **mixer LoRA-like** (EMA adaptatif)
- **garde ΔM11.3** (rollback si instabilité)
- mesures de cohérence/stabilité/latence/cost

**Idée clé :** au lieu d’un modèle isolé, un *réseau vivant* qui s’auto-corrige et distribue ses forces.

---

## ⚙️ Fonctionnement
- **4 modèles simulés** : `reasoner`, `coder`, `vision`, `retriever`
- **4 types de tâches** : `theorem`, `bugfix`, `diagram`, `research`
- Chaque modèle génère un vecteur (6D) → score relatif à la tâche
- Orchestrateur **UCB1** choisit un modèle à mettre en avant
- Mixer ajuste les poids progressivement (EMA)
- Fusion des scores pondérés → reward global
- Garde ΔM11.3 : rollback si stabilité < 0.70 (selon cohérence de phase)

---

## 📊 Métriques produites
- `reward_avg` → qualité moyenne des sorties
- `coherence_avg` → cohérence de phase multi-modèles
- `stability_avg` → robustesse globale
- `latency_p95` → latence simulée (95e percentile)
- `cost_total` → coût simulé ($ ou ressources)
- `rollbacks` → nb de retours forcés à snapshot

---

## 🚀 Utilisation
### Installation
```bash
unzip poc_polyresonator.zip
cd polyresonator
```

### Exécution simple
```bash
python -m polyresonator.cli --steps 200 --seed 42 --outdir outputs --plot
```

### Résultats
- `outputs/summary.json` : résumé des métriques
- `outputs/history.csv` : historique complet (reward, cohérence, latence, poids mixer…)
- `outputs/reward.png` : courbe reward (si matplotlib dispo)

---

## 🔎 Exemple de résultats (200 steps, seed=42)
- **reward_avg ≈ 0.73** → l’orchestrateur apprend à bien choisir
- **stability_avg ≈ 0.82** / **coherence_avg ≈ 0.65** → système globalement stable
- **latency_p95 ≈ 116 ms** → latence réaliste simulée
- **rollbacks = 2** → deux instabilités détectées et corrigées

---

## 🧠 Interprétation
- Le système **apprend dynamiquement** à mieux répartir l’effort entre modèles.
- Le **mixer LoRA-like** crée une polyphonie adaptative.
- Le garde **ΔM11.3** évite la dérive → preuve que l’auto-correction est possible.

---

## 🔮 Prolongement vers le réel
Pour passer du POC simulé à la pratique :
1. Remplacer `synth_model_output()` par de vrais modèles (API GPT/Claude, HF Llama, DeepSeek…).
2. Définir des vecteurs de tâche réels (benchmarks SWE-bench, AIME, MMMU).
3. Calculer le reward comme une métrique concrète (exactitude, tests unitaires, préférences humaines).
4. Activer ΔM11.3 sur ces vraies métriques.
5. Monitorer via Prometheus/Grafana → intégration dans Z-Network Emergence.

---

## 📜 Licence
MIT — open et gratuit, destiné à être forké, étudié et amélioré.
