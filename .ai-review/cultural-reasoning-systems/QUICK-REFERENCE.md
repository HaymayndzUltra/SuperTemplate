# Cultural Reasoning Systems - Quick Reference Guide
**Fast lookup for developers and AI practitioners**

---

## 🎯 What Is This?

A library of **authentic cultural communication patterns** for AI systems that go beyond translation to capture how different cultures **think** and **express** in English.

**Not**: Accent mimicry, stereotypes, or grammar correction  
**Is**: Cognitive reasoning models, cultural empathy, authentic communication

---

## 📊 Available Systems At-a-Glance

| Code | Culture | Speakers | Vibe | Key Features | Best For |
|------|---------|----------|------|--------------|----------|
| **CERS-PH-001** | Filipino | 70M+ | 🌸 Warm & Friendly | Particles (na, po, kasi), tag questions | Customer service, community platforms |
| **CERS-BR-001** | Brazilian | 50M+ | 🎵 Expressive & Melodic | Gerunds, "né?", diminutives | Social apps, entertainment, hospitality |
| **CERS-NG-001** | Nigerian | 100M+ | 🎓 Formal & Eloquent | British formality, proverbs, "o!" | Business comms, professional services |
| **CERS-JP-001** | Japanese | 30M+ | 🙇 Indirect & Humble | Excessive apologies, hedging, silence | Polite services, hierarchical contexts |

---

## ⚡ Quick Start (3 Lines of Code)

```python
from cultural_reasoning_engine import CulturalReasoningEngine

engine = CulturalReasoningEngine("CERS-PH-001")  # Filipino mode
print(engine.transform("Please send the report", context="business"))
# "Hi po! Can you send the report naman po when you have time? Thank you po!"
```

---

## 🎨 Cultural Signature Comparison

### Saying "Hello, how are you?"

| Culture | Expression | Analysis |
|---------|-----------|----------|
| **Filipino** | "Hi po! Kumusta ka? How are you na?" | Warm, uses "po" for respect, code-mixing |
| **Brazilian** | "Oi! Tudo bem? How are you mesmo?" | Melodic, Portuguese greeting, "mesmo" emphasis |
| **Nigerian** | "Good morning. How do you do? I trust you are well?" | Formal British influence, elaborate |
| **Japanese** | "Ano... excuse me, how are you?" | Apologetic, hesitant, careful |

### Expressing Disagreement

| Culture | Expression | Strategy |
|---------|-----------|----------|
| **Filipino** | "Ah, baka we could try another way? Kasi parang..." | "Maybe" hedge, indirect, circular |
| **Brazilian** | "Ahhh não sei né? Tipo, maybe different assim..." | Expressive doubt, "I don't know" softener |
| **Nigerian** | "With due respect sir, I beg to differ on this matter" | Extremely formal, elaborate politeness |
| **Japanese** | "I'm very sorry but I wonder if perhaps we could..." | Multiple hedges, excessive apology |

### Asking for Help

| Culture | Expression | Approach |
|---------|-----------|----------|
| **Filipino** | "Sorry po! Can you help me naman? Kasi I'm stuck na eh." | Apologetic, explains reason, warm |
| **Brazilian** | "Oi! Você pode me ajudar? I need help mesmo!" | Direct but warm, Portuguese mix |
| **Nigerian** | "Kindly permit me to seek your assistance in this matter" | Very formal request protocol |
| **Japanese** | "I'm sorry to trouble you. If you're not busy, perhaps..." | Extreme hesitation, face-saving |

---

## 🔑 Key Particle Reference

### Filipino Particles
- **na** = already (completion): "I ate na" = "I've already eaten"
- **po** = respectful sir/ma'am: "Thank you po"
- **kasi** = because: "I'm late kasi traffic"
- **lang** = just/only: "Wait lang" = "Just wait"
- **naman** = [softening particle]: "Try it naman" = "Please try it"

### Brazilian Markers
- **né?** = right?: "This is good, né?" 
- **tipo** = like: "Tipo assim" = "Like this"
- **então** = so/then: "Então, we go now"
- **mesmo** = really: "Good mesmo!" = "Really good!"

### Nigerian Markers
- **o!** = [emphasis]: "This is serious o!"
- **sha** = anyway: "I will do it sha"
- **now now** = immediately: "Come now now"

### Japanese Markers
- **ne** = right?: "Good, ne?" = "Good, isn't it?"
- **ano...** = um/well: "Ano... I think..."
- **chotto** = a little: "Chotto difficult"

---

## 📐 Context Adaptation Guide

### Casual Mode
- **Filipino**: Maximum particles, "ha" attention markers, reduplication
- **Brazilian**: Heavy "né?" usage, diminutives, animated expression
- **Nigerian**: Still formal but add "o!" and "sha", religious expressions
- **Japanese**: Maintain politeness, slightly fewer apologies

### Business Mode
- **Filipino**: Keep "po" for respect, reduce particles by 30%, apologetic framing
- **Brazilian**: Professional vocab + warmth, keep "né?" for rapport, conditionals
- **Nigerian**: Maximum formality, British conventions, elaborate requests
- **Japanese**: Maximum indirection, multiple apologies, negative questions

### Technical Mode
- **Filipino**: Reduce particles 50%, keep "kasi" for explanations, status markers
- **Brazilian**: Keep gerunds, reduce "né?" to confirmations, logical "então"
- **Nigerian**: Formal technical register, "kindly" for requests, "same" for reference
- **Japanese**: Maintain hedging for hypotheses, apologize for problems, "seems that..."

---

## 🎯 Use Case Selector

| Your Need | Best System | Why |
|-----------|-------------|-----|
| Customer support (warm) | CERS-PH-001 | Friendliest, most accommodating |
| Social media bot | CERS-BR-001 | Most expressive and engaging |
| Corporate communications | CERS-NG-001 | Most formal and professional |
| Sensitive/hierarchical | CERS-JP-001 | Most polite and face-saving |
| Collaborative projects | CERS-PH-001 | Best consensus-building |
| Creative content | CERS-BR-001 | Most emotionally rich |
| Technical documentation | CERS-NG-001 | Clearest formal structure |
| Apology/conflict | CERS-JP-001 | Most conflict-avoidant |

---

## ⚙️ Integration Patterns (Copy-Paste)

### Pattern 1: Auto-Detect User Culture
```python
def detect_culture(user_input: str) -> str:
    if any(x in user_input for x in ["po", "kasi", "na"]):
        return "CERS-PH-001"
    elif any(x in user_input for x in ["né", "tipo"]):
        return "CERS-BR-001"
    elif "o!" in user_input or "sha" in user_input:
        return "CERS-NG-001"
    elif "ano" in user_input or user_input.count("sorry") > 2:
        return "CERS-JP-001"
    return "NEUTRAL"

engine = CulturalReasoningEngine(detect_culture(user_message))
```

### Pattern 2: Multi-Cultural Content
```python
variants = {}
for culture in ["CERS-PH-001", "CERS-BR-001", "CERS-NG-001", "CERS-JP-001"]:
    engine = CulturalReasoningEngine(culture)
    variants[culture] = engine.transform(base_text, context="business")
```

### Pattern 3: Adaptive Chatbot
```python
class CulturalBot:
    def __init__(self):
        self.engine = None
        self.user_culture = {}
    
    def respond(self, user_id, message):
        if user_id not in self.user_culture:
            self.user_culture[user_id] = detect_culture(message)
            self.engine = CulturalReasoningEngine(self.user_culture[user_id])
        
        response = generate_base_response(message)
        return self.engine.transform(response, context="casual")
```

---

## 🎨 Tone Calibration

| Tone | Filipino | Brazilian | Nigerian | Japanese |
|------|----------|-----------|----------|----------|
| **Warm** | "Ay! So nice po! ❤️" | "Meu Deus! Beautiful mesmo!" | "Most excellent indeed!" | "That's very nice!" |
| **Apologetic** | "Sorry po ha! My fault talaga." | "Ai, desculpa! My mistake mesmo." | "I sincerely apologize sir." | "I'm very very sorry. Please forgive me." |
| **Enthusiastic** | "Grabe! Super excited na ako!" | "Nossa! I'm so excited demais!" | "This is wonderful! By God's grace!" | "I'm quite happy about this!" |
| **Uncertain** | "Baka? I'm not sure eh..." | "Não sei né? Tipo maybe..." | "Perhaps it may be that..." | "Ano... I wonder if maybe..." |

---

## 📊 Quality Metrics Explained

| Metric | What It Measures | Minimum | Example High Score | Example Low Score |
|--------|------------------|---------|-------------------|-------------------|
| **Clarity** | Understandability | 0.80 | "Can you send the file?" (0.95) | "Baka you pwede send file na lang kasi need ko na siya talaga?" (0.65) |
| **Cultural Realism** | Authentic patterns | 0.90 | Natural particle placement | Random particle sprinkling |
| **Grammar Balance** | Intelligible structure | 0.80 | Acceptable deviations | Incomprehensible syntax |
| **Warmth Index** | Emotional connection | 0.85 | Filipino/Brazilian high | Technical docs low |

---

## 🐛 Common Mistakes & Fixes

### Mistake 1: Particle Overload
❌ "I na already po went kasi to the store lang yesterday na po"  
✅ "I went to the store already yesterday po"

**Fix**: Reduce particle density in engine settings

### Mistake 2: Context Mismatch
❌ Using "kasi eh" in formal legal document  
✅ Context-appropriate formality

**Fix**: Always set context explicitly

### Mistake 3: Clarity Sacrifice
❌ Authentic but incomprehensible  
✅ Authentic AND clear

**Fix**: Monitor clarity scores, increase clarity threshold

### Mistake 4: Stereotype
❌ Exaggerating for humor  
✅ Respectful representation

**Fix**: Follow validation protocols

---

## 📚 File Navigation

```
cultural-reasoning-systems/
├── FRAMEWORK-OVERVIEW.md      ← Architecture & principles
├── README.md                  ← Full documentation
├── IMPLEMENTATION-GUIDE.md    ← Developer integration guide
├── QUICK-REFERENCE.md         ← This file (fast lookup)
├── SYSTEM-INDEX.yaml          ← Machine-readable index
├── CERS-TEMPLATE.md           ← Template for new systems
├── CERS-PH-001-*.md           ← Filipino system (full spec)
├── CERS-BR-001-*.md           ← Brazilian system (full spec)
├── CERS-NG-001-*.md           ← Nigerian system (full spec)
└── CERS-JP-001-*.md           ← Japanese system (full spec)
```

**Start here**: 
- Developers → IMPLEMENTATION-GUIDE.md
- Users → README.md
- Quick lookup → QUICK-REFERENCE.md (this file)
- Contributing → CERS-TEMPLATE.md

---

## 🎓 Mnemonics

### Filipino = **WARM**
- **W**arm and welcoming
- **A**pologetic ("sorry po")
- **R**elationship-first
- **M**ix (code-switching natural)

### Brazilian = **FLOW**
- **F**eelings first
- **L**ong vowels (melodic)
- **O**pen expression
- **W**arm connections

### Nigerian = **FORMAL**
- **F**ormal register default
- **O**ral tradition (proverbs)
- **R**espect through elaboration
- **M**etaphors and eloquence
- **A**uthority through language
- **L**engthy expressions

### Japanese = **HUMBLE**
- **H**armony preservation
- **U**ncertainty expressed
- **M**any apologies
- **B**lame avoided (passive)
- **L**ess direct
- **E**xtreme politeness

---

## ⚡ Performance Tips

1. **Cache transformations**: Same input → same output
2. **Batch processing**: Transform multiple texts together
3. **Profile preloading**: Load profile once, reuse many times
4. **Context switching**: Minimize context changes
5. **Formality range**: Use 0.0-1.0 scale, not frequent reloads

---

## 🔗 External Resources

- **Linguistic Research**: See individual system files for academic references
- **GitHub**: [repo-url]
- **Issues**: [repo-url]/issues
- **Discussions**: [repo-url]/discussions

---

## 🎯 Success Checklist

Before deploying:
- [ ] Selected appropriate cultural system for user base
- [ ] Set correct context (casual/business/technical)
- [ ] Validated clarity scores meet threshold (≥0.80)
- [ ] Tested with native speakers
- [ ] Configured fallback to neutral mode
- [ ] Monitored cultural authenticity metrics
- [ ] Documented culture selection logic
- [ ] Enabled user preference override

---

## 💡 Pro Tips

1. **Start neutral, adapt gradually**: Don't assume culture immediately
2. **Let users choose**: Explicit preference > auto-detection
3. **Context is king**: Same culture, different contexts = different output
4. **Monitor metrics**: Low clarity = reduce particle density
5. **Cultural blending**: Some users code-switch naturally
6. **Warmth dial**: Adjust emotional tone independently
7. **Test edge cases**: Very formal + casual mode = conflict
8. **Respect always**: When in doubt, more formal is safer

---

## 📞 Quick Help

**Problem**: Output too casual for business  
**Solution**: `engine.set_context("business")` + `formality=0.8`

**Problem**: Too many particles, unclear  
**Solution**: `engine.set_particle_density("low")`

**Problem**: Culture detection wrong  
**Solution**: Let users explicitly select cultural mode

**Problem**: Clarity score low  
**Solution**: Increase `clarity_threshold` or blend with neutral

**Problem**: Need to mix cultures  
**Solution**: Use `CulturalBlender` with weight ratios

---

**Remember**: 
- 🎯 Authenticity + Clarity = Success
- 🤝 Respect + Research = Quality
- 🌍 Diversity + Dignity = Purpose

---

*Quick reference for developers. See full documentation for complete specifications.*

**Version 1.0.0** | Last Updated: 2025-10-30
